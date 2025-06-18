import os
import pyttsx3
import time
from pynput.keyboard import Key, Controller
import webbrowser

tts = pyttsx3.init()
tts.setProperty('voice','HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Speech\\Voices\\Tokens\\TTS_MS_JA-JP_HARUKA_11.0')

keyboard = Controller()

commands = {}

def open_roblox_game(**kwargs):
    roblox_games = kwargs['config']['roblox games']

    for game, id in roblox_games.items():
        if game in kwargs['param']:
            webbrowser.open(f'roblox://placeId={id}')
            tts.say(f'Opening Roblox Game: {game}')
            tts.runAndWait()
commands['open roblox game'] = open_roblox_game

def open_application(**kwargs):

    desktop = os.listdir(f'c:\\Users\\{kwargs['USER']}\\Desktop')
    directories = dict(kwargs['config']['applications'])

    for app in desktop:
        if app.split('.')[0].lower() in kwargs['param']:
            os.startfile(f'c:\\Users\\{kwargs['USER']}\\Desktop\\{app}')
            tts.say(f'Opening {app}')
            tts.runAndWait()
            break
    else:
        for app in directories.keys():
            if app in kwargs['param']:
                os.startfile(directories[app])
                tts.say(f'Opening {app}')
                tts.runAndWait()
commands['open'] = open_application
commands['run'] = open_application


def web_search(**kwargs):
    webbrowser.open_new_tab(f'https://www.google.com/search?q={kwargs['param']}')
commands['search'] = web_search


def shutdown(**kwargs):
    os.system('shutdown /s /t 1')
commands['shut down'] = shutdown
