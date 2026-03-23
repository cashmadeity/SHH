const https = require('https');

const OPENROUTER_KEY = process.env.OPENROUTER_API_KEY;
const MODEL = 'meta-llama/llama-3-70b-instruct';

if (!OPENROUTER_KEY) {
  console.error('❌ No API key');
  process.exit(1);
}

const payload = JSON.stringify({
  model: MODEL,
  messages: [{ role: 'user', content: 'Extract 3 key concepts from: "Machine learning is a subset of AI that uses algorithms to learn from data."' }],
  temperature: 0.3,
  max_tokens: 500,
});

console.log('🔗 Testing OpenRouter API...');

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
        console.error(`❌ OpenRouter error: ${response.error.message}`);
        process.exit(1);
      }
      console.log('✅ OpenRouter API works!');
      console.log('\nResponse:');
      console.log(response.choices[0].message.content);
    } catch (e) {
      console.error(`❌ Parse error: ${e.message}`);
      process.exit(1);
    }
  });
});

req.on('error', e => {
  console.error(`❌ Network error: ${e.message}`);
  process.exit(1);
});

req.write(payload);
req.end();
