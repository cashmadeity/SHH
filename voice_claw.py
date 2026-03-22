#!/usr/bin/env python3
"""
OPENCLAW LOCAL VOICE AGENT v3.0
100% LOCAL • NO API KEYS • WHISPER + PIPER + OPENCLAW
Hotkey: Ctrl+Space • Daemon: --daemon • Wyoming Protocol Ready
"""

import sys, os, subprocess, threading, queue, time, signal, json
import numpy as np
import tempfile
from pathlib import Path
import pyaudio
import wave
import keyboard
import requests
from typing import Optional

class VoiceClaw:
    def __init__(self):
        self.whisper_url = "http://localhost:10300"
        self.piper_url = "http://localhost:10200"
        self.openclaw_proc = None
        self.listening = False
        self.daemon_mode = len(sys.argv) > 1 and sys.argv[1] == "--daemon"
        self.sample_rate = 16000
        self.chunk = 1024
        self.record_queue = queue.Queue()
        
    def install_dependencies(self):
        """Auto-install everything needed"""
        print("🔧 Installing dependencies...")
        
        deps = ["numpy", "soundfile", "pyaudio", "keyboard", "requests"]
        for dep in deps:
            subprocess.run(["pip", "install", "-q", dep], capture_output=True)
        
        print("✅ Dependencies ready!")
    
    def start_wyoming_servers(self):
        """Start Wyoming Whisper + Piper servers"""
        print("🚀 Starting Wyoming servers...")
        
        try:
            # Piper TTS
            subprocess.Popen(
                ["piper", "--model", "en_US-lessac-medium", 
                 "--server", "localhost:10200"],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL
            )
            
            # Whisper STT
            subprocess.Popen(
                ["wyoming-faster-whisper", "--model", "base"],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL
            )
            
            time.sleep(2)
            print("✅ Wyoming servers started")
        except Exception as e:
            print(f"⚠️  Wyoming servers: {e}")
    
    def record_audio(self, duration=6):
        """Record microphone input"""
        try:
            audio = pyaudio.PyAudio()
            
            stream = audio.open(
                format=pyaudio.paInt16,
                channels=1,
                rate=self.sample_rate,
                input=True,
                frames_per_buffer=self.chunk
            )
            
            print("🎤 Listening...")
            frames = []
            
            for _ in range(0, int(self.sample_rate / self.chunk * duration)):
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
            
            return temp_wav.name
        except Exception as e:
            print(f"❌ Record error: {e}")
            return None
    
    def stt_whisper(self, audio_file: str) -> str:
        """Wyoming Whisper STT"""
        try:
            with open(audio_file, 'rb') as f:
                audio_data = f.read()
            
            response = requests.post(
                f"{self.whisper_url}/api/speech-to-text",
                files={'audio': ('audio.wav', audio_data)},
                timeout=10
            )
            
            os.unlink(audio_file)
            
            if response.status_code == 200:
                return response.json().get('text', '').strip()
            return ""
        except Exception as e:
            print(f"❌ STT error: {e}")
            return ""
    
    def tts_piper(self, text: str):
        """Wyoming Piper TTS"""
        try:
            response = requests.post(
                f"{self.piper_url}/api/text-to-speech",
                json={'text': text},
                stream=True,
                timeout=10
            )
            
            if response.status_code == 200:
                # Play audio
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
            print(f"❌ TTS error: {e}")
    
    def query_openclaw(self, user_text: str) -> str:
        """Pipe to OpenClaw"""
        try:
            result = subprocess.run(
                ["openclaw", "run", user_text],
                capture_output=True,
                text=True,
                timeout=15
            )
            return result.stdout.strip()
        except Exception as e:
            return f"Error: {e}"
    
    def conversation_loop(self):
        """Main voice loop"""
        self.install_dependencies()
        self.start_wyoming_servers()
        
        print("\n🤖 VOICE CLAW ACTIVE")
        print("🎯 Hotkey: Ctrl+Space to speak")
        print("⏹️  Ctrl+C to exit\n")
        
        try:
            while True:
                keyboard.wait('ctrl+space')
                
                audio_file = self.record_audio()
                if not audio_file:
                    continue
                
                user_text = self.stt_whisper(audio_file)
                if not user_text or len(user_text) < 2:
                    print("❌ No speech detected\n")
                    continue
                
                print(f"👤 YOU: {user_text}")
                
                ai_response = self.query_openclaw(user_text)
                if not ai_response:
                    print("❌ No response\n")
                    continue
                
                print(f"🤖 CLAW: {ai_response}\n")
                
                self.tts_piper(ai_response)
                
        except KeyboardInterrupt:
            print("\n👋 Shutdown")
    
    def cleanup(self):
        if self.openclaw_proc:
            self.openclaw_proc.terminate()

if __name__ == "__main__":
    app = VoiceClaw()
    
    def signal_handler(sig, frame):
        app.cleanup()
        sys.exit(0)
    
    signal.signal(signal.SIGINT, signal_handler)
    app.conversation_loop()
