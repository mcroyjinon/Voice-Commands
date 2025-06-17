import os
import pyttsx3

tts = pyttsx3.init()
tts.setProperty('voice','HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Speech\\Voices\\Tokens\\TTS_MS_JA-JP_HARUKA_11.0')

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