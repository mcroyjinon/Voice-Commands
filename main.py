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

def get_command(string, lookfor):
    for command in lookfor:
        if not command in string: continue
        return string[string.find(command)+len(command)+1:]

while True:
    config.read('config.ini')
    try:
        with speech_recognition.Microphone() as mic:
            recognizer.adjust_for_ambient_noise(mic,1)
            audio = recognizer.listen(mic)

            text = recognizer.recognize_google(audio)
            text = text.lower()

            if debug:
                print(text)

            if not text.startswith(('hey sylvia','sylvia')): continue

            print(f'Recognized call: {text}')

            if 'open' in text or 'run' in text:
                command = get_command(text,['open','run'])
                

            if 'search' in text:
                command = get_command(text,['search'])

            if 'shut down' in text:
                

    except Exception as e:
        print(e)
        recognizer = speech_recognition.Recognizer()
        continue