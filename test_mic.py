#!/usr/bin/env python3
import pyaudio
import numpy as np

print("Testing microphone...")
p = pyaudio.PyAudio()

print(f"\nTotal audio devices: {p.get_device_count()}\n")
print("Available microphones:")

for i in range(p.get_device_count()):
    info = p.get_device_info_by_index(i)
    if info['maxInputChannels'] > 0:
        print(f"  {i}: {info['name']}")

# Test recording from default device
print("\nRecording 3 seconds of audio (speak now)...")
try:
    stream = p.open(
        format=pyaudio.paFloat32,
        channels=1,
        rate=16000,
        input=True,
        frames_per_buffer=1024
    )
    
    frames = []
    for i in range(0, int(16000 / 1024 * 3)):
        data = stream.read(1024)
        frames.append(np.frombuffer(data, dtype=np.float32))
    
    stream.stop_stream()
    stream.close()
    
    # Check if audio was captured
    audio_data = np.concatenate(frames)
    volume = np.sqrt(np.mean(audio_data**2))
    
    print(f"\nAudio captured!")
    print(f"Volume level: {volume:.4f}")
    
    if volume < 0.001:
        print("WARNING: Very low volume. Check microphone is unmuted and close to mouth.")
    else:
        print("Microphone is working!")
        
except Exception as e:
    print(f"Error: {e}")

p.terminate()
