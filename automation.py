import pyautogui as pag
import speech_recognition as sr
import pyttsx3 as tts

# Initialize the recognizer
r = sr.Recognizer()

# Function to convert text to
# speech


def SpeakText(command):

    # Initialize the engine
    engine = tts.init()
    engine.say(command)
    engine.runAndWait()


# Loop infinitely for user to
# speak


while(1):

    # Exception handling to handle
    # exceptions at the runtime
    try:

        # use the microphone as source for input.
        with sr.Microphone() as source2:

            # wait for a second to let the recognizer
            # adjust the energy threshold based on
            # the surrounding noise level
            r.adjust_for_ambient_noise(source2, duration=0.5)

            # listens for the user's input
            audio2 = r.listen(source2)

            # Using ggogle to recognize audio
            MyText = r.recognize_google(audio2)
            MyText = MyText.lower()

            print("Did you say "+MyText)
            SpeakText(MyText)

    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))

    except sr.UnknownValueError:
        print("unknown error occured")

#############################################

# def goToSite(website):
#     pag.hotkey('alt', 'tab')
#     pag.hotkey('ctrl', 't')
#     pag.hotkey('ctrl', 'l')
#     pag.write(website, interval=0.1)
#     pag.press('enter')


# def openFileExplorer():
#     pag.hotkey('win', 'e')


# website = input("Enter website name: ")
# goToSite(website)

# print(pag.KEY_NAMES)
# pag.hotkey('fn', 'f9')
