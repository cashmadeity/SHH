import pyaudio
import speech_recognition as sr

print("=== AUDIO DEVICES ===")
p = pyaudio.PyAudio()
for i in range(p.get_device_count()):
    info = p.get_device_info_by_index(i)
    print(f"{i}: {info['name']} (In: {info['maxInputChannels']}, Out: {info['maxOutputChannels']})")

print("\n=== TESTING MICROPHONE ===")
recognizer = sr.Recognizer()
try:
    with sr.Microphone() as source:
        print("Listening for 3 seconds...")
        audio = recognizer.listen(source, timeout=3)
        print("Audio captured!")
        try:
            text = recognizer.recognize_google(audio)
            print(f"Heard: {text}")
        except sr.UnknownValueError:
            print("Could not understand audio")
except Exception as e:
    print(f"Microphone error: {e}")

print("\n=== TESTING SPEAKER ===")
import pyttsx3
engine = pyttsx3.init()
engine.say("Microphone test complete")
engine.runAndWait()
print("Speaker working")
