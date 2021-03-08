import pyttsx3

engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

print(engine.getProperty('rate'))
print(engine.getProperty('volume'))

engine.setProperty('rate', 200)
engine.say('Listen Carefully...')
engine.setProperty('rate', 50)
engine.say('Do some work')
engine.runAndWait()
