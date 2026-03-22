#!/usr/bin/env python3
"""
VOICE SMART - Uses base.txt as vocabulary/context for better speech recognition
Trains speech recognizer with domain knowledge
"""

import tkinter as tk
from tkinter import scrolledtext
import threading
import pyttsx3
import json
import subprocess
import os

class VoiceSmart:
    def __init__(self, root):
        self.root = root
        self.root.title("Voice Claw - Smart Recognition")
        self.root.geometry("950x700")
        self.root.configure(bg="#1a1a1a")
        
        self.tts_engine = pyttsx3.init()
        self.tts_engine.setProperty('rate', 150)
        
        # Load conversation database + base.txt vocabulary
        self.conversations = self.load_conversations()
        self.vocabulary = self.load_vocabulary()
        
        self.setup_ui()
        
    def load_conversations(self):
        """Load conversations.json"""
        try:
            with open('conversations.json', 'r') as f:
                data = json.load(f)
                return data.get('conversations', [])
        except:
            return []
    
    def load_vocabulary(self):
        """Load base.txt for context/vocabulary"""
        try:
            with open('base.txt', 'r') as f:
                content = f.read()
                # Extract unique words
                words = set()
                for line in content.split('\n'):
                    for word in line.split():
                        words.add(word.lower().strip('.,;:!?'))
                return list(words)
        except:
            return []
    
    def find_response(self, user_input):
        """Match user input - prefer conversations.json, fallback to general"""
        user_lower = user_input.lower()
        
        # Check conversations database
        for conv in self.conversations:
            for keyword in conv.get('keywords', []):
                if keyword.lower() in user_lower:
                    return conv['response']
        
        # Check if question relates to content in base.txt
        words_in_input = set(user_lower.split())
        matching_words = words_in_input.intersection(set(self.vocabulary))
        
        if matching_words:
            return f"You asked about: {', '.join(list(matching_words)[:3])}. From what I understand, this relates to the knowledge base. Can you ask more specifically?"
        
        # Generic fallback
        return f"I heard: '{user_input}'. Try asking about voice, AI, systems, or say 'help'."
    
    def setup_ui(self):
        header = tk.Frame(self.root, bg="#2d2d2d")
        header.pack(fill=tk.X)
        
        title = tk.Label(
            header, text="VOICE CLAW - Smart Recognition (base.txt + conversations.json)",
            font=("Arial", 14, "bold"), bg="#2d2d2d", fg="#00ff00", pady=15
        )
        title.pack()
        
        self.status_var = tk.StringVar(value="Ready. Press RECORD or Ctrl+Space")
        status = tk.Label(
            self.root, textvariable=self.status_var,
            font=("Arial", 10), bg="#1a1a1a", fg="#ffff00", anchor=tk.W
        )
        status.pack(pady=8, fill=tk.X, padx=15)
        
        info = tk.Label(
            self.root, text=f"Loaded: {len(self.conversations)} conversations | {len(self.vocabulary)} vocabulary words",
            font=("Arial", 9), bg="#1a1a1a", fg="#aaaaaa", anchor=tk.W
        )
        info.pack(pady=2, fill=tk.X, padx=15)
        
        content = tk.Frame(self.root, bg="#1a1a1a")
        content.pack(fill=tk.BOTH, expand=True, padx=20, pady=15)
        
        voice_label = tk.Label(
            content, text="YOUR VOICE:", font=("Arial", 11, "bold"),
            bg="#1a1a1a", fg="#00ff00"
        )
        voice_label.pack(anchor=tk.W, pady=(0, 5))
        
        self.voice_text = scrolledtext.ScrolledText(
            content, height=3, wrap=tk.WORD,
            bg="#2d2d2d", fg="#ffffff", font=("Courier", 11)
        )
        self.voice_text.pack(fill=tk.X, padx=0, pady=(0, 15))
        
        response_label = tk.Label(
            content, text="CLAW RESPONSE:", font=("Arial", 11, "bold"),
            bg="#1a1a1a", fg="#00ff00"
        )
        response_label.pack(anchor=tk.W, pady=(0, 5))
        
        self.response_text = scrolledtext.ScrolledText(
            content, height=10, wrap=tk.WORD,
            bg="#2d2d2d", fg="#00ff00", font=("Courier", 11)
        )
        self.response_text.pack(fill=tk.BOTH, expand=True, padx=0, pady=(0, 15))
        
        button_frame = tk.Frame(content, bg="#1a1a1a")
        button_frame.pack(fill=tk.X, pady=10)
        
        self.record_btn = tk.Button(
            button_frame, text="RECORD (Ctrl+Space)",
            command=self.start_recording,
            bg="#00ff00", fg="#000000", font=("Arial", 11, "bold"),
            width=18, height=2
        )
        self.record_btn.pack(side=tk.LEFT, padx=5)
        
        self.speak_btn = tk.Button(
            button_frame, text="SPEAK",
            command=self.speak_response,
            bg="#00ccff", fg="#000000", font=("Arial", 11, "bold"),
            width=18, height=2, state=tk.DISABLED
        )
        self.speak_btn.pack(side=tk.LEFT, padx=5)
        
        clear_btn = tk.Button(
            button_frame, text="CLEAR",
            command=self.clear_all,
            bg="#ff6600", fg="#000000", font=("Arial", 11, "bold"),
            width=18, height=2
        )
        clear_btn.pack(side=tk.LEFT, padx=5)
        
        self.root.bind('<Control-space>', lambda e: self.start_recording())
        
    def start_recording(self):
        self.recording = True
        self.record_btn.config(state=tk.DISABLED, bg="#ff0000", text="RECORDING...")
        self.status_var.set("Recording (10 sec)... SPEAK NOW")
        threading.Thread(target=self.record_and_process, daemon=True).start()
    
    def record_and_process(self):
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
    Write-Host "[No speech detected]"
}
"""
            
            result = subprocess.run(
                ["powershell", "-Command", ps_script],
                capture_output=True,
                text=True,
                timeout=15
            )
            
            text = result.stdout.strip()
            
            if text and "[No speech" not in text:
                self.voice_text.delete(1.0, tk.END)
                self.voice_text.insert(1.0, text)
                
                response = self.find_response(text)
                
                self.response_text.delete(1.0, tk.END)
                self.response_text.insert(1.0, response)
                self.speak_btn.config(state=tk.NORMAL)
                self.status_var.set("Ready. Press SPEAK.")
            else:
                self.voice_text.delete(1.0, tk.END)
                self.voice_text.insert(1.0, "[No speech detected - speak louder]")
                self.status_var.set("No speech. Try again.")
                
        except Exception as e:
            self.response_text.delete(1.0, tk.END)
            self.response_text.insert(1.0, f"Error: {str(e)[:80]}")
            self.status_var.set("Error")
        finally:
            self.recording = False
            self.record_btn.config(state=tk.NORMAL, bg="#00ff00", text="RECORD (Ctrl+Space)")
    
    def speak_response(self):
        text = self.response_text.get(1.0, tk.END).strip()
        if text:
            self.speak_btn.config(state=tk.DISABLED)
            self.status_var.set("Speaking...")
            threading.Thread(target=self._speak, args=(text,), daemon=True).start()
    
    def _speak(self, text):
        try:
            self.tts_engine.say(text)
            self.tts_engine.runAndWait()
            self.status_var.set("Ready")
            self.speak_btn.config(state=tk.NORMAL)
        except Exception as e:
            self.status_var.set("TTS Error")
            self.speak_btn.config(state=tk.NORMAL)
    
    def clear_all(self):
        self.voice_text.delete(1.0, tk.END)
        self.response_text.delete(1.0, tk.END)
        self.speak_btn.config(state=tk.DISABLED)
        self.status_var.set("Cleared. Ready.")

if __name__ == "__main__":
    root = tk.Tk()
    app = VoiceSmart(root)
    app.recording = False
    root.mainloop()
