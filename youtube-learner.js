#!/usr/bin/env node

/**
 * YOUTUBE LEARNER - Extract & learn from YouTube transcripts via OpenRouter LLM
 * 
 * Usage:
 *   node youtube-learner.js <youtube-url>
 *   node youtube-learner.js https://www.youtube.com/watch?v=dQw4w9WgXcQ
 * 
 * Outputs:
 *   - Extracted concepts (JSON)
 *   - Key takeaways
 *   - Vocabulary learned
 *   - Stored in memory/youtube-learned/
 */

const fs = require('fs');
const path = require('path');
const { execSync } = require('child_process');
const https = require('https');

// Load OpenRouter API key
const credPath = path.join(__dirname, '../.openclaw/credentials/openrouter.env');
let OPENROUTER_KEY = '';

if (fs.existsSync(credPath)) {
  const env = fs.readFileSync(credPath, 'utf8');
  const match = env.match(/OPENROUTER_API_KEY="(.+?)"/);
  if (match) OPENROUTER_KEY = match[1];
}

if (!OPENROUTER_KEY) {
  console.error('❌ OpenRouter API key not found. Set it in .openclaw/credentials/openrouter.env');
  process.exit(1);
}

const OPENROUTER_URL = 'https://openrouter.ai/api/v1/chat/completions';
const MODEL = 'meta-llama/llama-3-70b-instruct';

// ============================================================================
// STEP 1: Fetch YouTube transcript
// ============================================================================

async function fetchTranscript(youtubeUrl) {
  console.log(`📺 Fetching transcript from: ${youtubeUrl}`);

  try {
    // Extract video ID
    const videoId = youtubeUrl.match(/(?:youtube\.com\/watch\?v=|youtu\.be\/)([a-zA-Z0-9_-]{11})/)?.[1];
    if (!videoId) throw new Error('Invalid YouTube URL');

    // Use yt-dlp to fetch transcript
    const cmd = `yt-dlp --write-auto-sub --sub-lang en --skip-download "${youtubeUrl}" -o /tmp/yt_%(id)s 2>&1`;
    const output = execSync(cmd, { encoding: 'utf8', maxBuffer: 10 * 1024 * 1024 });

    // Find the subtitle file
    const subFile = `/tmp/yt_${videoId}.en.vtt`;
    if (!fs.existsSync(subFile)) {
      throw new Error('Could not fetch transcript. Video may have no captions.');
    }

    // Parse VTT to plain text
    let transcript = fs.readFileSync(subFile, 'utf8');
    transcript = transcript
      .split('\n')
      .filter(line => !line.startsWith('WEBVTT') && !line.match(/^\d+:\d+/) && line.trim())
      .join(' ')
      .replace(/\s+/g, ' ');

    console.log(`✅ Transcript fetched (${transcript.length} chars)`);
    return { videoId, transcript };
  } catch (error) {
    console.error(`❌ Transcript fetch failed: ${error.message}`);
    throw error;
  }
}

// ============================================================================
// STEP 2: Extract concepts via LLM
// ============================================================================

async function extractConcepts(transcript, videoTitle) {
  console.log('🧠 Extracting concepts with LLM...');

  const prompt = `
You are an expert knowledge extractor. Analyze this YouTube transcript and extract:

TRANSCRIPT:
${transcript.substring(0, 4000)}...

Extract and return ONLY valid JSON (no markdown, no backticks):
{
  "title": "video title",
  "key_concepts": ["concept1", "concept2", ...],
  "main_takeaways": ["takeaway1", "takeaway2", ...],
  "vocabulary": ["word1", "word2", ...],
  "summary": "2-3 sentence summary"
}
`;

  return new Promise((resolve, reject) => {
    const payload = JSON.stringify({
      model: MODEL,
      messages: [{ role: 'user', content: prompt }],
      temperature: 0.3,
      max_tokens: 1000,
    });

    const options = {
      hostname: 'openrouter.ai',
      path: '/api/v1/chat/completions',
      method: 'POST',
      headers: {
        'Authorization': `Bearer ${OPENROUTER_KEY}`,
        'Content-Type': 'application/json',
        'Content-Length': Buffer.byteLength(payload),
      },
    };

    const req = https.request(options, (res) => {
      let data = '';
      res.on('data', chunk => data += chunk);
      res.on('end', () => {
        try {
          const response = JSON.parse(data);
          if (response.error) {
            reject(new Error(`OpenRouter error: ${response.error.message}`));
          } else {
            const content = response.choices[0].message.content;
            const json = JSON.parse(content);
            console.log('✅ Concepts extracted');
            resolve(json);
          }
        } catch (e) {
          reject(new Error(`Failed to parse LLM response: ${e.message}`));
        }
      });
    });

    req.on('error', reject);
    req.write(payload);
    req.end();
  });
}

// ============================================================================
// STEP 3: Store in memory
// ============================================================================

function storeInMemory(videoId, concepts) {
  const memDir = path.join(__dirname, 'memory/youtube-learned');
  if (!fs.existsSync(memDir)) fs.mkdirSync(memDir, { recursive: true });

  const entry = {
    videoId,
    timestamp: new Date().toISOString(),
    ...concepts,
  };

  const filename = path.join(memDir, `${videoId}.json`);
  fs.writeFileSync(filename, JSON.stringify(entry, null, 2));

  console.log(`💾 Stored in: ${filename}`);
  return filename;
}

// ============================================================================
// STEP 4: Update master knowledge index
// ============================================================================

function updateKnowledgeIndex(videoId, concepts) {
  const indexPath = path.join(__dirname, 'memory/youtube-index.json');
  let index = {};

  if (fs.existsSync(indexPath)) {
    index = JSON.parse(fs.readFileSync(indexPath, 'utf8'));
  }

  index[videoId] = {
    title: concepts.title,
    concepts: concepts.key_concepts,
    timestamp: new Date().toISOString(),
  };

  fs.writeFileSync(indexPath, JSON.stringify(index, null, 2));
  console.log('📑 Knowledge index updated');
}

// ============================================================================
// MAIN
// ============================================================================

async function main() {
  const url = process.argv[2];
  if (!url) {
    console.error('Usage: node youtube-learner.js <youtube-url>');
    process.exit(1);
  }

  try {
    const { videoId, transcript } = await fetchTranscript(url);
    const concepts = await extractConcepts(transcript, '');
    storeInMemory(videoId, concepts);
    updateKnowledgeIndex(videoId, concepts);

    console.log('\n✅ Learning complete!');
    console.log(`   Video ID: ${videoId}`);
    console.log(`   Concepts learned: ${concepts.key_concepts.length}`);
    console.log(`   Vocabulary: ${concepts.vocabulary.length} words`);
  } catch (error) {
    console.error(`\n❌ Error: ${error.message}`);
    process.exit(1);
  }
}

main();
