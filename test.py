# Python 2.x program for Speech Recognition
import speech_recognition as sr
import pyautogui as pag
import time


def isMatching(text, keywords):
    text = text.split(' ')
    counter = 0
    for word in text:
        if (word == keywords[counter]):
            counter += 1
            if (counter == len(keywords)):
                return True

    return False


def doAutomatedTask(text):
    if isMatching(text, ['increase', 'volume']):
        for i in range(10):
            pag.press('volumeup')

    if isMatching(text, ['decrease', 'volume']):
        for i in range(10):
            pag.press('volumedown')

    if isMatching(text, ['stop', 'music']) or isMatching(text, ['play', 'music']) or isMatching(text, ['pause', 'music']):
        pag.press('playpause')

    if isMatching(text, ['next', 'song']):
        pag.press('nexttrack')

    if isMatching(text, ['previous', 'song']):
        pag.press('prevtrack')

    elif isMatching(text, ['switch', 'application']) or isMatching(text, ['next', 'application']):
        pag.hotkey('alt', 'tab')

    elif isMatching(text, ['previous', 'application']):
        pag.hotkey('alt', 'shift', 'tab')

    elif isMatching(text, ['new', 'tab']):
        pag.hotkey('ctrl', 't')

    elif isMatching(text, ['close', 'tab']):
        pag.hotkey('ctrl', 'w')

    elif isMatching(text, ['open', 'incognito', 'window']):
        pag.hotkey('ctrl', 'shift', 'n')

# extend this functionality to dynamically fetch website name
    elif isMatching(text, ['go', 'to', 'facebook.com']):
        pag.hotkey('ctrl', 'l')
        pag.write('facebook.com')
        pag.press('enter')

    elif isMatching(text, ['desktop']) or isMatching(text, ['minimise']):
        pag.hotkey('win', 'd')

# extend this functionality to dynamically fetch application name
    elif isMatching(text, ['open', 'application', 'word']):
        pag.press('win')
        pag.write('word')
        time.sleep(1)
        pag.press('enter')

    elif isMatching(text, ['close', 'application']) or isMatching(text, ['close', 'window']):
        pag.hotkey('alt', 'f4')

    elif isMatching(text, ['screenshot']) or isMatching(text, ['screen', 'shot']):
        pag.press('printscreen')

# this scroll the window at current mouse position
    elif isMatching(text, ['scroll', 'down']):
        pag.scroll(-300)

# this scroll the window at current mouse position
    elif isMatching(text, ['scroll', 'up']):
        pag.scroll(300)


# enter the name of usb microphone that you found
# using lsusb
# the following name is only used as an example
# mic_name = "USB Device 0x46d:0x825: Audio (hw:1, 0)"

# Sample rate is how often values are recorded
sample_rate = 48000

# Chunk is like a buffer. It stores 1024 samples (bytes of data)
# here.
# (it is advisable to use powers of 2 such as 1024 or 2048)
chunk_size = 512
# Initialize the recognizer
r = sr.Recognizer()
r.energy_threshold = 300
r.dynamic_energy_threshold = False

# generate a list of all audio cards/microphones
# mic_list = sr.Microphone.list_microphone_names()

# the following loop aims to set the device ID of the mic that
# we specifically want to use to avoid ambiguity.
# for i, microphone_name in enumerate(mic_list):
#     if microphone_name == mic_name:
#         device_id = i

# use the microphone as source for input. Here, we also specify
# which device ID to specifically look for incase the microphone
# is not working, an error will pop up saying "device_id undefined"

shouldRun = True
while(shouldRun):
    # shouldRun = False

    with sr.Microphone(sample_rate=sample_rate,
                       chunk_size=chunk_size) as source:

        # print("Wait for noise recog")
        # wait for a second to let the recognizer adjust the
        # energy threshold based on the surrounding noise level
        # r.adjust_for_ambient_noise(source, duration=0.5)
        print("Say Something")

        # listens for the user's input
        audio = r.listen(source)
        print('------')

        # saving the record audio clip to a file
        # print(len(audio.get_wav_data()))
        # with open("audioFile.wav", "wb") as f:
        #     f.write(audio.get_wav_data())

        try:
            text = r.recognize_google(audio)
            print('======')
            print("you said: " + text)

            doAutomatedTask(text)

        # error occurs when google could not understand what was said

        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")

        except sr.RequestError as e:
            print(
                "Could not request results from Google Speech Recognition service {0}".format(e))