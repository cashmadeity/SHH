#!/usr/bin/env python3
"""
VOICE CLAW SIMPLE - Local Voice UI (No Wyoming dependency)
Records audio, uses OpenClaw directly, shows results
"""

import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox
import threading
import subprocess
import tempfile
import pyaudio
import wave
import os
from pathlib import Path

class VoiceClawSimple:
    def __init__(self, root):
        self.root = root
        self.root.title("Voice Claw - Local Voice Agent")
        self.root.geometry("900x650")
        self.root.configure(bg="#1e1e1e")
        
        self.recording = False
        self.sample_rate = 16000
        self.chunk = 1024
        
        self.setup_ui()
        
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
        
        # Status
        self.status_var = tk.StringVar(value="Ready. Click RECORD or Ctrl+Space")
        status = tk.Label(
            self.root, textvariable=self.status_var,
            font=("Arial", 10), bg="#1e1e1e", fg="#ffff00", anchor=tk.W
        )
        status.pack(pady=5, fill=tk.X, padx=10)
        
        # Content
        content = tk.Frame(self.root, bg="#1e1e1e")
        content.pack(fill=tk.BOTH, expand=True, padx=15, pady=15)
        
        # Input
        input_label = tk.Label(
            content, text="Your Voice:", font=("Arial", 12, "bold"),
            bg="#1e1e1e", fg="#00ff00"
        )
        input_label.pack(anchor=tk.W, pady=(0, 5))
        
        self.user_text = scrolledtext.ScrolledText(
            content, height=4, wrap=tk.WORD,
            bg="#2d2d2d", fg="#ffffff", font=("Courier", 11)
        )
        self.user_text.pack(fill=tk.X, padx=0, pady=(0, 15))
        
        # Output
        output_label = tk.Label(
            content, text="AI Response:", font=("Arial", 12, "bold"),
            bg="#1e1e1e", fg="#00ff00"
        )
        output_label.pack(anchor=tk.W, pady=(0, 5))
        
        self.response_text = scrolledtext.ScrolledText(
            content, height=8, wrap=tk.WORD,
            bg="#2d2d2d", fg="#00ff00", font=("Courier", 11)
        )
        self.response_text.pack(fill=tk.BOTH, expand=True, padx=0, pady=(0, 15))
        
        # Buttons
        button_frame = tk.Frame(content, bg="#1e1e1e")
        button_frame.pack(fill=tk.X, pady=10)
        
        self.record_btn = tk.Button(
            button_frame, text="RECORD (Ctrl+Space)",
            command=self.start_recording,
            bg="#00ff00", fg="#000000", font=("Arial", 12, "bold"),
            width=25, height=2
        )
        self.record_btn.pack(side=tk.LEFT, padx=5)
        
        clear_btn = tk.Button(
            button_frame, text="CLEAR",
            command=self.clear_all,
            bg="#ff6600", fg="#000000", font=("Arial", 12, "bold"),
            width=25, height=2
        )
        clear_btn.pack(side=tk.LEFT, padx=5)
        
        # Hotkey
        self.root.bind('<Control-space>', lambda e: self.start_recording())
        
    def start_recording(self):
        if not self.recording:
            self.recording = True
            self.record_btn.configure(state=tk.DISABLED, bg="#ff0000")
            self.record_btn.configure(text="RECORDING...")
            self.status_var.set("Recording... speak now")
            threading.Thread(target=self.record_and_process, daemon=True).start()
    
    def record_and_process(self):
        try:
            # Record
            audio_file = self.record_audio()
            if not audio_file:
                self.status_var.set("Record failed")
                self.recording = False
                self.record_btn.configure(state=tk.NORMAL, bg="#00ff00")
                self.record_btn.configure(text="RECORD (Ctrl+Space)")
                return
            
            self.status_var.set("Converting speech to text...")
            
            # Use OpenClaw to process
            result = subprocess.run(
                ["openclaw", "run", "--input-file", audio_file],
                capture_output=True,
                text=True,
                timeout=20
            )
            
            if result.returncode == 0 and result.stdout:
                response = result.stdout.strip()
                self.update_response(response)
                self.status_var.set("Done. Ready for next input.")
            else:
                self.update_response("Error: No response from OpenClaw")
                self.status_var.set("Error processing request")
            
            os.unlink(audio_file)
            
        except Exception as e:
            self.update_response(f"Error: {str(e)}")
            self.status_var.set(f"Error: {str(e)}")
        finally:
            self.recording = False
            self.record_btn.configure(state=tk.NORMAL, bg="#00ff00")
            self.record_btn.configure(text="RECORD (Ctrl+Space)")
    
    def record_audio(self):
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
            
            self.user_text.delete(1.0, tk.END)
            self.user_text.insert(1.0, "[Audio recorded - processing...]")
            
            return temp_wav.name
            
        except Exception as e:
            self.update_response(f"Record error: {str(e)}")
            return None
    
    def update_response(self, text):
        self.response_text.delete(1.0, tk.END)
        self.response_text.insert(1.0, text)
    
    def clear_all(self):
        self.user_text.delete(1.0, tk.END)
        self.response_text.delete(1.0, tk.END)
        self.status_var.set("Cleared. Ready for next input.")

if __name__ == "__main__":
    root = tk.Tk()
    app = VoiceClawSimple(root)
    root.mainloop()
