import os
import pyttsx3
import time
from pynput.keyboard import Key, Controller

tts = pyttsx3.init()
tts.setProperty('voice','HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Speech\\Voices\\Tokens\\TTS_MS_JA-JP_HARUKA_11.0')

keyboard = Controller()

commands = {}


def open_application(command, config, USER):

    desktop = os.listdir(f'c:\\Users\\{USER}\\Desktop')
    directories = dict(config['applications'])

    for app in desktop:
        if app.split('.')[0].lower() in command:
            os.startfile(f'c:\\Users\\{USER}\\Desktop\\{app}')
            tts.say(f'Opening {app}')
            tts.runAndWait()
            break
    else:
        for app in directories.keys():
            if app in command:
                os.startfile(directories[app])
                tts.say(f'Opening {app}')
                tts.runAndWait()
commands['open'] = open_application
commands['run'] = open_application


def web_search(command, USER):
    os.startfile(f'c:\\Users\\{USER}\\Desktop\\Opera GX Browser.lnk')
    time.sleep(3)
    keyboard.type(command)
    keyboard.press(Key.enter)
commands['search'] = web_search


def shutdown():
    os.system('shutdown /s /t 1')
commands['shut down'] = shutdown