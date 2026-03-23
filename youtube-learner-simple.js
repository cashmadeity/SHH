#!/usr/bin/env node

/**
 * YOUTUBE LEARNER (Simplified) - Extract & learn from YouTube transcripts
 * Uses YouTube Transcript API (free, no API key needed)
 */

const https = require('https');
const fs = require('fs');
const path = require('path');

let OPENROUTER_KEY = process.env.OPENROUTER_API_KEY;

if (!OPENROUTER_KEY) {
  const credPath = path.join(__dirname, '../.openclaw/credentials/openrouter.env');
  if (fs.existsSync(credPath)) {
    const env = fs.readFileSync(credPath, 'utf8');
    const match = env.match(/OPENROUTER_API_KEY="(.+?)"/);
    if (match) OPENROUTER_KEY = match[1];
  }
}

if (!OPENROUTER_KEY) {
  console.error('❌ OpenRouter API key not found');
  process.exit(1);
}

const MODEL = 'meta-llama/llama-3-70b-instruct';

// ============================================================================
// Fetch transcript from YouTube (using noembed API)
// ============================================================================

function fetchTranscript(youtubeUrl) {
  return new Promise((resolve, reject) => {
    const videoId = youtubeUrl.match(/(?:youtube\.com\/watch\?v=|youtu\.be\/)([a-zA-Z0-9_-]{11})/)?.[1];
    if (!videoId) {
      reject(new Error('Invalid YouTube URL'));
      return;
    }

    console.log(`📺 Fetching transcript for: ${videoId}`);

    // Use YouTube Transcript API
    const apiUrl = `https://www.youtube.com/api/timedtext?v=${videoId}&lang=en`;
    
    https.get(apiUrl, (res) => {
      let data = '';
      res.on('data', chunk => data += chunk);
      res.on('end', () => {
        try {
          // Parse XML transcript
          const transcript = data
            .split('</text>')
            .filter(line => line.includes('<text'))
            .map(line => {
              const match = line.match('>(.+?)<');
              return match ? decodeURIComponent(match[1]).replace(/\+/g, ' ') : '';
            })
            .join(' ');

          if (!transcript) {
            reject(new Error('No transcript found. Video may not have captions.'));
            return;
          }

          console.log(`✅ Transcript fetched (${transcript.length} chars)`);
          resolve({ videoId, transcript });
        } catch (e) {
          reject(e);
        }
      });
    }).on('error', reject);
  });
}

// ============================================================================
// Extract concepts via OpenRouter LLM
// ============================================================================

function extractConcepts(transcript) {
  return new Promise((resolve, reject) => {
    const prompt = `Analyze this transcript and extract key concepts, takeaways, and vocabulary.

TRANSCRIPT (first 3000 chars):
${transcript.substring(0, 3000)}

Return ONLY valid JSON (no markdown):
{
  "key_concepts": ["concept1", "concept2", "concept3"],
  "main_takeaways": ["takeaway1", "takeaway2"],
  "vocabulary": ["word1", "word2", "word3"],
  "summary": "1-2 sentence summary"
}`;

    const payload = JSON.stringify({
      model: MODEL,
      messages: [{ role: 'user', content: prompt }],
      temperature: 0.3,
      max_tokens: 800,
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

    console.log('🧠 Extracting concepts with LLM...');

    const req = https.request(options, (res) => {
      let data = '';
      res.on('data', chunk => data += chunk);
      res.on('end', () => {
        try {
          const response = JSON.parse(data);
          if (response.error) {
            reject(new Error(`OpenRouter: ${response.error.message}`));
            return;
          }
          const content = response.choices[0].message.content;
          const json = JSON.parse(content);
          console.log('✅ Concepts extracted');
          resolve(json);
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
// Store in memory
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
  console.log(`💾 Stored: ${filename}`);

  // Update index
  const indexPath = path.join(__dirname, 'memory/youtube-index.json');
  let index = {};
  if (fs.existsSync(indexPath)) {
    index = JSON.parse(fs.readFileSync(indexPath, 'utf8'));
  }

  index[videoId] = {
    title: concepts.summary,
    concepts: concepts.key_concepts,
    timestamp: new Date().toISOString(),
  };

  fs.writeFileSync(indexPath, JSON.stringify(index, null, 2));
  console.log('📑 Index updated');
}

// ============================================================================
// Main
// ============================================================================

async function main() {
  const url = process.argv[2];
  if (!url) {
    console.error('Usage: node youtube-learner-simple.js <youtube-url>');
    process.exit(1);
  }

  try {
    const { videoId, transcript } = await fetchTranscript(url);
    const concepts = await extractConcepts(transcript);
    storeInMemory(videoId, concepts);

    console.log('\n✅ Learning complete!');
    console.log(`📚 Video: ${videoId}`);
    console.log(`📖 Concepts: ${concepts.key_concepts.join(', ')}`);
  } catch (error) {
    console.error(`\n❌ Error: ${error.message}`);
    process.exit(1);
  }
}

main();
