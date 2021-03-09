# THE MAIN FILE TO RUN FOR DESKTOP AUTOMATION

# imports
from os import cpu_count
import speech_recognition as sr
import pyautogui as pag  # for key presses
import pyttsx3  # text-to-speech
import time  # for delays, sleep()
import datetime  # for fetching current date, time
import psutil   # for current cpu, ram usage
import requests  # http library
import json  # to work with json data
import wikipedia  # to do quick wikipedia search


keywordsFor = {
    # ================================== 0 == Assistant Tools ========================================
    'ignore this statement': [['ignore'], ['forget', 'it']],

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
    'go back': [['go', 'back'], ['come', 'back']],
    'go forward': [['go', 'forward']],
    'browser history': [['browser', 'history']],
    'browser downloads': [['download'], ['downloads']],
    'refresh webpage': [['refresh']],
    'fullscreen': [['fullscreen']],

    # ================================== 3 == WINDOWS ======================================
    'next application': [['switch', 'application'], ['next', 'application']],
    'previous application': [['previous', 'application']],
    'task view': [['task', 'view']],
    'go to desktop': [['go', 'to', 'desktop'], ['minimise']],
    'file explorer': [['file', 'explorer'], ['this', 'PC']],
    'file folder search': [['file', 'search'], ['folder', 'search'], ['search', 'file'], ['search', 'folder']],
    'windows settings': [['settings'], ['setting']],
    'close application': [['close', 'application'], ['close', 'window']],
    'lock this pc': [['lock']],
    'task manager': [['task', 'manager']],
    'system properties': [['system', 'properties']],

    # ================================== 4 == VOICE FEEDBACK begin =================================
    'joke': [['joke']],
    'weather': [['weather']],
    'wikipedia search': [['wikipedia', 'search']],
    # added 'court' cuz of Speech recog api limitations
    'quote': [['quote'], ['court']],
    'cpu ram usage': [['cpu'], ['ram'], ['memory']],

    # ================================== 5 == TOOLS ======================================
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
    'task view': [['task'], ['view']],

    'exit this python script': [['bye', 'bye', 'bye']]

}


def isMatching(text, keywordsList):
    text = text.split(' ')
    for keywords in keywordsList:
        counter = 0
        for word in text:
            if (word.lower() == keywords[counter].lower()):
                counter += 1
                if (counter == len(keywords)):
                    return True

    return False


def getJoke(category='general'):
    # 3 categoties: general, programming, knock-knock
    url = r"https://official-joke-api.appspot.com/jokes/{}/random".format(
        category)

    response = requests.get(url)
    joke = json.loads(response.text)[0]

    tts.setProperty('rate', 150)
    tts.say(joke['setup'])
    tts.say(joke['punchline'])
    tts.runAndWait()
    tts.setProperty('rate', 200)


def getWeather(complete=False):
    # weather API documentation: https://openweathermap.org/current
    # fetching weather for 'Delhi' (with api key '57611d1e87cbe8e4d1698088119b87d3')
    url = r'http://api.openweathermap.org/data/2.5/weather?appid=57611d1e87cbe8e4d1698088119b87d3&units=metric&q=Delhi'

    response = requests.get(url)
    weather = response.json()

    # won't be a problem at we are statically defining our city
    if weather['cod'] == '404':
        print('city not found')
    else:
        tts.say('It\'s {} degree celcius.'.format(weather['main']['temp']))
        tts.say('{} expected.'.format(weather['weather'][0]['description']))

        if complete:
            tts.say('Also, humidity is {} %.'.format(
                weather['main']['humidity']))
            tts.say('And minimum and maximum temperatures are {} and {} degree celcius respectively.'.format(
                weather['main']['temp_min'], weather['main']['temp_max']))

        tts.runAndWait()


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

    # ================================== 0 == Assistant Tools ========================================
    if isMatching(recogText, keywordsFor['ignore this statement']):
        pass
    # ================================== 0 == Assistant Tools end ========================================

    # ================================== 1 == MEDIA begin ========================================
    elif isMatching(recogText, keywordsFor['increase volume']):
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

    # ✨✔ NOW: extend this functionality to dynamically fetch string to be searched
    elif isMatching(recogText, [['browser', 'search']]):
        target = recogText.split('search')[1].strip()
        if target.find('for') == 0:
            target = target[4:]

        pag.press('browsersearch')
        pag.write(target)
        pag.press('enter')

    # ✨✔ NOW: extend this functionality to dynamically fetch website name
    elif isMatching(recogText, [['go', 'to']]):
        if (recogText.find('desktop') != -1):
            pag.hotkey('win', 'd')

        target = recogText.split('go to')[1].strip()

        pag.hotkey('ctrl', 'l')
        pag.write(target)
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

    elif isMatching(recogText, keywordsFor['file folder search']):
        target = recogText.split('search')[1]
        target = target.replace('file', '').replace(
            'folder', '').replace('search', '').replace('for', '').strip()

        # open file explorer and go to This PC
        pag.hotkey('win', 'e')
        time.sleep(0.5)
        pag.hotkey('alt', 'up')
        time.sleep(0.5)
        pag.press('down')
        pag.press('enter')
        time.sleep(0.5)

        # search for the target string
        pag.press('f3')
        time.sleep(0.8)
        pag.write(target)
        time.sleep(0.5)
        pag.press('enter')

    elif isMatching(recogText, keywordsFor['windows settings']):
        pag.hotkey('win', 'i')

    # ✨✔ NOW: extend this functionality to dynamically fetch application name
    elif isMatching(recogText, [['open', 'application']]):
        target = recogText.split('application')[1].strip()

        pag.hotkey('win', 's')
        time.sleep(0.5)
        pag.write(target)
        time.sleep(0.2)
        pag.press('enter')

    elif isMatching(recogText, keywordsFor['close application']):
        pag.hotkey('alt', 'f4')

    # 💥💥 not working (probably some permission error)
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

