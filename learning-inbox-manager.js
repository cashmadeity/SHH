#!/usr/bin/env node

/**
 * LEARNING INBOX MANAGER
 * 
 * Manages raw learning → evaluation → implementation pipeline
 * Usage: node learning-inbox-manager.js <action>
 */

const fs = require('fs');
const path = require('path');

const INBOX_DIR = path.join(__dirname, 'memory/learning-inbox');
const RAW_DIR = path.join(INBOX_DIR, 'inbox');
const STAGING_DIR = path.join(INBOX_DIR, 'staging');
const IMPL_DIR = path.join(INBOX_DIR, 'implemented');
const LOG_FILE = path.join(INBOX_DIR, 'evaluation-log.json');

// Ensure directories exist
[RAW_DIR, STAGING_DIR, IMPL_DIR].forEach(dir => {
  if (!fs.existsSync(dir)) fs.mkdirSync(dir, { recursive: true });
});

// ============================================================================
// MOVE FROM YOUTUBE LEARNER TO INBOX
// ============================================================================

function captureFromYoutube() {
  console.log('📥 Capturing learned videos into inbox...');
  
  const learnedDir = path.join(__dirname, 'memory/youtube-learned');
  if (!fs.existsSync(learnedDir)) {
    console.log('  (no learned videos yet)');
    return;
  }

  const files = fs.readdirSync(learnedDir).filter(f => f.endsWith('.json'));
  let captured = 0;

  files.forEach(file => {
    const srcPath = path.join(learnedDir, file);
    const data = JSON.parse(fs.readFileSync(srcPath, 'utf8'));
    
    const inboxEntry = {
      id: `video-${data.videoId}`,
      source: 'youtube',
      title: data.summary,
      raw_concepts: data.key_concepts,
      takeaways: data.main_takeaways,
      vocabulary: data.vocabulary,
      timestamp: data.timestamp,
      status: 'inbox',
      confidence: 0.8,
      relevance_to_user: 'unrated',
      ready_to_use: false,
      eval_notes: 'Waiting for evaluation',
    };

    const inboxPath = path.join(RAW_DIR, `video-${data.videoId}.json`);
    if (!fs.existsSync(inboxPath)) {
      fs.writeFileSync(inboxPath, JSON.stringify(inboxEntry, null, 2));
      captured++;
    }
  });

  console.log(`  ✅ Captured ${captured} new entries`);
}

// ============================================================================
// LIST INBOX (unevaluated)
// ============================================================================

function listInbox() {
  console.log('\n📋 INBOX (Unevaluated)');
  
  if (!fs.existsSync(RAW_DIR)) return;
  
  const files = fs.readdirSync(RAW_DIR).filter(f => f.endsWith('.json'));
  
  if (files.length === 0) {
    console.log('  (empty)');
    return;
  }

  files.forEach((file, i) => {
    const data = JSON.parse(fs.readFileSync(path.join(RAW_DIR, file), 'utf8'));
    console.log(`\n  ${i + 1}. ${data.title}`);
    console.log(`     Source: ${data.source} | Confidence: ${data.confidence}`);
    console.log(`     Concepts: ${data.raw_concepts.slice(0, 3).join(', ')}`);
    console.log(`     File: ${file}`);
  });
}

// ============================================================================
// EVALUATE AN ENTRY
// ============================================================================

function evaluateEntry(filename, decision, notes) {
  console.log(`\n🔍 Evaluating ${filename}...`);
  
  const srcPath = path.join(RAW_DIR, filename);
  if (!fs.existsSync(srcPath)) {
    console.error(`  ❌ Not found: ${filename}`);
    return false;
  }

  const entry = JSON.parse(fs.readFileSync(srcPath, 'utf8'));
  entry.status = decision; // 'approved' or 'rejected'
  entry.eval_notes = notes;
  entry.evaluated_at = new Date().toISOString();

  // Move to staging
  const destDir = decision === 'approved' ? 
    path.join(STAGING_DIR, 'approved') : 
    path.join(STAGING_DIR, 'rejected');
  
  if (!fs.existsSync(destDir)) fs.mkdirSync(destDir, { recursive: true });
  
  const destPath = path.join(destDir, filename);
  fs.writeFileSync(destPath, JSON.stringify(entry, null, 2));
  fs.unlinkSync(srcPath);

  // Log decision
  logDecision(entry.id, decision, notes);

  console.log(`  ✅ ${decision.toUpperCase()}`);
  return true;
}

