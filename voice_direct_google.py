#!/usr/bin/env python3
"""
VOICE DIRECT GOOGLE - Direct microphone input, uses Google free STT
Open mic, always listening, responds based on learned knowledge
"""

import tkinter as tk
from tkinter import scrolledtext
import threading
import pyttsx3
import json
import time
import pyaudio
import speech_recognition as sr

class VoiceDirectGoogle:
    def __init__(self, root):
        self.root = root
        self.root.title("Voice Claw - Open Mic Chat")
        self.root.geometry("1000x800")
        self.root.configure(bg="#1a1a1a")
        
        self.tts_engine = pyttsx3.init()
        self.tts_engine.setProperty('rate', 150)
        
        self.recognizer = sr.Recognizer()
        self.recognizer.energy_threshold = 2000
        
        # Load knowledge
        self.conversations = self.load_json('conversations.json', 'conversations')
        self.learned = self.load_json('learned_knowledge.json', None)
        self.concepts = self.learned.get('key_concepts', []) if self.learned else []
        self.patterns = self.learned.get('response_patterns', []) if self.learned else []
        self.vocab = self.learned.get('vocabulary', []) if self.learned else []
        
        self.listening = False
        
        self.setup_ui()
        
    def load_json(self, filename, key):
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
                return data.get(key, []) if key else data
        except:
            return [] if key else {}
    
    def find_response(self, user_input):
        user_lower = user_input.lower()
        
        for conv in self.conversations:
            for keyword in conv.get('keywords', []):
                if keyword.lower() in user_lower:
                    return conv['response']
        
        for concept in self.concepts:
            concept_words = concept['concept'].lower()
            if any(word in concept_words for word in user_lower.split()):
                return f"From my learning: {concept['concept']}"
        
        for pattern in self.patterns:
            pattern_words = pattern['topic'].lower()
            if any(word in pattern_words for word in user_lower.split()):
                return f"About {pattern['topic']}: {pattern['summary']}"
        
        user_words = set(user_lower.split())
        vocab_matches = user_words.intersection(set(self.vocab))
        
        if vocab_matches:
            matches_str = ', '.join(list(vocab_matches)[:2])
            return f"I understand: {matches_str}. Keep talking."
        
        return "I'm listening. Tell me more."
    
    def setup_ui(self):
        header = tk.Frame(self.root, bg="#2d2d2d")
        header.pack(fill=tk.X)
        
        title = tk.Label(
            header, text="VOICE CLAW - Open Mic Chat",
            font=("Arial", 16, "bold"), bg="#2d2d2d", fg="#00ff00", pady=15
        )
        title.pack()
        
        self.status_var = tk.StringVar(value="Ready. Click START LISTENING")
        status = tk.Label(
            self.root, textvariable=self.status_var,
            font=("Arial", 11), bg="#1a1a1a", fg="#ffff00", anchor=tk.W
        )
        status.pack(pady=8, fill=tk.X, padx=15)
        
        content = tk.Frame(self.root, bg="#1a1a1a")
        content.pack(fill=tk.BOTH, expand=True, padx=20, pady=15)
        
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
        self.conversation_text.config(state=tk.NORMAL)
        timestamp = time.strftime("%H:%M:%S")
        self.conversation_text.insert(tk.END, f"[{timestamp}] {speaker}: {text}\n")
        self.conversation_text.see(tk.END)
        self.conversation_text.config(state=tk.DISABLED)
        self.root.update()
    
    def start_listening(self):
        self.listening = True
        self.start_btn.config(state=tk.DISABLED, bg="#999999")
        self.stop_btn.config(state=tk.NORMAL, bg="#ff0000")
        self.status_var.set("LISTENING...")
        self.add_to_conversation("SYSTEM", "Open mic. Listening for your voice...")
        threading.Thread(target=self.listening_loop, daemon=True).start()
    
    def listening_loop(self):
        while self.listening:
            try:
                self.status_var.set("LISTENING... Speak now")
                
                with sr.Microphone() as source:
                    self.recognizer.adjust_for_ambient_noise(source, duration=0.5)
                    audio = self.recognizer.listen(source, timeout=10, phrase_time_limit=5)
                
                self.status_var.set("Converting speech...")
                
                try:
                    text = self.recognizer.recognize_google(audio)
                    
                    self.add_to_conversation("YOU", text)
                    self.status_var.set(f"Heard: {text}")
                    
                    response = self.find_response(text)
                    self.add_to_conversation("CLAW", response)
                    
                    self.status_var.set("Speaking...")
                    self.tts_engine.say(response)
                    self.tts_engine.runAndWait()
                    
                    self.status_var.set("LISTENING...")
                    
                except sr.UnknownValueError:
                    self.status_var.set("Could not understand. Listening...")
                except sr.RequestError as e:
                    self.add_to_conversation("SYSTEM", f"API Error: {str(e)[:50]}")
                    self.status_var.set("API Error. Continuing...")
                
            except sr.RequestError:
                self.status_var.set("Timeout. Listening...")
            except Exception as e:
                self.add_to_conversation("SYSTEM", f"Error: {str(e)[:60]}")
                if not self.listening:
                    break
            
            time.sleep(0.2)
    
    def stop_listening(self):
        self.listening = False
        self.start_btn.config(state=tk.NORMAL, bg="#00ff00")
        self.stop_btn.config(state=tk.DISABLED, bg="#999999")
        self.status_var.set("Stopped.")
        self.add_to_conversation("SYSTEM", "Microphone closed.")
    
    def clear_conversation(self):
        self.conversation_text.config(state=tk.NORMAL)
        self.conversation_text.delete(1.0, tk.END)
        self.conversation_text.config(state=tk.DISABLED)
        self.status_var.set("Cleared.")

if __name__ == "__main__":
    root = tk.Tk()
    app = VoiceDirectGoogle(root)
    root.mainloop()
