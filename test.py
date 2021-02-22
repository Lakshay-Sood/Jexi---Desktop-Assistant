# Python 2.x program for Speech Recognition
import speech_recognition as sr
import pyautogui as pag
import time


def doAutomatedTask(text):
    if text == 'increase volume':
        for i in range(10):
            pag.press('volumeup')

    if text == 'decrease volume':
        for i in range(10):
            pag.press('volumedown')

    if text == 'music stop' or text == 'music play':
        pag.press('playpause')

    if text == 'next song':
        pag.press('nexttrack')

    elif text == 'switch application':
        pag.hotkey('alt', 'tab')

    elif text == 'open new tab':
        pag.hotkey('ctrl', 't')

    elif text == 'close this tab':
        pag.hotkey('ctrl', 'w')

    elif text == 'go to facebook.com':
        pag.hotkey('ctrl', 'l')
        pag.write('facebook.com')
        pag.press('enter')

    elif text == 'open application word':
        pag.press('win')
        pag.write('word')
        time.sleep(1)
        pag.press('enter')

    elif text == 'close this application':
        pag.hotkey('alt', 'f4')


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
while(1):

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