// ============================================================================
// LOG EVALUATION DECISION
// ============================================================================

function logDecision(entryId, decision, notes) {
  let log = {};
  if (fs.existsSync(LOG_FILE)) {
    log = JSON.parse(fs.readFileSync(LOG_FILE, 'utf8'));
  }

  log[entryId] = {
    decision,
    notes,
    timestamp: new Date().toISOString(),
  };

  fs.writeFileSync(LOG_FILE, JSON.stringify(log, null, 2));
}

// ============================================================================
// LIST STAGING (approved, ready)
// ============================================================================

function listStaging() {
  console.log('\n✅ STAGING (Approved, Ready to Implement)');
  
  const approvedDir = path.join(STAGING_DIR, 'approved');
  if (!fs.existsSync(approvedDir)) {
    console.log('  (empty)');
    return;
  }

  const files = fs.readdirSync(approvedDir).filter(f => f.endsWith('.json'));
  
  if (files.length === 0) {
    console.log('  (empty)');
    return;
  }

  files.forEach((file, i) => {
    const data = JSON.parse(fs.readFileSync(path.join(approvedDir, file), 'utf8'));
    console.log(`\n  ${i + 1}. ${data.title}`);
    console.log(`     Concepts: ${data.raw_concepts.slice(0, 3).join(', ')}`);
  });
}

// ============================================================================
// IMPLEMENT (move approved to MEMORY.md)
// ============================================================================

function implementApproved() {
  console.log('\n🚀 Implementing approved entries into MEMORY.md...');
  
  const approvedDir = path.join(STAGING_DIR, 'approved');
  if (!fs.existsSync(approvedDir)) {
    console.log('  (no approved entries)');
    return;
  }

  const files = fs.readdirSync(approvedDir).filter(f => f.endsWith('.json'));
  let implemented = 0;

  files.forEach(file => {
    const srcPath = path.join(approvedDir, file);
    const entry = JSON.parse(fs.readFileSync(srcPath, 'utf8'));

    // Log to MEMORY.md (simplified)
    const memoryEntry = `
### Learned: ${entry.title}
- **Source:** ${entry.source}
- **Key Concepts:** ${entry.raw_concepts.join(', ')}
- **Takeaways:** ${entry.takeaways.join('; ')}
- **Captured:** ${entry.timestamp}
`;

    // Append to MEMORY.md under "Learning"
    const memPath = path.join(__dirname, 'MEMORY.md');
    const mem = fs.readFileSync(memPath, 'utf8');
    if (!mem.includes(entry.id)) {
      fs.appendFileSync(memPath, `\n${memoryEntry}`);
      
      // Move to implemented
      const implPath = path.join(IMPL_DIR, file);
      fs.writeFileSync(implPath, JSON.stringify(entry, null, 2));
      fs.unlinkSync(srcPath);
      
      implemented++;
    }
  });

  console.log(`  ✅ Implemented ${implemented} entries into MEMORY.md`);
}

// ============================================================================
// MAIN
// ============================================================================

function main() {
  const action = process.argv[2];

  switch (action) {
    case 'capture':
      captureFromYoutube();
      break;
    case 'inbox':
      listInbox();
      break;
    case 'staging':
      listStaging();
      break;
    case 'eval':
      const filename = process.argv[3];
      const decision = process.argv[4]; // 'approved' or 'rejected'
      const notes = process.argv[5] || 'No notes';
      evaluateEntry(filename, decision, notes);
      break;
    case 'implement':
      implementApproved();
      break;
    case 'status':
      captureFromYoutube();
      console.log('');
      listInbox();
      console.log('');
      listStaging();
      break;
    default:
      console.log(`
Learning Inbox Manager

Actions:
  capture    - Import YouTube learned videos into inbox
  inbox      - List unevaluated entries
  staging    - List approved entries ready to implement
  eval <f> <decision> <notes> - Evaluate an entry (approved/rejected)
  implement  - Move approved entries to MEMORY.md
  status     - Show full pipeline status

Example:
  node learning-inbox-manager.js capture
  node learning-inbox-manager.js inbox
  node learning-inbox-manager.js eval video-abc123.json approved "Useful for ML concepts"
  node learning-inbox-manager.js implement
      `);
  }
}

main();
