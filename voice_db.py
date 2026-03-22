#!/usr/bin/env python3
"""
VOICE DB - Uses conversations.json for responses
No APIs. No ML. Pure local database matching.
"""

import tkinter as tk
from tkinter import scrolledtext
import threading
import pyaudio
import speech_recognition as sr
import pyttsx3
import json
from datetime import datetime
import os

class VoiceDB:
    def __init__(self, root):
        self.root = root
        self.root.title("Voice Claw - Local Database")
        self.root.geometry("950x700")
        self.root.configure(bg="#1a1a1a")
        
        self.recording = False
        self.recognizer = sr.Recognizer()
        self.recognizer.energy_threshold = 3000
        self.tts_engine = pyttsx3.init()
        self.tts_engine.setProperty('rate', 150)
        
        # Load conversation database
        self.conversations = self.load_conversations()
        
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
    
    def load_conversations(self):
        """Load conversations.json"""
        try:
            with open('conversations.json', 'r') as f:
                data = json.load(f)
                return data.get('conversations', [])
        except:
            return []
    
    def find_response(self, user_input):
        """Match user input against conversation database"""
        user_lower = user_input.lower()
        
        for conv in self.conversations:
            for keyword in conv.get('keywords', []):
                if keyword.lower() in user_lower:
                    return conv['response']
        
        # No match
        return f"I understood you said: '{user_input}'. Try 'help' for options or ask me a question."
    
    def setup_ui(self):
        header = tk.Frame(self.root, bg="#2d2d2d")
        header.pack(fill=tk.X)
        
        title = tk.Label(
            header, text="VOICE CLAW - Local Database (conversations.json)",
            font=("Arial", 16, "bold"), bg="#2d2d2d", fg="#00ff00", pady=15
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
        
        # Response
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
            self.status_var.set("Recording (8 seconds)... SPEAK NOW")
            threading.Thread(target=self.record_and_process, daemon=True).start()
    
    def record_and_process(self):
        try:
            if self.mic_index is None:
                self.voice_text.delete(1.0, tk.END)
                self.voice_text.insert(1.0, "[No microphone found]")
                self.status_var.set("Error: No microphone")
                self.recording = False
                self.record_btn.config(state=tk.NORMAL, bg="#00ff00", text="RECORD (Ctrl+Space)")
                return
            
            # Record
            mic = sr.Microphone(device_index=self.mic_index)
            with mic as source:
                self.recognizer.adjust_for_ambient_noise(source, duration=0.5)
                audio = self.recognizer.listen(source, timeout=8, phrase_time_limit=7)
            
            self.status_var.set("Converting speech to text...")
            
            try:
                # Free Google Speech-to-Text
                text = self.recognizer.recognize_google(audio)
                self.voice_text.delete(1.0, tk.END)
                self.voice_text.insert(1.0, text)
                
                # Find response from database
                response = self.find_response(text)
                
                self.response_text.delete(1.0, tk.END)
                self.response_text.insert(1.0, response)
                self.speak_btn.config(state=tk.NORMAL)
                self.status_var.set("Ready. Press SPEAK to hear response.")
                    
            except sr.UnknownValueError:
                self.voice_text.delete(1.0, tk.END)
                self.voice_text.insert(1.0, "[Could not understand - speak louder]")
                self.status_var.set("Could not understand. Try again.")
            except Exception as e:
                self.response_text.delete(1.0, tk.END)
                self.response_text.insert(1.0, f"Error: {str(e)[:100]}")
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
    app = VoiceDB(root)
    root.mainloop()
