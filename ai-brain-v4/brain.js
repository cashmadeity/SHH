import fs from "fs"
import os from "os"
import path from "path"

const base = path.join(os.homedir(), "Desktop", "AI_BRAIN")

// Ensure directory exists
if (!fs.existsSync(base)) {
  fs.mkdirSync(base, { recursive: true })
}

function read(file) {
  try {
    return JSON.parse(fs.readFileSync(path.join(base, file)))
  } catch {
    return file === "memory.json" ? { user: {}, knowledge: [], history: [], failures: [] }
         : file === "skills.json" ? []
         : []
  }
}

function write(file, data) {
  fs.writeFileSync(path.join(base, file), JSON.stringify(data, null, 2))
}

function backup(file, data) {
  const timestamp = Date.now()
  fs.writeFileSync(
    path.join(base, `${file}_backup_${timestamp}.json`),
    JSON.stringify(data, null, 2)
  )
}

let memory = read("memory.json")
let skills = read("skills.json")
let cache = read("cache.json")

function sim(a, b) {
  a = a.toLowerCase()
  b = b.toLowerCase()
  let score = 0
  a.split(" ").forEach(word => {
    if (b.includes(word)) score++
  })
  return score
}

function cacheCheck(input) {
  let best = null
  let bestScore = 0
  cache.forEach(c => {
    let score = sim(input, c.input)
    if (score > bestScore) {
      bestScore = score
      best = c
    }
  })
  return bestScore > 3 ? best.output : null
}

function skillFind(input) {
  let best = null
  let bestScore = 0
  skills.forEach(skill => {
    let score = sim(input, skill.name + " " + (skill.trigger || []).join(" "))
    if (score > bestScore) {
      bestScore = score
      best = skill
    }
  })
  return bestScore > 2 ? best : null
}

function route(input) {
  const agentMap = {
    translator: "translate language multilingual",
    persuasion: "sell persuade convert marketing",
    teacher: "teach explain learn tutorial",
    style: "tone rewrite voice style",
    interpersonal: "emotion reply message relationship",
    architect: "system design architecture plan",
    code: "code api function programming",
    analyst: "analyze compare evaluate data",
    research: "research info find investigate",
    optimizer: "optimize improve efficiency"
  }
  
  return Object.entries(agentMap)
    .map(([agent, keywords]) => [agent, sim(input, keywords)])
    .filter(([_, score]) => score > 1)
    .sort((a, b) => b[1] - a[1])
    .map(([agent]) => agent)
}

function extractSkill(input, output) {
  if (output.length < 50) return
  
  const skill = {
    name: input.slice(0, 40),
    trigger: input.split(" ").slice(0, 5),
    steps: ["analyze", "process", "output"],
    usage_count: 0,
    success_score: 1.0,
    created_at: new Date().toISOString()
  }
  
  skills.push(skill)
  write("skills.json", skills)
}

export async function runBrain(input, callAI) {
  // Reload on each run (in case edited manually)
  memory = read("memory.json")
  skills = read("skills.json")
  cache = read("cache.json")

  // STEP 1: Check cache
  let cached = cacheCheck(input)
  if (cached) return cached

  // STEP 2: Find skill
  let skill = skillFind(input)
  if (skill) {
    skill.usage_count = (skill.usage_count || 0) + 1
    write("skills.json", skills)
    backup("skills", skills)
    return `[SKILL:${skill.name}]`
  }

  // STEP 3: Route agents
  let agents = route(input)

  // STEP 4: Call AI
  let prompt = `MODE: LOW_COST
AGENTS: ${agents.join(",")}
RULES:
- concise
- no fluff
INPUT:
${input}`

  let output = await callAI(prompt)

  // STEP 5: Compress
  if (output.length > 300) {
    output = output.slice(0, 300)
  }

  // STEP 6: Store + Backup
  cache.push({ input, output, timestamp: new Date().toISOString() })
  write("cache.json", cache)
  backup("cache", cache)

  // STEP 7: Extract skill
  extractSkill(input, output)

  // STEP 8: Auto-backup memory
  write("memory.json", memory)
  backup("memory", memory)

  return output
}
