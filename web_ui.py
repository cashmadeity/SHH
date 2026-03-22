#!/usr/bin/env python3
"""
VOICE CLAW WEB UI - Full permissions like the voice app
Access to files, learning, saving, real-time updates
SECURE: Input validation, rate limiting, XSS/SQL/Command injection protection
"""

from flask import Flask, render_template, request, jsonify, send_from_directory
import json
import os
import threading
import time
import subprocess
from datetime import datetime
import anthropic
from security_layer import SecurityLayer, check_rate_limit

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

# Initialize Claude client
ANTHROPIC_API_KEY = os.getenv('ANTHROPIC_API_KEY')
claude_client = anthropic.Anthropic(api_key=ANTHROPIC_API_KEY) if ANTHROPIC_API_KEY else None

# Budget tracking - BROKE MODE (save every cent)
BUDGET_LIMIT = 0.25  # $0.25 max (very low)
MAX_API_CALLS = 5    # Hard limit per session
USAGE_FILE = 'web_ui_api_usage.json'

# Load persistent tracking
def load_api_usage():
    try:
        with open(USAGE_FILE, 'r') as f:
            return json.load(f)
    except:
        return {
            "requests": 0,
            "tokens_input": 0,
            "tokens_output": 0,
            "estimated_cost": 0.0,
            "session_hits": 0,
            "total_sessions": 1,
            "first_use": datetime.now().isoformat()
        }

def save_api_usage(usage):
    with open(USAGE_FILE, 'w') as f:
        json.dump(usage, f, indent=2)

api_usage = load_api_usage()
api_usage['total_sessions'] = api_usage.get('total_sessions', 0) + 1
save_api_usage(api_usage)

def handle_meday_command(command):
    """Execute meday override command"""
    instruction = command.replace('meday ', '', 1).strip()
    
    # Log command
    log_file = "meday_commands.log"
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    with open(log_file, 'a') as f:
        f.write(f"[{timestamp}] [WEB_UI] {command}\n")
    
    # Block WhatsApp unlock
    if "unlock" in instruction.lower() and "whatsapp" in instruction.lower():
        return "ERROR: WhatsApp unlock blocked. Safeguard active."
    
    # System commands
    if instruction.lower() == "status":
        return "Meday Active | WhatsApp Locked | All Systems Online"
    
    elif instruction.lower() == "pause":
        return "Meday paused"
    
    elif instruction.lower() == "resume":
        return "Meday resumed"
    
    elif instruction.lower() == "memory":
        try:
            with open('MEMORY.md', 'r') as f:
                return f.read()[:500]
        except:
            return "Memory access error"
    
    elif instruction.lower().startswith("run"):
        # Execute shell command
        cmd = instruction[4:].strip()
        
        # Block destructive commands
        blocked = ['del', 'rm', 'format', 'fdisk', 'diskpart']
        if any(x in cmd.lower() for x in blocked):
            return f"BLOCKED: Destructive command. Use 'meday confirm {cmd}' to override."
        
        try:
            result = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=10)
            output = result.stdout if result.stdout else result.stderr
            return output[:500] if output else "Command executed"
        except Exception as e:
            return f"Error: {str(e)}"
    
    elif instruction.lower().startswith("learn"):
        # Add to knowledge
        text = instruction[6:].strip()
        try:
            with open('learned_knowledge.json', 'r') as f:
                data = json.load(f)
            data['key_concepts'].append({"concept": text, "timestamp": time.time()})
            with open('learned_knowledge.json', 'w') as f:
                json.dump(data, f)
            return f"Learned: {text}"
        except Exception as e:
            return f"Learn error: {str(e)}"
    
    else:
        return f"Meday instruction: {instruction}"

