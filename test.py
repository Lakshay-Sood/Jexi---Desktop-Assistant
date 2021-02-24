# Python 2.x program for Speech Recognition
import speech_recognition as sr
import pyautogui as pag
import time


keywordsFor = {
    # ================================== 1 == MEDIA ========================================
    'increase volume': [['increase', 'volume']],
    'decrease volume': [['decrease', 'volume']],
    'play/pause music': [['stop', 'music'], ['play', 'music'], ['pause', 'music']],
    'next song': [['next', 'song']],
    'previous song': [['previous', 'song']],

    # ================================== 2 == BROWSER ======================================
    'new tab': [['new', 'tab']],
    'close tab': [['close', 'tab']],
    'next tab': [['switch', 'tab'], ['next', 'tab']],
    'previous tab': [['previous', 'tab']],
    'new incognito window': [['open', 'incognito', 'window']],
    'browser history': [['browser', 'history']],
    'browser downloads': [['download'], ['downloads']],
    'refresh webpage': [['refresh']],
    'fullscreen': [['fullscreen']],
    'go back': [['go', 'back']],
    'go forward': [['go', 'forward']],

    # ================================== 3 == WINDOWS ======================================
    'next application': [['switch', 'application'], ['next', 'application']],
    'previous application': [['previous', 'application']],
    'task view': [['task', 'view']],
    'go to desktop': [['go', 'to', 'desktop'], ['minimise']],
    'file explorer': [['file', 'explorer'], ['this', 'PC']],
    'windows settings': [['settings'], ['setting']],
    'close application': [['close', 'application'], ['close', 'window']],
    'lock this pc': [['lock']],
    'task manager': [['task', 'manager']],
    'system properties': [['system', 'properties']],

    # ================================== 4 == TOOLS ======================================
    'custom screenshot': [['custom', 'screenshot']],
    'screenshot to clipboard': [['screenshot']],
    'scroll down': [['scroll', 'down']],
    'scroll up': [['scroll', 'up']],
    'scroll to top': [['scroll', 'top']],
    'scroll to bottom': [['scroll', 'bottom']],
    'zoom in': [['zoom', 'in']],
    'zoom out': [['zoom', 'out']],
    'take a selfie': [['selfie']],
    'date time': [['date'], ['time'], ['calendar']],

    'exit this python script': [['bye', 'bye', 'bye']]

}


def isMatching(text, keywordsList):
    text = text.split(' ')
    counter = 0
    for keywords in keywordsList:
        for word in text:
            if (word.lower() == keywords[counter].lower()):
                counter += 1
                if (counter == len(keywords)):
                    return True

    return False


######## pag.KEY_NAMES ###############################
['\t', '\n', '\r', ' ', '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
 ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '{', '|', '}', '~',
 'accept', 'add', 'alt', 'altleft', 'altright', 'apps', 'backspace', 'browserback', 'browserfavorites', 'browserforward', 'browserhome',
 'browserrefresh', 'browsersearch', 'browserstop', 'capslock', 'clear', 'convert', 'ctrl', 'ctrlleft', 'ctrlright',
 'decimal', 'del', 'delete', 'divide', 'down', 'end', 'enter', 'esc', 'escape', 'execute', 'f1', 'f10', 'f11', 'f12', 'f13', 'f14', 'f15', 'f16',
 'f17', 'f18', 'f19', 'f2', 'f20', 'f21', 'f22', 'f23', 'f24', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9', 'final', 'fn',
 'hanguel', 'hangul', 'hanja', 'help', 'home', 'insert', 'junja', 'kana', 'kanji', 'launchapp1', 'launchapp2', 'launchmail', 'launchmediaselect', 'left',
 'modechange', 'multiply', 'nexttrack', 'nonconvert', 'num0', 'num1', 'num2', 'num3', 'num4', 'num5', 'num6', 'num7', 'num8', 'num9', 'numlock',
 'pagedown', 'pageup', 'pause', 'pgdn', 'pgup', 'playpause', 'prevtrack', 'print', 'printscreen', 'prntscrn', 'prtsc', 'prtscr', 'return', 'right',
 'scrolllock', 'select', 'separator', 'shift', 'shiftleft', 'shiftright', 'sleep', 'space', 'stop', 'subtract', 'tab', 'up', 'volumedown', 'volumemute', 'volumeup',
 'win', 'winleft', 'winright', 'yen', 'command', 'option', 'optionleft', 'optionright']


def doAutomatedTask(recogText):

    # ================================== 1 == MEDIA begin ========================================
    if isMatching(recogText, keywordsFor['increase volume']):
        for i in range(10):
            pag.press('volumeup')

    elif isMatching(recogText, keywordsFor['decrease volume']):
        for i in range(10):
            pag.press('volumedown')

    elif isMatching(recogText, keywordsFor['play/pause music']):
        pag.press('playpause')

    elif isMatching(recogText, keywordsFor['next song']):
        pag.press('nexttrack')

    elif isMatching(recogText, keywordsList=['previous song']):
        pag.press('prevtrack')
# ================================== MEDIA end ========================================

