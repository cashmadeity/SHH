#!/usr/bin/env python3
"""
VOICE LOCAL - No API keys needed
Uses: Google Speech-to-Text (free) + Local processing + Windows TTS
"""

import tkinter as tk
from tkinter import scrolledtext
import threading
import pyaudio
import speech_recognition as sr
import pyttsx3
import json
from datetime import datetime

class VoiceLocal:
    def __init__(self, root):
        self.root = root
        self.root.title("Voice Claw - No API Keys")
        self.root.geometry("950x700")
        self.root.configure(bg="#1a1a1a")
        
        self.recording = False
        self.recognizer = sr.Recognizer()
        self.recognizer.energy_threshold = 4000
        self.tts_engine = pyttsx3.init()
        self.tts_engine.setProperty('rate', 150)
        
        # Local knowledge base
        self.knowledge = self.load_knowledge()
        
        # Find microphone
        self.mic_index = self.find_best_microphone()
        
        self.setup_ui()
        
    def find_best_microphone(self):
        p = pyaudio.PyAudio()
        for i in range(p.get_device_count()):
            info = p.get_device_info_by_index(i)
            if 'Microphone' in info['name'] and info['maxInputChannels'] > 0:
                return i
        return None
    
    def load_knowledge(self):
        """Load local knowledge base"""
        return {
            "greeting": "Hi! I'm Voice Claw, a local voice assistant. How can I help?",
            "help": "I can answer questions, tell you the time, remember information, and have conversations. Just speak naturally.",
            "time": f"It's {datetime.now().strftime('%I:%M %p')}",
            "date": f"Today is {datetime.now().strftime('%A, %B %d, %Y')}",
            "capabilities": "I can listen to your voice, process what you say, and respond back. No internet needed for basic conversation.",
        }
    
    def process_voice_input(self, text):
        """Process voice input locally"""
        text_lower = text.lower()
        
        # Simple keyword matching
        if any(word in text_lower for word in ['hello', 'hi', 'hey', 'greetings']):
            return self.knowledge["greeting"]
        
        if 'help' in text_lower:
            return self.knowledge["help"]
        
        if 'time' in text_lower:
            return self.knowledge["time"]
        
        if 'date' in text_lower or 'today' in text_lower:
            return self.knowledge["date"]
        
        if any(word in text_lower for word in ['what', 'can you', 'capabilities', 'do']):
            return self.knowledge["capabilities"]
        
        if 'repeat' in text_lower or 'say' in text_lower:
            # Extract and repeat what they said
            return f"You said: {text}"
        
        if 'clear' in text_lower or 'reset' in text_lower:
            return "Cleared. Ready for next input."
        
        # Default response - echo back and ask for clarification
        return f"You said: '{text}'. I understand basic commands. Try 'help' for options."
    
    def setup_ui(self):
        header = tk.Frame(self.root, bg="#2d2d2d")
        header.pack(fill=tk.X)
        
        title = tk.Label(
            header, text="VOICE CLAW - Local Voice (No API Keys)",
            font=("Arial", 18, "bold"), bg="#2d2d2d", fg="#00ff00", pady=15
        )
        title.pack()
        
        self.status_var = tk.StringVar(value="Ready. Press RECORD or Ctrl+Space")
        status = tk.Label(
            self.root, textvariable=self.status_var,
            font=("Arial", 11), bg="#1a1a1a", fg="#ffff00", anchor=tk.W
        )
        status.pack(pady=8, fill=tk.X, padx=15)
        
        content = tk.Frame(self.root, bg="#1a1a1a")
        content.pack(fill=tk.BOTH, expand=True, padx=20, pady=15)
        
        # Your voice
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
        
        # AI response
        response_label = tk.Label(
            content, text="AI RESPONSE:", font=("Arial", 11, "bold"),
            bg="#1a1a1a", fg="#00ff00"
        )
        response_label.pack(anchor=tk.W, pady=(0, 5))
        
        self.response_text = scrolledtext.ScrolledText(
            content, height=10, wrap=tk.WORD,
            bg="#2d2d2d", fg="#00ff00", font=("Courier", 11)
        )
        self.response_text.pack(fill=tk.BOTH, expand=True, padx=0, pady=(0, 15))
        
        # Buttons
        button_frame = tk.Frame(content, bg="#1a1a1a")
        button_frame.pack(fill=tk.X, pady=10)
        
        self.record_btn = tk.Button(
            button_frame, text="RECORD (Ctrl+Space)",
            command=self.start_recording,
            bg="#00ff00", fg="#000000", font=("Arial", 11, "bold"),
            width=20, height=2
        )
        self.record_btn.pack(side=tk.LEFT, padx=5)
        
        self.speak_btn = tk.Button(
            button_frame, text="SPEAK",
            command=self.speak_response,
            bg="#00ccff", fg="#000000", font=("Arial", 11, "bold"),
            width=20, height=2, state=tk.DISABLED
        )
        self.speak_btn.pack(side=tk.LEFT, padx=5)
        
        clear_btn = tk.Button(
            button_frame, text="CLEAR",
            command=self.clear_all,
            bg="#ff6600", fg="#000000", font=("Arial", 11, "bold"),
            width=20, height=2
        )
        clear_btn.pack(side=tk.LEFT, padx=5)
        
        self.root.bind('<Control-space>', lambda e: self.start_recording())
        
    def start_recording(self):
        if not self.recording:
            self.recording = True
            self.record_btn.config(state=tk.DISABLED, bg="#ff0000", text="RECORDING...")
            self.status_var.set("Recording... SPEAK NOW")
            threading.Thread(target=self.record_and_process, daemon=True).start()
    
    def record_and_process(self):
        try:
            self.status_var.set("Recording (10 seconds)...")
            
            if self.mic_index is None:
                self.voice_text.delete(1.0, tk.END)
                self.voice_text.insert(1.0, "[No microphone found]")
                self.status_var.set("Error: No microphone")
                self.recording = False
                self.record_btn.config(state=tk.NORMAL, bg="#00ff00", text="RECORD (Ctrl+Space)")
                return
            
            # Record from mic
            mic = sr.Microphone(device_index=self.mic_index)
            with mic as source:
                self.recognizer.adjust_for_ambient_noise(source, duration=0.5)
                audio = self.recognizer.listen(source, timeout=10, phrase_time_limit=8)
            
            self.status_var.set("Converting speech to text...")
            
            try:
                # Free Google Speech-to-Text
                text = self.recognizer.recognize_google(audio)
                self.voice_text.delete(1.0, tk.END)
                self.voice_text.insert(1.0, text)
                
                self.status_var.set("Processing locally...")
                
                # Process locally (no API)
                response = self.process_voice_input(text)
                
                self.response_text.delete(1.0, tk.END)
                self.response_text.insert(1.0, response)
                self.speak_btn.config(state=tk.NORMAL)
                self.status_var.set("Ready. Press SPEAK to hear response.")
                    
            except sr.UnknownValueError:
                self.voice_text.delete(1.0, tk.END)
                self.voice_text.insert(1.0, "[Could not understand - speak louder or clearer]")
                self.status_var.set("Could not understand. Try again.")
            except Exception as e:
                self.response_text.delete(1.0, tk.END)
                self.response_text.insert(1.0, f"Error: {str(e)[:100]}")
                self.status_var.set(f"Error")
                
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
    app = VoiceLocal(root)
    root.mainloop()