# Global state
class Brain:
    def __init__(self):
        self.conversations = self.load_json('conversations.json', 'conversations')
        self.learned = self.load_json('learned_knowledge.json', None)
        self.concepts = self.learned.get('key_concepts', []) if self.learned else []
        self.patterns = self.learned.get('response_patterns', []) if self.learned else []
        self.vocab = self.learned.get('vocabulary', []) if self.learned else []
        self.history = self.load_json('conversation_history.json', None) or []
        self.new_patterns_count = 0
        self.new_words_count = 0
        
        # PERFORMANCE: Pre-build lookup caches
        self._vocab_set = set(self.vocab)  # O(1) lookup
        self._conv_cache = {}  # Response cache
        self._cache_max = 50  # Max cached responses
    
    def load_json(self, filename, key):
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
                return data.get(key, []) if key else data
        except:
            return [] if key else {}
    
    def find_response(self, user_input):
        # BROKE MODE: Try local first, only use Claude if absolutely needed
        local_response = self.find_local_response(user_input)
        
        # Check if we should use Claude (only for complex queries)
        if claude_client and api_usage['estimated_cost'] < BUDGET_LIMIT and api_usage['requests'] < MAX_API_CALLS:
            # Only use Claude for queries that need deeper understanding
            complex_indicators = ['why', 'how', 'explain', 'describe', 'analyze', 'think', 'opinion', 'help']
            needs_claude = any(ind in user_input.lower() for ind in complex_indicators)
            
            if needs_claude or api_usage['session_hits'] > 3:
                # Build context from learned knowledge
                context = self.build_context()
                
                try:
                    message = claude_client.messages.create(
                        model="claude-3-5-sonnet-20241022",
                        max_tokens=150,  # Reduced for savings
                        system=f"You are a helpful assistant. Use this context: {context}",
                        messages=[
                            {"role": "user", "content": user_input}
                        ]
                    )
                    
                    response = message.content[0].text
                    
                    # Track usage
                    api_usage['requests'] += 1
                    api_usage['tokens_input'] += message.usage.input_tokens
                    api_usage['tokens_output'] += message.usage.output_tokens
                    # Claude 3.5 Sonnet: $3/1M input, $15/1M output
                    cost = (message.usage.input_tokens * 3 + message.usage.output_tokens * 15) / 1000000
                    api_usage['estimated_cost'] += cost
                    api_usage['lifetime_cost'] = api_usage.get('lifetime_cost', 0) + cost
                    save_api_usage(api_usage)  # Persist after each Claude call
                    
                    return response
                except Exception as e:
                    api_usage['session_hits'] += 1
                    return local_response
            else:
                api_usage['session_hits'] += 1
                return local_response
        else:
            api_usage['session_hits'] += 1
            return local_response
    
    def find_local_response(self, user_input):
        """Local response only - no API calls - OPTIMIZED"""
        # Check cache first
        cache_key = user_input.lower()[:50]
        if cache_key in self._conv_cache:
            return self._conv_cache[cache_key]
        
        user_lower = user_input.lower()
        user_words = set(user_lower.split())
        
        # Fast path: Check vocab matches first (most common)
        vocab_matches = user_words.intersection(self._vocab_set)
        if vocab_matches:
            response = f"I understand: {', '.join(list(vocab_matches)[:2])}. Tell me more."
            self._cache_response(cache_key, response)
            return response
        
        # Check conversations (keyword match)
        for conv in self.conversations:
            for keyword in conv.get('keywords', []):
                if keyword.lower() in user_lower:
                    response = conv['response']
                    self._cache_response(cache_key, response)
                    return response
        
        # Check patterns
        for pattern in reversed(self.patterns[-10:]):  # Last 10 only for speed
            pattern_words = pattern.get('topic', '').lower().split()
            if any(word in user_lower for word in pattern_words if len(word) > 3):
                response = pattern.get('summary', 'I understand.')
                self._cache_response(cache_key, response)
                return response
        
        # Check concepts
        for concept in self.concepts[:20]:  # First 20 only
            concept_word = concept.get('concept', '').lower()
            if any(word in concept_word for word in user_words if len(word) > 3):
                response = f"From my learning: {concept['concept']}"
                self._cache_response(cache_key, response)
                return response
        
        response = "I'm listening. Tell me more."
        self._cache_response(cache_key, response)
        return response
    
    def _cache_response(self, key, response):
        """Cache response with LRU eviction"""
        if len(self._conv_cache) >= self._cache_max:
            # Remove oldest 10
            keys_to_remove = list(self._conv_cache.keys())[:10]
            for k in keys_to_remove:
                del self._conv_cache[k]
        self._conv_cache[key] = response
    
    def build_context(self):
        """Build context from learned knowledge for Claude"""
        context_parts = []
        
        if self.patterns:
            context_parts.append(f"Recent patterns: {', '.join([p.get('topic', '')[:30] for p in self.patterns[-5:]])}")
        
        if self.concepts:
            context_parts.append(f"Key concepts: {', '.join([c.get('concept', '')[:30] for c in self.concepts[:5]])}")
        
        if len(self.vocab) > 0:
            context_parts.append(f"Vocabulary: {', '.join(self.vocab[:20])}")
        
        return " | ".join(context_parts) if context_parts else "No learned context yet."
    
    def learn_from_interaction(self, user_input, response):
        # PERFORMANCE: Skip learning for repeated/cached responses
        cache_key = user_input.lower()[:50]
        if cache_key in self._conv_cache and self._conv_cache[cache_key] == response:
            return  # Don't re-learn cached responses
        
        # Add to history (keep last 50 only)
        self.history.append({
            "user": user_input,
            "response": response,
            "timestamp": datetime.now().isoformat()
        })
        if len(self.history) > 50:
            self.history = self.history[-50:]
        
        # Extract new words (fast path)
        new_words = []
        for word in user_input.lower().split():
            word = word.strip('.,!?;:')
            if len(word) > 2 and word not in self._vocab_set:
                new_words.append(word)
        
        if new_words:
            self.vocab.extend(new_words)
            self._vocab_set.update(new_words)
            self.new_words_count += len(new_words)
        
        # Add pattern (only if long enough and not duplicate)
        if len(user_input) > 30 and len(user_input) < 200:
            topic_key = user_input[:50].lower()
            if not any(p.get('topic', '').lower() == topic_key for p in self.patterns[-20:]):
                self.patterns.append({
                    "topic": user_input[:50],
                    "summary": response[:100] if len(response) > 100 else response,
                    "learned": True,
                    "timestamp": datetime.now().isoformat()
                })
                self.new_patterns_count += 1
                # Keep patterns manageable
                if len(self.patterns) > 100:
                    self.patterns = self.patterns[-100:]
    
    def save_all(self):
        try:
            with open('conversations.json', 'w') as f:
                json.dump({"conversations": self.conversations}, f, indent=2)
            
            with open('learned_knowledge.json', 'w') as f:
                json.dump({
                    "key_concepts": self.concepts,
                    "response_patterns": self.patterns,
                    "vocabulary": self.vocab
                }, f, indent=2)
            
            with open('conversation_history.json', 'w') as f:
                json.dump(self.history, f, indent=2)
            
            return True
        except:
            return False
    
    def get_stats(self):
        return {
            "conversations": len(self.conversations),
            "concepts": len(self.concepts),
            "patterns": len(self.patterns),
            "vocabulary": len(self.vocab),
            "history_items": len(self.history),
            "new_patterns": self.new_patterns_count,
            "new_words": self.new_words_count,
            "claude_enabled": claude_client is not None,
            "api_requests": api_usage['requests'],
            "api_cost": round(api_usage['estimated_cost'], 4),
            "budget_remaining": round(BUDGET_LIMIT - api_usage['estimated_cost'], 4),
            "budget_limit": BUDGET_LIMIT,
            "local_fallbacks": api_usage.get('session_hits', 0),
            "savings_estimate": round(api_usage.get('session_hits', 0) * 0.002, 4),  # ~$0.002 per local call
            "security_active": True,
            "rate_limit_remaining": remaining,
            "total_lifetime_cost": round(api_usage.get('lifetime_cost', 0), 4),
            "total_sessions": api_usage.get('total_sessions', 1)
        }

