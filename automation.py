import pyautogui as pag


def goToSite(website):
    pag.hotkey('alt', 'tab')
    pag.hotkey('ctrl', 't')
    pag.hotkey('ctrl', 'l')
    pag.write(website, interval=0.1)
    pag.press('enter')


def openFileExplorer():
    pag.hotkey('win', 'e')


website = input("Enter website name: ")
goToSite(website)

# print(pag.KEY_NAMES)
# pag.hotkey('fn', 'f9')
