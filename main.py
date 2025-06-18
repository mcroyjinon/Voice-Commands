import speech_recognition
import pyttsx3
import os
from configparser import ConfigParser
from pynput.keyboard import Key, Controller
import time
from commands import commands

recognizer = speech_recognition.Recognizer()
tts = pyttsx3.init()
tts.setProperty('voice','HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Speech\\Voices\\Tokens\\TTS_MS_JA-JP_HARUKA_11.0')

keyboard = Controller()
config = ConfigParser()

debug = False
USER = 'nealm'

def get_command(string, lookfor):
    if not lookfor in string: return
    return string[string.find(lookfor)+len(lookfor)+1:]

while True:
    config.read('config.ini')
    try:
        with speech_recognition.Microphone() as mic:
            recognizer.adjust_for_ambient_noise(mic,0.2)
            audio = recognizer.listen(mic)

            text = recognizer.recognize_google(audio)
            text = text.lower()

            if debug:
                print(text)

            if not text.startswith(('hey sylvia','sylvia')): continue

            output = f'Recognized call: {text}'
            print(output)

            for command in commands.keys():
                if command in text:
                    param = get_command(text, command)
                    commands[command](param=param, config=config, USER=USER)
                    break
            else: 
                if'debug' in text:
                    debug = True
                    tts.say(f'Debug is now {debug}')
                    tts.runAndWait()
    except Exception as e:
        print(e)
        recognizer = speech_recognition.Recognizer()
        continue