# virtual desktop (win + ctrl + D) and switching (win + ctrl + left/right) and closing (win + ctrl + F4)
# powershell (win+X : then I(normal) or A(admin rights) )
# ================================== WINDOWS ends ========================================

# ================================== 4 == VOICE FEEDBACK begin ========================================
    elif isMatching(recogText, keywordsFor['joke']):
        if recogText.find('programming') != -1:
            getJoke('programming')
        elif recogText.find('knock knock') != -1:
            getJoke('knock-knock')
        else:
            getJoke()

    elif isMatching(recogText, keywordsFor['weather']):
        if recogText.find('complete') != -1:
            getWeather(complete=True)
        else:
            getWeather()

    elif isMatching(recogText, keywordsFor['wikipedia search']):
        target = recogText.split('search')[1].strip()
        if target.find('for') == 0:
            target = target[4:]
        try:
            result = wikipedia.summary(target, sentences=2)
            print(result)
            tts.say(result)
            tts.runAndWait()
        except:
            tts.say('Unable to do a search. Try searching through a browser.')
            tts.runAndWait()
            # can add a feature where we ask user in case of DisambiguationError
            # except wikipedia.exceptions.DisambiguationError as e:
            #   print e.options
            #  output => [u'Mercury (mythology)', u'Mercury (planet)', u'Mercury (element)', u'Mercury, Nevada', ...]

    elif isMatching(recogText, keywordsFor['quote']):
        url = 'https://api.forismatic.com/api/1.0/?method=getQuote&lang=en&format=json'
        response = requests.get(url)
        quote = response.json()
        print(quote['quoteText'])
        tts.say(quote['quoteText'])
        tts.runAndWait()

    elif isMatching(recogText, keywordsFor['cpu ram usage']):
        # Calling psutil.cpu_precent() for 2 seconds
        cpuPercent = psutil.cpu_percent(2)
        print('CPU usage is: {}%'.format(cpuPercent))
        tts.say('CPU usage is: {}%'.format(cpuPercent))

        # Getting % usage of virtual_memory (3rd field)
        ramPercent = psutil.virtual_memory()[2]
        print('and RAM usage is: {} %:'.format(ramPercent))
        tts.say('and RAM usage is: {} %:'.format(ramPercent))
        tts.runAndWait()

# movie review
# book review
# stock prices
# any other api
# ================================== VOICE FEEDBACK ends ========================================


# ================================== 5 == TOOLS begin ========================================
    elif isMatching(recogText, keywordsFor['custom screenshot']):
        pag.hotkey('win', 'shift', 's')

    elif isMatching(recogText, keywordsFor['screenshot to clipboard']):
        pag.press('printscreen')
        tts.say('Done.')
        tts.runAndWait()

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

    # ✨✔ add VOICE feedback too
    elif isMatching(recogText, keywordsFor['date time']):
        today = datetime.datetime.today()
        askedForDate = False
        if (recogText.find('date') != -1):
            tts.say('today is {}'.format(today.strftime('%x')))
            askedForDate = True

        if (recogText.find('time') != -1):
            if askedForDate:
                tts.say('And')
            # 12-hour format
            tts.say('It\'s {} {} {}'.format(
                today.strftime('%I').lstrip('0'), today.strftime('%M').lstrip('0'), today.strftime('%p')))
            # 24-hour format
            # tts.say('It\'s {} hours, {} minutes.'.format(
            #     today.strftime('%H'), today.strftime('%M')))

        pag.hotkey('win', 'alt', 'd')
        tts.runAndWait()
        time.sleep(1)
        pag.hotkey('win', 'alt', 'd')

    elif isMatching(recogText, keywordsFor['task view']):
        pag.hotkey('win', 'tab')


# right click on taskbar
# ================================== TOOLS ends ========================================

# ================================== 6 == BASIC CALCULATOR command ========================================
# with voice feedback
# ================================== BASIC CALCULATOR ends ========================================

##################  💥💥 ADD   H I N D I   SUPPORT  💥💥  #########################################################

# ================================== 7 == EXIT command ========================================
    elif isMatching(recogText, keywordsFor['exit this python script']):
        tts.say('Was nice to see you. Byeeeee.')
        tts.runAndWait()
        exit(1)


# ================================== STARTING POINT OF THE PROGRAM ========================================
# ================================== STARTING POINT OF THE PROGRAM ========================================
# ================================== STARTING POINT OF THE PROGRAM ========================================


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
r.energy_threshold = 600
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


tts = pyttsx3.init()
# ✨ STARTUP VOICE MESSAGE
# tts.say('Your desktop assistant is up and running.')
# tts.setProperty('rate', 300)
# tts.say('Let\'s go!')
# tts.setProperty('rate', 200)  # 200 is the default rate (words per minute)
# tts.runAndWait()

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

        # saving the recorded audio clip to a file
        # print(len(audio.get_wav_data()))
        # with open("audioFile.wav", "wb") as f:
        #     f.write(audio.get_wav_data())

        try:
            text = r.recognize_google(audio)
            print('======')
            print("you said: " + text)

            text = text.lower()
# 💥💥 concatenate instructions using "AND"
            # text = text.split('and')
            # text.forEach(command => {
            #     doAutomatedTask(command)
            # })
            doAutomatedTask(text)

        # error occurs when google could not understand what was said

        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")

        except sr.RequestError as e:
            print(
                "Could not request results from Google Speech Recognition service {0}".format(e))
