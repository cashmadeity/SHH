#!/usr/bin/env node

/**
 * YOUTUBE LEARNER WEB UI
 * Runs on http://localhost:9000 (or configurable port)
 * Cross-platform: access from Windows, macOS, Linux
 */

const express = require('express');
const fs = require('fs');
const path = require('path');
const { execSync } = require('child_process');

const app = express();
const PORT = process.env.PORT || 9000;
const WORKSPACE = path.join(__dirname);

app.use(express.json());
app.use(express.static(path.join(__dirname, 'public')));

// ============================================================================
// API: Learn from YouTube URL
// ============================================================================

app.post('/api/learn', (req, res) => {
  const { url } = req.body;
  
  if (!url) {
    return res.status(400).json({ error: 'URL required' });
  }

  try {
    console.log(`🎬 Learning from: ${url}`);
    
    // Run the zero-cost learner
    const cmd = `node "${WORKSPACE}/youtube-learner-zero-cost.js" "${url}"`;
    const output = execSync(cmd, { encoding: 'utf8', cwd: WORKSPACE });
    
    console.log(output);
    
    // Extract video ID
    const videoId = url.match(/(?:youtube\.com\/watch\?v=|youtu\.be\/)([a-zA-Z0-9_-]{11})/)?.[1];
    
    // Get the stored data
    const dataPath = path.join(WORKSPACE, `memory/youtube-learned/${videoId}.json`);
    const data = JSON.parse(fs.readFileSync(dataPath, 'utf8'));
    
    res.json({
      success: true,
      videoId,
      data,
      message: 'Learning complete (0 tokens)',
    });
  } catch (error) {
    console.error(error);
    res.status(500).json({ error: error.message });
  }
});

// ============================================================================
// API: Get Inbox Status
// ============================================================================