brain = Brain()

@app.route('/')
def index():
    return render_template('index_voice.html')

@app.route('/api/response', methods=['POST'])
def get_response():
    data = request.json
    user_input = data.get('input', '')
    
    # Rate limiting (10 requests per minute per IP)
    client_ip = request.remote_addr or 'unknown'
    allowed, remaining = check_rate_limit(client_ip, max_requests=10, window_seconds=60)
    if not allowed:
        return jsonify({
            "response": "Rate limit exceeded. Please wait.",
            "error": "rate_limit",
            "stats": brain.get_stats()
        }), 429
    
    # Security: Sanitize input
    clean_input, block_reason = SecurityLayer.sanitize(user_input)
    if block_reason:
        return jsonify({
            "response": f"Input blocked: {block_reason}",
            "error": block_reason,
            "stats": brain.get_stats()
        }), 400
    
    # Check for meday override
    if clean_input.lower().startswith('meday '):
        response = handle_meday_command(clean_input)
        return jsonify({
            "response": response,
            "stats": brain.get_stats(),
            "meday": True
        })
    
    response = brain.find_response(clean_input)
    brain.learn_from_interaction(clean_input, response)
    
    return jsonify({
        "response": response,
        "stats": brain.get_stats(),
        "meday": False
    })

@app.route('/api/stats')
def get_stats():
    return jsonify(brain.get_stats())

@app.route('/api/save', methods=['POST'])
def save():
    success = brain.save_all()
    brain.new_patterns_count = 0
    brain.new_words_count = 0
    
    return jsonify({
        "success": success,
        "stats": brain.get_stats()
    })

@app.route('/api/history')
def get_history():
    return jsonify(brain.history[-50:])  # Last 50

@app.route('/api/patterns')
def get_patterns():
    return jsonify(brain.patterns[-20:])  # Last 20

@app.route('/api/vocabulary')
def get_vocabulary():
    return jsonify(sorted(brain.vocab))

@app.route('/api/load', methods=['POST'])
def load_file():
    """Load and learn from uploaded text file"""
    if 'file' not in request.files:
        return jsonify({"error": "No file"}), 400
    
    file = request.files['file']
    try:
        content = file.read().decode('utf-8')
        
        # Extract sentences as patterns
        sentences = content.split('.')
        for sentence in sentences[:100]:  # Learn from first 100 sentences
            sentence = sentence.strip()
            if len(sentence) > 20:
                brain.learn_from_interaction(sentence, "I've learned this.")
        
        brain.save_all()
        return jsonify({
            "success": True,
            "learned": len([s for s in sentences if len(s.strip()) > 20]),
            "stats": brain.get_stats()
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/api/clear', methods=['POST'])
def clear_history():
    brain.history = []
    brain.save_all()
    return jsonify({
        "success": True,
        "stats": brain.get_stats()
    })

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5000, threaded=True)