# ================================== 2 == BROWSER begin ========================================
    elif isMatching(recogText, keywordsFor['new tab']):
        pag.hotkey('ctrl', 't')

    elif isMatching(recogText, keywordsFor['close tab']):
        pag.hotkey('ctrl', 'w')

    elif isMatching(recogText, keywordsFor['next tab']):
        pag.hotkey('ctrl', 'tab')

    elif isMatching(recogText, keywordsFor['previous tab']):
        pag.hotkey('ctrl', 'shift', 'tab')

    elif isMatching(recogText, keywordsFor['new incognito window']):
        pag.hotkey('ctrl', 'shift', 'n')

    elif isMatching(recogText, keywordsFor['go back']):
        # pag.hotkey('alt', 'left')
        pag.press('browserback')

    elif isMatching(recogText, keywordsFor['go forward']):
        # pag.hotkey('alt', 'right')
        pag.press('browserforward')

    elif isMatching(recogText, keywordsFor['browser history']):
        pag.hotkey('ctrl', 'h')

    elif isMatching(recogText, keywordsFor['browser downloads']):
        pag.hotkey('ctrl', 'j')

    elif isMatching(recogText, keywordsFor['refresh webpage']):
        pag.press('f5')

    elif isMatching(recogText, keywordsFor['fullscreen']):
        pag.press('f11')

    # extend this functionality to dynamically fetch string to be searched
    elif isMatching(recogText, [['browser', 'search', 'apple']]):
        pag.press('browsersearch')
        pag.write('apple')
        pag.press('enter')

    # extend this functionality to dynamically fetch website name
    elif isMatching(recogText, [['go', 'to', 'facebook.com']]):
        pag.hotkey('ctrl', 'l')
        pag.write('facebook.com')
        pag.press('enter')
# ================================== BROWSER ends ========================================

# ================================== 3 == WINDOWS begin ========================================
    elif isMatching(recogText, keywordsFor['next application']):
        pag.hotkey('alt', 'tab')

    elif isMatching(recogText, keywordsFor['previous application']):
        pag.hotkey('alt', 'shift', 'tab')

    elif isMatching(recogText, keywordsFor['task view']):
        pag.hotkey('win', 'tab')

    elif isMatching(recogText, keywordsFor['go to desktop']):
        pag.hotkey('win', 'd')

    elif isMatching(recogText, keywordsFor['file explorer']):
        pag.hotkey('win', 'e')

    elif isMatching(recogText, keywordsFor['windows settings']):
        pag.hotkey('win', 'i')

    # extend this functionality to dynamically fetch application name
    elif isMatching(recogText, [['open', 'application', 'word']]):
        pag.hotkey('win', 's')
        time.sleep(0.5)
        pag.write('word')
        time.sleep(0.2)
        pag.press('enter')

    elif isMatching(recogText, keywordsFor['close application']):
        pag.hotkey('alt', 'f4')

    # 💥💥 not working
    elif isMatching(recogText, keywordsFor['lock this pc']):
        print('doing it')
        pag.hotkey('win', 'l')

    # 💥💥 not working (failsafe error)
    elif isMatching(recogText, keywordsFor['task manager']):
        pag.hotkey('ctrl', 'shift', 'esc')
        time.sleep(1)
        pag.press('left')
        pag.press('enter')
        print('did do')

    elif isMatching(recogText, keywordsFor['system properties']):
        pag.hotkey('win', 'pause')

# F3: Search for a file or folder in File Explorer.
# virtual desktop and switching and closing (win + ctrl + D)
# ================================== WINDOWS ends ========================================

# ================================== 4 == VOICE FEEDBACK begin ========================================
# time
# date
# weather
# wikipedia search (library: wikipedia)
# movie review
# book review
# quotes
# stock prices
# cpu usage (os module)
# any other api
# ================================== VOICE FEEDBACK ends ========================================


# ================================== 5 == TOOLS begin ========================================
    elif isMatching(recogText, keywordsFor['custom screenshot']):
        pag.hotkey('win', 'shift', 's')

    elif isMatching(recogText, keywordsFor['screenshot to clipboard']):
        pag.press('printscreen')

    # this scroll the window at current mouse position
    elif isMatching(recogText, keywordsFor['scroll down']):
        pag.scroll(-400)    # these many pixels

    # this scroll the window at current mouse position
    elif isMatching(recogText, keywordsFor['scroll up']):
        pag.scroll(400)

    # this scroll the window at current mouse position
    elif isMatching(recogText, keywordsFor['scroll to top']):
        pag.hotkey('ctrl', 'home')

    # this scroll the window at current mouse position
    elif isMatching(recogText, keywordsFor['scroll to bottom']):
        pag.hotkey('ctrl', 'end')

    elif isMatching(recogText, keywordsFor['zoom in']):
        pag.hotkey('ctrl', '+')

    elif isMatching(recogText, keywordsFor['zoom out']):
        pag.hotkey('ctrl', '-')

    elif isMatching(recogText, keywordsFor['take a selfie']):
        pag.hotkey('win', 's')
        time.sleep(0.5)
        pag.write('camera')
        pag.press('enter')
        time.sleep(1.5)
        pag.press('space')

    # add VOICE feedback too
    elif isMatching(recogText, keywordsFor['date time']):
        pag.hotkey('win', 'alt', 'd')
        time.sleep(3)
        pag.hotkey('win', 'alt', 'd')


# right click on taskbar
# ================================== TOOLS ends ========================================

# ================================== 6 == BASIC CALCULATOR command ========================================
# with voice feedback
# ================================== BASIC CALCULATOR ends ========================================

################## ADD   H I N D I   SUPPORT #########################################################

# ================================== 7 == EXIT command ========================================
    elif isMatching(recogText, keywordsFor['exit this python script']):
        exit(1)


# enter the name of usb microphone that you found
# using lsusb
# the following name is only used as an example
# mic_name = "USB Device 0x46d:0x825: Audio (hw:1, 0)"

# Sample rate is how often values are recorded
sample_rate = 48000

# Chunk is like a buffer. It stores 512 samples (bytes of data) here.
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
    # uncomment below statement to run loop only once
    # shouldRun = False

    with sr.Microphone(sample_rate=sample_rate,
                       chunk_size=chunk_size) as source:

        # print("Wait for dynamic noise recog")
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
