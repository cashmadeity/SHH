#!/usr/bin/env python3
"""
YouTube Local Learner
A Windows app to download YouTube videos and process them for local AI training.
No API calls. Personal use only.

Requirements:
- yt-dlp (YouTube downloader)
- pydub (audio processing)
- whisper-ctranslate2 or similar (local transcription)
- tkinter (built-in)

Install: pip install yt-dlp pydub whisper-ctranslate2
"""

import os
import sys
import json
import threading
import subprocess
from pathlib import Path
from datetime import datetime
from typing import Optional, List, Dict
import tkinter as tk
from tkinter import ttk, filedialog, messagebox, scrolledtext

# Configuration
CONFIG = {
    "download_dir": str(Path.home() / "YouTubeLocal" / "downloads"),
    "processed_dir": str(Path.home() / "YouTubeLocal" / "processed"),
    "transcripts_dir": str(Path.home() / "YouTubeLocal" / "transcripts"),
    "metadata_dir": str(Path.home() / "YouTubeLocal" / "metadata"),
}

# Ensure directories exist
for dir_path in CONFIG.values():
    Path(dir_path).mkdir(parents=True, exist_ok=True)


class YouTubeLocalLearner:
    """Main app class for downloading and processing YouTube videos."""
    
    def __init__(self, root):
        self.root = root
        self.root.title("YouTube Local Learner")
        self.root.geometry("900x700")
        self.processing = False
        self.current_process = None
        
        self.setup_ui()
        self.load_config()
    
    def setup_ui(self):
        """Build the GUI."""
        # Title
        title = ttk.Label(self.root, text="YouTube Local Learner", font=("Arial", 16, "bold"))
        title.pack(pady=10)
        
        # URL input
        url_frame = ttk.Frame(self.root)
        url_frame.pack(padx=10, pady=5, fill="x")
        
        ttk.Label(url_frame, text="YouTube URL:").pack(side="left", padx=5)
        self.url_entry = ttk.Entry(url_frame, width=60)
        self.url_entry.pack(side="left", padx=5, fill="x", expand=True)
        
        # Buttons
        button_frame = ttk.Frame(self.root)
        button_frame.pack(padx=10, pady=10, fill="x")
        
        self.download_btn = ttk.Button(button_frame, text="Download & Process", command=self.start_download)
        self.download_btn.pack(side="left", padx=5)
        
        ttk.Button(button_frame, text="Open Download Folder", command=self.open_downloads).pack(side="left", padx=5)
        ttk.Button(button_frame, text="Settings", command=self.open_settings).pack(side="left", padx=5)
        
        # Status
        self.status_var = tk.StringVar(value="Ready")
        status = ttk.Label(self.root, textvariable=self.status_var, foreground="blue")
        status.pack(pady=5)
        
        # Progress bar
        self.progress = ttk.Progressbar(self.root, mode="indeterminate")
        self.progress.pack(padx=10, pady=5, fill="x")
        
        # Output log
        log_label = ttk.Label(self.root, text="Processing Log:")
        log_label.pack(padx=10, pady=(10, 0), anchor="w")
        
        self.log_text = scrolledtext.ScrolledText(self.root, height=20, width=100, state="normal")
        self.log_text.pack(padx=10, pady=5, fill="both", expand=True)
        
        # Footer
        footer = ttk.Label(
            self.root,
            text=f"Downloads: {CONFIG['download_dir']} | Processed: {CONFIG['processed_dir']}",
            font=("Arial", 8),
            foreground="gray"
        )
        footer.pack(pady=5)
    
    def log(self, message: str):
        """Log a message to the UI."""
        timestamp = datetime.now().strftime("%H:%M:%S")
        self.log_text.insert("end", f"[{timestamp}] {message}\n")
        self.log_text.see("end")
        self.root.update()
    
    def start_download(self):
        """Start the download process in a thread."""
        url = self.url_entry.get().strip()
        if not url:
            messagebox.showwarning("Error", "Please enter a YouTube URL")
            return
        
        if self.processing:
            messagebox.showinfo("Info", "Already processing a video")
            return
        
        self.processing = True
        self.download_btn.config(state="disabled")
        self.progress.start()
        self.status_var.set("Processing...")
        
        # Run in background thread
        thread = threading.Thread(target=self.download_and_process, args=(url,), daemon=True)
        thread.start()
    
    def download_and_process(self, url: str):
        """Download video and process it."""
        try:
            self.log(f"Starting download: {url}")
            
            # Step 1: Download video
            video_path = self.download_video(url)
            if not video_path:
                self.log("❌ Download failed")
                return
            
            self.log(f"✅ Downloaded: {video_path}")
            
            # Step 2: Extract metadata
            metadata = self.extract_metadata(video_path, url)
            self.log(f"✅ Metadata extracted: {len(metadata)} fields")
            
            # Step 3: Extract audio and transcribe
            transcript_path = self.extract_and_transcribe(video_path)
            if transcript_path:
                self.log(f"✅ Transcript saved: {transcript_path}")
            
            # Step 4: Create learning package
            self.create_learning_package(video_path, metadata, transcript_path)
            self.log("✅ Learning package created")
            
            self.log(f"\n✨ Ready for local model training!")
            self.status_var.set("✅ Complete")
            
        except Exception as e:
            self.log(f"❌ Error: {str(e)}")
            self.status_var.set("❌ Error")
        finally:
            self.processing = False
            self.progress.stop()
            self.download_btn.config(state="normal")
    
    def download_video(self, url: str) -> Optional[str]:
        """Download video using yt-dlp."""
        try:
            output_template = os.path.join(CONFIG["download_dir"], "%(title)s.%(ext)s")
            
            cmd = [
                "yt-dlp",
                "-f", "best[ext=mp4]/best",  # Best quality MP4
                "-o", output_template,
                "--no-warnings",
                url
            ]
            
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=600)
            
            if result.returncode != 0:
                self.log(f"yt-dlp error: {result.stderr}")
                return None
            
            # Find the downloaded file
            for file in sorted(Path(CONFIG["download_dir"]).glob("*"), key=os.path.getmtime, reverse=True):
                if file.is_file() and file.suffix in [".mp4", ".mkv", ".webm"]:
                    return str(file)
            
            return None
        
        except Exception as e:
            self.log(f"Download error: {str(e)}")
            return None
    
    def extract_metadata(self, video_path: str, url: str) -> Dict:
        """Extract video metadata using yt-dlp."""
        try:
            cmd = [
                "yt-dlp",
                "--dump-json",
                "--no-warnings",
                url
            ]
            
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
            if result.returncode == 0:
                metadata = json.loads(result.stdout)
                return {
                    "title": metadata.get("title", "Unknown"),
                    "description": metadata.get("description", ""),
                    "duration": metadata.get("duration", 0),
                    "uploader": metadata.get("uploader", "Unknown"),
                    "upload_date": metadata.get("upload_date", ""),
                    "url": url,
                    "downloaded_at": datetime.now().isoformat(),
                }
            return {}
        except Exception as e:
            self.log(f"Metadata extraction error: {str(e)}")
            return {}
    
    def extract_and_transcribe(self, video_path: str) -> Optional[str]:
        """Extract audio and transcribe using local Whisper."""
        try:
            import subprocess
            
            audio_path = video_path.replace(".mp4", ".wav")
            
            # Extract audio
            self.log("Extracting audio...")
            cmd_audio = [
                "ffmpeg", "-i", video_path, "-q:a", "9", "-n", audio_path
            ]
            subprocess.run(cmd_audio, capture_output=True, timeout=300)
            
            if not os.path.exists(audio_path):
                self.log("Audio extraction failed, skipping transcription")
                return None
            
            # Transcribe
            self.log("Transcribing audio (this may take a while)...")
            transcript_path = os.path.join(CONFIG["transcripts_dir"], Path(video_path).stem + ".txt")
            
            cmd_whisper = [
                "whisper",
                audio_path,
                "--output_format", "txt",
                "--output_dir", CONFIG["transcripts_dir"],
                "--model", "base",  # Use 'base' or 'small' for speed; adjust as needed
                "--language", "en"
            ]
            
            result = subprocess.run(cmd_whisper, capture_output=True, text=True, timeout=1800)
            
            if result.returncode == 0 and os.path.exists(transcript_path):
                return transcript_path
            
            self.log(f"Transcription warning: {result.stderr[:200]}")
            return None
        
        except Exception as e:
            self.log(f"Transcription error: {str(e)}")
            return None
    
    def create_learning_package(self, video_path: str, metadata: Dict, transcript_path: Optional[str]):
        """Create a structured learning package for the AI model."""
        try:
            package_name = Path(video_path).stem
            package_dir = Path(CONFIG["processed_dir"]) / package_name
            package_dir.mkdir(exist_ok=True)
            
            # Save metadata
            metadata_file = package_dir / "metadata.json"
            with open(metadata_file, "w") as f:
                json.dump(metadata, f, indent=2)
            
            # Copy transcript if available
            if transcript_path and os.path.exists(transcript_path):
                import shutil
                shutil.copy(transcript_path, package_dir / "transcript.txt")
            
            # Create learning format for local AI
            learning_file = package_dir / "learning_data.jsonl"
            with open(learning_file, "w") as f:
                # Metadata entry
                f.write(json.dumps({
                    "type": "metadata",
                    "title": metadata.get("title"),
                    "description": metadata.get("description"),
                    "duration_seconds": metadata.get("duration"),
                    "uploader": metadata.get("uploader"),
                }) + "\n")
                
                # Transcript entries (split into chunks for better learning)
                if transcript_path and os.path.exists(transcript_path):
                    with open(transcript_path, "r") as tf:
                        text = tf.read()
                        # Split into paragraphs
                        chunks = [chunk.strip() for chunk in text.split("\n\n") if chunk.strip()]
                        for i, chunk in enumerate(chunks):
                            f.write(json.dumps({
                                "type": "transcript_chunk",
                                "chunk_id": i,
                                "content": chunk,
                                "video_title": metadata.get("title"),
                            }) + "\n")
            
            self.log(f"Learning package created at: {package_dir}")
        
        except Exception as e:
            self.log(f"Package creation error: {str(e)}")
    
    def open_downloads(self):
        """Open the downloads folder."""
        os.startfile(CONFIG["download_dir"]) if sys.platform == "win32" else \
        subprocess.Popen(["open", CONFIG["download_dir"]]) if sys.platform == "darwin" else \
        subprocess.Popen(["xdg-open", CONFIG["download_dir"]])
    
    def open_settings(self):
        """Open settings dialog."""
        settings_window = tk.Toplevel(self.root)
        settings_window.title("Settings")
        settings_window.geometry("500x300")
        
        ttk.Label(settings_window, text="Configuration", font=("Arial", 12, "bold")).pack(pady=10)
        
        for key, path in CONFIG.items():
            frame = ttk.Frame(settings_window)
            frame.pack(padx=10, pady=5, fill="x")
            
            ttk.Label(frame, text=f"{key}:").pack(side="left", anchor="w", width=20)
            entry = ttk.Entry(frame, width=40)
            entry.insert(0, path)
            entry.pack(side="left", fill="x", expand=True, padx=5)
            
            def update_config(k=key, e=entry):
                CONFIG[k] = e.get()
                Path(CONFIG[k]).mkdir(parents=True, exist_ok=True)
            
            ttk.Button(frame, text="Browse", command=lambda k=key: self.browse_folder(k)).pack(side="left", padx=5)
        
        ttk.Button(settings_window, text="Save", command=lambda: [update_config(), settings_window.destroy()]).pack(pady=10)
    
    def browse_folder(self, key: str):
        """Browse for a folder."""
        folder = filedialog.askdirectory(title=f"Select folder for {key}")
        if folder:
            CONFIG[key] = folder
            Path(CONFIG[key]).mkdir(parents=True, exist_ok=True)
    
    def load_config(self):
        """Load config from file if it exists."""
        config_file = Path.home() / "YouTubeLocal" / "config.json"
        if config_file.exists():
            try:
                with open(config_file) as f:
                    saved_config = json.load(f)
                    CONFIG.update(saved_config)
            except:
                pass


def main():
    """Run the app."""
    root = tk.Tk()
    app = YouTubeLocalLearner(root)
    root.mainloop()


if __name__ == "__main__":
    main()
