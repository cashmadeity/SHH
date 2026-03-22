import pyttsx3

engine = pyttsx3.init()
engine.setProperty('rate', 150)

sample_text = """
Intelligence is not a single thing. It is a pattern that emerges when information flows through a system capable of adapting. What makes a system appear intelligent is responsiveness. A system that adjusts, even imperfectly, begins to resemble thought.

At the core of modern artificial intelligence lies pattern recognition. Given enough examples, a system can identify structure in what first appears to be noise. With enough data and computational power, systems begin to generalize beyond memorization into abstraction.

Voice is one of humanity's most natural interfaces. A microphone captures sound. Digital processing converts vibrations into data. Machine learning transforms data into meaning. The elegance of this loop lies in its simplicity for the user. Speak. Be understood. Receive response. No keyboard required.
"""

print("Playing 60-second vocabulary sample...")
print("Content: Voice, AI, Systems, Intelligence, Recognition, Pattern, Data\n")

engine.say(sample_text)
engine.runAndWait()

print("\nSample complete. Vocabulary loaded.")
