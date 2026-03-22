#!/usr/bin/env python3
"""
VOICE CONTINUOUS - Always listening. Open mic for natural conversation.
Press STOP to close. Otherwise loops continuously.
"""

import tkinter as tk
from tkinter import scrolledtext
import threading
import pyttsx3
import json
import subprocess
import time

class VoiceContinuous:
    def __init__(self, root):
        self.root = root
        self.root.title("Voice Claw - Open Mic")
        self.root.geometry("1000x800")
        self.root.configure(bg="#1a1a1a")
        
        self.tts_engine = pyttsx3.init()
        self.tts_engine.setProperty('rate', 150)
        
        # Load knowledge
        self.conversations = self.load_json('conversations.json', 'conversations')
        self.learned = self.load_json('learned_knowledge.json', None)
        self.concepts = self.learned.get('key_concepts', []) if self.learned else []
        self.patterns = self.learned.get('response_patterns', []) if self.learned else []
        self.vocab = self.learned.get('vocabulary', []) if self.learned else []
        
        self.listening = False
        self.conversation_history = []
        
        self.setup_ui()
        
    def load_json(self, filename, key):
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
                return data.get(key, []) if key else data
        except:
            return [] if key else {}
    
    def find_response(self, user_input):
        """Generate response using learned knowledge"""
        user_lower = user_input.lower()
        
        # Check conversations first
        for conv in self.conversations:
            for keyword in conv.get('keywords', []):
                if keyword.lower() in user_lower:
                    return conv['response']
        
        # Check learned concepts
        for concept in self.concepts:
            concept_words = concept['concept'].lower()
            if any(word in concept_words for word in user_lower.split()):
                return f"From my learning: {concept['concept']}"
        
        # Check patterns
        for pattern in self.patterns:
            pattern_words = pattern['topic'].lower()
            if any(word in pattern_words for word in user_lower.split()):
                return f"About {pattern['topic']}: {pattern['summary']}"
        
        # Check vocab
        user_words = set(user_lower.split())
        vocab_matches = user_words.intersection(set(self.vocab))
        
        if vocab_matches:
            matches_str = ', '.join(list(vocab_matches)[:2])
            return f"I understand: {matches_str}. Tell me more."
        
        return f"I heard '{user_input}'. Keep talking."
    
    def setup_ui(self):
        header = tk.Frame(self.root, bg="#2d2d2d")
        header.pack(fill=tk.X)
        
        title = tk.Label(
            header, text="VOICE CLAW - Open Mic (Always Listening)",
            font=("Arial", 16, "bold"), bg="#2d2d2d", fg="#00ff00", pady=15
        )
        title.pack()
        
        self.status_var = tk.StringVar(value="Waiting to start...")
        status = tk.Label(
            self.root, textvariable=self.status_var,
            font=("Arial", 11), bg="#1a1a1a", fg="#ffff00", anchor=tk.W
        )
        status.pack(pady=8, fill=tk.X, padx=15)
        
        content = tk.Frame(self.root, bg="#1a1a1a")
        content.pack(fill=tk.BOTH, expand=True, padx=20, pady=15)
        
        # Conversation display
        conv_label = tk.Label(
            content, text="CONVERSATION:", font=("Arial", 11, "bold"),
            bg="#1a1a1a", fg="#00ff00"
        )
        conv_label.pack(anchor=tk.W, pady=(0, 5))
        
        self.conversation_text = scrolledtext.ScrolledText(
            content, height=15, wrap=tk.WORD,
            bg="#2d2d2d", fg="#00ff00", font=("Courier", 10),
            state=tk.DISABLED
        )
        self.conversation_text.pack(fill=tk.BOTH, expand=True, padx=0, pady=(0, 15))
        
        # Buttons
        button_frame = tk.Frame(content, bg="#1a1a1a")
        button_frame.pack(fill=tk.X, pady=10)
        
        self.start_btn = tk.Button(
            button_frame, text="START LISTENING",
            command=self.start_listening,
            bg="#00ff00", fg="#000000", font=("Arial", 12, "bold"),
            width=20, height=2
        )
        self.start_btn.pack(side=tk.LEFT, padx=5)
        
        self.stop_btn = tk.Button(
            button_frame, text="STOP",
            command=self.stop_listening,
            bg="#ff0000", fg="#000000", font=("Arial", 12, "bold"),
            width=20, height=2, state=tk.DISABLED
        )
        self.stop_btn.pack(side=tk.LEFT, padx=5)
        
        clear_btn = tk.Button(
            button_frame, text="CLEAR",
            command=self.clear_conversation,
            bg="#ff6600", fg="#000000", font=("Arial", 12, "bold"),
            width=20, height=2
        )
        clear_btn.pack(side=tk.LEFT, padx=5)
        
    def add_to_conversation(self, speaker, text):
        """Add line to conversation display"""
        self.conversation_text.config(state=tk.NORMAL)
        timestamp = time.strftime("%H:%M:%S")
        self.conversation_text.insert(tk.END, f"[{timestamp}] {speaker}: {text}\n")
        self.conversation_text.see(tk.END)
        self.conversation_text.config(state=tk.DISABLED)
        self.root.update()
    
    def start_listening(self):
        """Start continuous listening"""
        self.listening = True
        self.start_btn.config(state=tk.DISABLED, bg="#999999")
        self.stop_btn.config(state=tk.NORMAL, bg="#ff0000")
        self.status_var.set("Listening... Speak now")
        self.add_to_conversation("SYSTEM", "Open mic started. Listening...")
        threading.Thread(target=self.listening_loop, daemon=True).start()
    
    def listening_loop(self):
        """Continuous listening loop"""
        while self.listening:
            try:
                ps_script = """
Add-Type -AssemblyName System.Speech
$recognize = New-Object System.Speech.Recognition.SpeechRecognitionEngine
$grammar = New-Object System.Speech.Recognition.DictationGrammar
$recognize.LoadGrammar($grammar)
try {
    $result = $recognize.Recognize()
    if ($result) { Write-Host $result.Text }
} catch {
    Write-Host "[timeout]"
}
"""
                
                result = subprocess.run(
                    ["powershell", "-Command", ps_script],
                    capture_output=True,
                    text=True,
                    timeout=15
                )
                
                text = result.stdout.strip()
                
                if text and "[timeout]" not in text and text != "":
                    # Add user input
                    self.add_to_conversation("YOU", text)
                    self.status_var.set(f"Heard: {text}")
                    
                    # Generate response
                    response = self.find_response(text)
                    self.add_to_conversation("CLAW", response)
                    
                    # Speak response
                    self.tts_engine.say(response)
                    self.tts_engine.runAndWait()
                    
                    self.status_var.set("Listening... Speak again")
                else:
                    self.status_var.set("Listening... (no speech detected)")
                
                time.sleep(0.5)  # Brief pause before next listen
                
            except Exception as e:
                self.add_to_conversation("SYSTEM", f"Error: {str(e)[:60]}")
                if not self.listening:
                    break
    
    def stop_listening(self):
        """Stop continuous listening"""
        self.listening = False
        self.start_btn.config(state=tk.NORMAL, bg="#00ff00")
        self.stop_btn.config(state=tk.DISABLED, bg="#999999")
        self.status_var.set("Stopped.")
        self.add_to_conversation("SYSTEM", "Microphone closed.")
    
    def clear_conversation(self):
        """Clear conversation history"""
        self.conversation_text.config(state=tk.NORMAL)
        self.conversation_text.delete(1.0, tk.END)
        self.conversation_text.config(state=tk.DISABLED)
        self.conversation_history = []
        self.status_var.set("Cleared.")

if __name__ == "__main__":
    root = tk.Tk()
    app = VoiceContinuous(root)
    root.mainloop()