app.get('/api/inbox', (req, res) => {
  try {
    const inboxDir = path.join(WORKSPACE, 'memory/learning-inbox/inbox');
    
    if (!fs.existsSync(inboxDir)) {
      return res.json({ count: 0, entries: [] });
    }

    const files = fs.readdirSync(inboxDir).filter(f => f.endsWith('.json'));
    const entries = files.map(file => {
      const data = JSON.parse(fs.readFileSync(path.join(inboxDir, file), 'utf8'));
      return {
        filename: file,
        title: data.title,
        source: data.source,
        concepts: data.raw_concepts,
      };
    });

    res.json({ count: entries.length, entries });
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
});

// ============================================================================
// API: Get Staging Status
// ============================================================================

app.get('/api/staging', (req, res) => {
  try {
    const stagingDir = path.join(WORKSPACE, 'memory/learning-inbox/staging/approved');
    
    if (!fs.existsSync(stagingDir)) {
      return res.json({ count: 0, entries: [] });
    }

    const files = fs.readdirSync(stagingDir).filter(f => f.endsWith('.json'));
    const entries = files.map(file => {
      const data = JSON.parse(fs.readFileSync(path.join(stagingDir, file), 'utf8'));
      return {
        filename: file,
        title: data.title,
        concepts: data.raw_concepts,
      };
    });

    res.json({ count: entries.length, entries });
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
});

// ============================================================================
// API: Approve Entry
// ============================================================================

app.post('/api/approve', (req, res) => {
  const { filename, notes } = req.body;
  
  try {
    const cmd = `node "${WORKSPACE}/learning-inbox-manager.js" eval "${filename}" approved "${notes}"`;
    execSync(cmd, { encoding: 'utf8', cwd: WORKSPACE });
    
    res.json({ success: true, message: `Approved: ${filename}` });
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
});

// ============================================================================
// API: Reject Entry
// ============================================================================

app.post('/api/reject', (req, res) => {
  const { filename, notes } = req.body;
  
  try {
    const cmd = `node "${WORKSPACE}/learning-inbox-manager.js" eval "${filename}" rejected "${notes}"`;
    execSync(cmd, { encoding: 'utf8', cwd: WORKSPACE });
    
    res.json({ success: true, message: `Rejected: ${filename}` });
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
});

// ============================================================================
// API: Implement Approved
// ============================================================================

app.post('/api/implement', (req, res) => {
  try {
    const cmd = `node "${WORKSPACE}/learning-inbox-manager.js" implement`;
    const output = execSync(cmd, { encoding: 'utf8', cwd: WORKSPACE });
    
    res.json({ success: true, output });
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
});

// ============================================================================
// Serve HTML UI
// ============================================================================

const htmlUI = `
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>YouTube Learner</title>
  <style>
    * { margin: 0; padding: 0; box-sizing: border-box; }
    
    body {
      font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
      background: #0f172a;
      color: #e2e8f0;
      padding: 20px;
      line-height: 1.6;
    }
    
    .container {
      max-width: 1200px;
      margin: 0 auto;
    }
    
    h1 {
      color: #60a5fa;
      margin-bottom: 30px;
      display: flex;
      align-items: center;
      gap: 10px;
    }
    
    .grid {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 20px;
      margin-bottom: 30px;
    }
    
    @media (max-width: 768px) {
      .grid { grid-template-columns: 1fr; }
    }
    
    .panel {
      background: #1e293b;
      border: 1px solid #334155;
      border-radius: 8px;
      padding: 20px;
    }
    
    .panel h2 {
      color: #93c5fd;
      margin-bottom: 15px;
      font-size: 1.1rem;
    }
    
    input[type="text"] {
      width: 100%;
      padding: 10px;
      margin-bottom: 10px;
      background: #0f172a;
      border: 1px solid #475569;
      color: #e2e8f0;
      border-radius: 4px;
      font-family: monospace;
    }
    
    button {
      background: #3b82f6;
      color: white;
      border: none;
      padding: 10px 20px;
      border-radius: 4px;
      cursor: pointer;
      font-size: 0.9rem;
      transition: background 0.2s;
      width: 100%;
    }
    
    button:hover {
      background: #2563eb;
    }
    
    button:disabled {
      background: #64748b;
      cursor: not-allowed;
    }
    
    .entry {
      background: #0f172a;
      padding: 12px;
      margin: 8px 0;
      border-left: 3px solid #3b82f6;
      border-radius: 4px;
      font-size: 0.9rem;
    }
    
    .entry-title {
      font-weight: bold;
      color: #93c5fd;
      margin-bottom: 5px;
    }
    
    .entry-meta {
      color: #94a3b8;
      font-size: 0.85rem;
      margin-bottom: 8px;
    }
    
    .concepts {
      color: #a8e6cf;
      font-size: 0.85rem;
      word-break: break-word;
    }
    
    .entry-actions {
      display: flex;
      gap: 5px;
      margin-top: 8px;
    }
    
    .entry-actions button {
      flex: 1;
      padding: 6px 10px;
      font-size: 0.8rem;
      width: auto;
    }
    
    .entry-actions .approve {
      background: #10b981;
    }
    
    .entry-actions .approve:hover {
      background: #059669;
    }
    
    .entry-actions .reject {
      background: #ef4444;
    }
    
    .entry-actions .reject:hover {
      background: #dc2626;
    }
    
    .status {
      background: #064e3b;
      color: #86efac;
      padding: 10px;
      border-radius: 4px;
      margin-bottom: 15px;
      font-size: 0.9rem;
    }
    
    .status.error {
      background: #7f1d1d;
      color: #fca5a5;
    }
    
    .status.loading {
      background: #1e3a8a;
      color: #93c5fd;
    }
    
    .counter {
      display: inline-block;
      background: #3b82f6;
      color: white;
      padding: 4px 10px;
      border-radius: 12px;
      font-size: 0.8rem;
      margin-left: 10px;
    }
    
    .footer {
      color: #64748b;
      font-size: 0.85rem;
      margin-top: 30px;
      padding-top: 20px;
      border-top: 1px solid #334155;
      text-align: center;
    }
  </style>
</head>
<body>
  <div class="container">
    <h1>🎬 YouTube Learner <span style="font-size: 0.8rem; color: #475569;">(Zero Cost)</span></h1>
    
    <div class="grid">
      <!-- LEARN PANEL -->
      <div class="panel">
        <h2>📹 Learn from Video</h2>
        <input type="text" id="youtubeUrl" placeholder="Paste YouTube URL here...">
        <button id="learnBtn" onclick="learnVideo()">Learn Video</button>
        <div id="learnStatus"></div>
      </div>
      
      <!-- STATS PANEL -->
      <div class="panel">
        <h2>📊 Pipeline Status</h2>
        <div id="stats"></div>
        <button onclick="refreshStats()" style="margin-top: 10px;">Refresh</button>
      </div>
    </div>
    
    <div class="grid">
      <!-- INBOX PANEL -->
      <div class="panel">
        <h2>📥 Inbox (Unevaluated)<span class="counter" id="inboxCount">0</span></h2>
        <div id="inboxList"></div>
      </div>
      
      <!-- STAGING PANEL -->
      <div class="panel">
        <h2>✅ Staging (Approved)<span class="counter" id="stagingCount">0</span></h2>
        <div id="stagingList"></div>
        <button onclick="implementApproved()" style="margin-top: 15px; background: #10b981;">
          ↪️ Implement All Approved
        </button>
      </div>
    </div>
    
    <div class="footer">
      Running on port 9000 | Zero-cost local processing | Access from any device
    </div>
  </div>

  <script>
    async function learnVideo() {
      const url = document.getElementById('youtubeUrl').value;
      if (!url) return alert('Enter a YouTube URL');
      
      const btn = document.getElementById('learnBtn');
      const status = document.getElementById('learnStatus');
      
      btn.disabled = true;
      status.innerHTML = '<div class="status loading">🔄 Learning...</div>';
      
      try {
        const res = await fetch('/api/learn', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ url }),
        });
        
        const data = await res.json();
        
        if (data.success) {
          status.innerHTML = '<div class="status">✅ Learned! Concepts added to inbox.</div>';
          document.getElementById('youtubeUrl').value = '';
          setTimeout(refreshStats, 500);
        } else {
          status.innerHTML = '<div class="status error">❌ ' + (data.error || 'Failed') + '</div>';
        }
      } catch (e) {
        status.innerHTML = '<div class="status error">❌ Error: ' + e.message + '</div>';
      } finally {
        btn.disabled = false;
      }
    }
    
    async function refreshStats() {
      try {
        const inbox = await fetch('/api/inbox').then(r => r.json());
        const staging = await fetch('/api/staging').then(r => r.json());
        
        document.getElementById('inboxCount').textContent = inbox.count;
        document.getElementById('stagingCount').textContent = staging.count;
        
        document.getElementById('stats').innerHTML = \`
          <div class="entry">
            <div class="entry-title">Pipeline Status</div>
            <div class="entry-meta">
              📥 Inbox: \${inbox.count} entries<br>
              ✅ Staging: \${staging.count} approved<br>
              💾 Ready to implement
            </div>
          </div>
        \`;
        
        // Render inbox
        const inboxHTML = inbox.entries.map(e => \`
          <div class="entry">
            <div class="entry-title">\${e.title}</div>
            <div class="entry-meta">Source: \${e.source}</div>
            <div class="concepts">\${e.concepts.slice(0, 3).join(', ')}</div>
            <div class="entry-actions">
              <button class="approve" onclick="approveEntry('\${e.filename}')">✓ Approve</button>
              <button class="reject" onclick="rejectEntry('\${e.filename}')">✗ Reject</button>
            </div>
          </div>
        \`).join('');
        
        document.getElementById('inboxList').innerHTML = inboxHTML || '<div style="color: #64748b;">No new entries</div>';
        
        // Render staging
        const stagingHTML = staging.entries.map(e => \`
          <div class="entry">
            <div class="entry-title">\${e.title}</div>
            <div class="concepts">\${e.concepts.slice(0, 3).join(', ')}</div>
          </div>
        \`).join('');
        
        document.getElementById('stagingList').innerHTML = stagingHTML || '<div style="color: #64748b;">No approved entries</div>';
      } catch (e) {
        console.error('Stats error:', e);
      }
    }
    
    async function approveEntry(filename) {
      const notes = prompt('Notes (optional):');
      if (!fetch) return;
      
      await fetch('/api/approve', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ filename, notes: notes || 'No notes' }),
      });
      
      refreshStats();
    }
    
    async function rejectEntry(filename) {
      const notes = prompt('Reason (optional):');
      if (!fetch) return;
      
      await fetch('/api/reject', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ filename, notes: notes || 'No reason' }),
      });
      
      refreshStats();
    }
    
    async function implementApproved() {
      if (!confirm('Implement all approved entries into MEMORY.md?')) return;
      
      await fetch('/api/implement', { method: 'POST' });
      alert('✅ Implemented! Check MEMORY.md');
      refreshStats();
    }
    
    // Load on start
    refreshStats();
  </script>
</body>
</html>
`;

app.get('/', (req, res) => {
  res.send(htmlUI);
});

// ============================================================================
// START SERVER
// ============================================================================

app.listen(PORT, () => {
  console.log(`
╔════════════════════════════════════════╗
║   🎬 YOUTUBE LEARNER WEB UI            ║
║   Zero-Cost Local Processing           ║
╚════════════════════════════════════════╝

🌐 Access from any device:
   http://localhost:${PORT}
   
For Windows:
   Use http://<your-vps-ip>:${PORT}

Features:
   📹 Learn from YouTube videos
   📥 Inbox pipeline (review before using)
   ✅ Approve/reject entries
   💰 Zero token cost
   
Press Ctrl+C to stop
`);
});
