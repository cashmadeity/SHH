#!/usr/bin/env python3
"""
VOICE CLAW UI - Visual Interface for Local Voice Agent
Tkinter GUI with real-time display
"""

import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox
import threading
import subprocess
import tempfile
import pyaudio
import wave
import requests
import os
from pathlib import Path

class VoiceClawUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Voice Claw - Local Voice Agent")
        self.root.geometry("800x700")
        self.root.configure(bg="#1e1e1e")
        
        self.whisper_url = "http://localhost:10300"
        self.piper_url = "http://localhost:10200"
        self.recording = False
        self.sample_rate = 16000
        self.chunk = 1024
        
        self.setup_ui()
        self.check_servers()
        
    def setup_ui(self):
        # Header
        header = tk.Frame(self.root, bg="#2d2d2d", height=60)
        header.pack(fill=tk.X, padx=0, pady=0)
        header.pack_propagate(False)
        
        title = tk.Label(
            header, text="Voice Claw - Local Voice Agent",
            font=("Arial", 20, "bold"), bg="#2d2d2d", fg="#00ff00"
        )
        title.pack(pady=10)
        
        # Status bar
        self.status_var = tk.StringVar(value="Status: Checking servers...")
        status = tk.Label(
            self.root, textvariable=self.status_var,
            font=("Arial", 10), bg="#1e1e1e", fg="#ffff00"
        )
        status.pack(pady=5)
        
        # Main content frame
        content = tk.Frame(self.root, bg="#1e1e1e")
        content.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Input section
        input_label = tk.Label(
            content, text="YOU:", font=("Arial", 12, "bold"),
            bg="#1e1e1e", fg="#00ff00"
        )
        input_label.pack(anchor=tk.W, pady=(0, 5))
        
        self.user_text = scrolledtext.ScrolledText(
            content, height=4, width=80, wrap=tk.WORD,
            bg="#2d2d2d", fg="#ffffff", font=("Courier", 10)
        )
        self.user_text.pack(fill=tk.X, padx=0, pady=(0, 10))
        
        # Output section
        output_label = tk.Label(
            content, text="CLAW:", font=("Arial", 12, "bold"),
            bg="#1e1e1e", fg="#00ff00"
        )
        output_label.pack(anchor=tk.W, pady=(10, 5))
        
        self.response_text = scrolledtext.ScrolledText(
            content, height=8, width=80, wrap=tk.WORD,
            bg="#2d2d2d", fg="#00ff00", font=("Courier", 10)
        )
        self.response_text.pack(fill=tk.BOTH, expand=True, padx=0, pady=(0, 10))
        
        # Buttons frame
        button_frame = tk.Frame(content, bg="#1e1e1e")
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
            bg="#00ffff", fg="#000000", font=("Arial", 11, "bold"),
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
        
        # Bind hotkey
        self.root.bind('<Control-space>', lambda e: self.start_recording())
        
    def check_servers(self):
        """Check if Wyoming servers are running"""
        try:
            requests.get(f"{self.whisper_url}/api/info", timeout=2)
            requests.get(f"{self.piper_url}/api/info", timeout=2)
            self.status_var.set("Status: READY (Whisper STT + Piper TTS online)")
        except:
            self.status_var.set("Status: Starting Wyoming servers...")
            threading.Thread(target=self.start_servers, daemon=True).start()
    
    def start_servers(self):
        """Start Wyoming servers in background"""
        try:
            subprocess.Popen(
                ["wyoming-piper", "--model", "en_US-lessac-medium"],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL
            )
            subprocess.Popen(
                ["wyoming-faster-whisper", "--model", "base"],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL
            )
            self.root.after(3000, self.check_servers)
        except Exception as e:
            self.status_var.set(f"Status: ERROR - {str(e)}")
    
    def start_recording(self):
        """Record audio in thread"""
        if not self.recording:
            self.recording = True
            self.record_btn.configure(state=tk.DISABLED, bg="#ff0000")
            self.record_btn.configure(text="RECORDING...")
            threading.Thread(target=self.record_audio, daemon=True).start()
    
    def record_audio(self):
        """Record microphone"""
        try:
            audio = pyaudio.PyAudio()
            stream = audio.open(
                format=pyaudio.paInt16,
                channels=1,
                rate=self.sample_rate,
                input=True,
                frames_per_buffer=self.chunk
            )
            
            frames = []
            for _ in range(0, int(self.sample_rate / self.chunk * 6)):
                data = stream.read(self.chunk, exception_on_overflow=False)
                frames.append(data)
            
            stream.stop_stream()
            stream.close()
            audio.terminate()
            
            # Save WAV
            temp_wav = tempfile.NamedTemporaryFile(suffix=".wav", delete=False)
            wf = wave.open(temp_wav.name, 'wb')
            wf.setnchannels(1)
            wf.setsampwidth(2)
            wf.setframerate(self.sample_rate)
            wf.writeframes(b''.join(frames))
            wf.close()
            
            # STT
            self.stt_whisper(temp_wav.name)
            
        except Exception as e:
            self.update_response(f"Record error: {str(e)}")
        finally:
            self.recording = False
            self.record_btn.configure(state=tk.NORMAL, bg="#00ff00")
            self.record_btn.configure(text="RECORD (Ctrl+Space)")
    
    def stt_whisper(self, audio_file):
        """Whisper STT"""
        try:
            with open(audio_file, 'rb') as f:
                audio_data = f.read()
            
            response = requests.post(
                f"{self.whisper_url}/api/speech-to-text",
                files={'audio': ('audio.wav', audio_data)},
                timeout=15
            )
            
            os.unlink(audio_file)
            
            if response.status_code == 200:
                text = response.json().get('text', '').strip()
                self.update_user_text(text)
                if text:
                    self.query_openclaw(text)
        except Exception as e:
            self.update_response(f"STT error: {str(e)}")
    
    def update_user_text(self, text):
        """Update user text display"""
        self.user_text.delete(1.0, tk.END)
        self.user_text.insert(1.0, text)
    
    def query_openclaw(self, user_text):
        """Query OpenClaw"""
        try:
            result = subprocess.run(
                ["openclaw", "run", user_text],
                capture_output=True,
                text=True,
                timeout=15
            )
            response = result.stdout.strip()
            if response:
                self.update_response(response)
                self.speak_btn.configure(state=tk.NORMAL)
        except Exception as e:
            self.update_response(f"Error: {str(e)}")
    
    def update_response(self, text):
        """Update response display"""
        self.response_text.delete(1.0, tk.END)
        self.response_text.insert(1.0, text)
    
    def speak_response(self):
        """Speak the response"""
        text = self.response_text.get(1.0, tk.END).strip()
        if text:
            threading.Thread(target=self.tts_piper, args=(text,), daemon=True).start()
    
    def tts_piper(self, text):
        """Piper TTS"""
        try:
            response = requests.post(
                f"{self.piper_url}/api/text-to-speech",
                json={'text': text},
                stream=True,
                timeout=10
            )
            
            if response.status_code == 200:
                audio = pyaudio.PyAudio()
                stream = audio.open(
                    format=pyaudio.paFloat32,
                    channels=1,
                    rate=22050,
                    output=True
                )
                stream.write(response.content)
                stream.stop_stream()
                stream.close()
                audio.terminate()
        except Exception as e:
            messagebox.showerror("TTS Error", str(e))
    
    def clear_all(self):
        """Clear all text"""
        self.user_text.delete(1.0, tk.END)
        self.response_text.delete(1.0, tk.END)
        self.speak_btn.configure(state=tk.DISABLED)

if __name__ == "__main__":
    root = tk.Tk()
    app = VoiceClawUI(root)
    root.mainloop()
