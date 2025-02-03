import pyttsx3

engine = pyttsx3.init()

engine.setProperty('rate', 150)
engine.setProperty('volume', 1.0)

voices = engine.getProperty('voices')

for index, voice in enumerate(voices):
    print(f"Voice {index}: {voice.name} ({voice.id})")

engine.setProperty('voice', voices[2].id)

text = "Hello My Name is Dhillon"

engine.say(text)

engine.runAndWait()