import speech_recognition as sr
from time import ctime
import time
import webbrowser
import playsound
import os
import random
from gtts import gTTS


speech_recognizer = sr.Recognizer()


def record_audio(ask = False):
    with sr.Microphone() as source:
        if ask:
            robot_speak(ask)
        audio = speech_recognizer.listen(source)
        voice_data = ''
        try:
            voice_data = speech_recognizer.recognize_google(audio)
        except sr.UnknownValueError:
            robot_speak("Sorry, can you speak clearly")
        except sr.RequestError:
            robot_speak("Sorry, speech service currently down")

        return voice_data

def robot_speak(audio_string):
    tts = gTTS(text=audio_string, lang='en')
    r = random.randint(1, 1000000)
    audio_file = 'audio-' + str(r) + '.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    robot_speak(audio_file)
    os.remove(audio_file)

def respond(voice_data):
    if 'what is your name' in voice_data:
        robot_speak("My name is Abiola")
    if 'what time is it now' in voice_data:
        robot_speak("Time now is " + ctime())
    if 'search' in voice_data:
        search = record_audio('What do you want to search for?')
        url = 'https://google.com/search?q=' + search
        webbrowser.get().open(url)
        robot_speak('Here is what I found for ' + search)
    if 'find location' in voice_data:
        location = record_audio('What is the location?')
        url = 'https://google.nl/maps/place/' + location + '/&amp;'
        webbrowser.get().open(url)
        robot_speak('Here is the location of ' + location)
    if 'exit' in voice_data:
        exit()


time.sleep(1)
robot_speak("How can I help you:")
while 1:
    voice_data = record_audio()
    respond(voice_data)
