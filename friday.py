import speech_recognition as sr
import requests
import json
from gtts import gTTS
import pyaudio
import os
import pygame
import time

# Set up voice recognition
recognizer = sr.Recognizer()
microphone = sr.Microphone()

# Get the directory of the current script
script_dir = os.path.dirname(os.path.abspath(__file__))

def recognize_voice_input():
    with microphone as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        return recognizer.recognize_google(audio)
    except sr.UnknownValueError:
        print("Could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
        
def text_to_audio(response_text):
    speech = gTTS(text = response_text, lang="en", slow=False, tld="com.au")
    speech.save("sounds/friday.mp3")
    file_path = os.path.join(script_dir, 'sounds', 'friday.mp3')
    # playsound(file_path)
    pygame.init()
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()
    pygame.event.wait()

def send_request_to_board_ai(text_input):
    print('text_input->'+text_input)
    headers = {
       "Content-Type": "application/json"
    }

    data = {
        "prompt": { "text" : text_input}
    }

    response = requests.post("https://generativelanguage.googleapis.com/v1beta3/models/text-bison-001:generateText?key={YOUR_API_KEY}", headers=headers, data=json.dumps(data))

    if response.status_code == 200:
        response_json = json.loads(response.text)
        # print('response.text->'+response.text)
        if "filters" in response_json:
            return "Something wrong, can you try again"
        else:
            print('response->'+response_json["candidates"][0]["output"])
            return response_json["candidates"][0]["output"]
    else:
        print("Error calling Board AI API: " + str(response.status_code))
        return "No result"

def fridayAI():
    while True:
        print("Ask something:")
        # Recognize the user's voice input
        text_input = recognize_voice_input()
        
        if text_input:
            print('input: '+text_input)
            # Send the text input to the Board AI API
            response_text = send_request_to_board_ai(text_input)

            if response_text:
                print('answer: '+response_text)
                text_to_audio(response_text)
            else:
                print("Error generating response from Board AI")
                text_to_audio("Can you come again")
                
        else:
            print("No voice input detected")
    

def activateFridayAI():
    print("Say something...")
    text_input = recognize_voice_input()
    print(text_input)
    if text_input == 'Friday':
        text_to_audio("Hi krishnam, How will you eat my valueable time today")
        time.sleep(4)
        fridayAI()
    else:
        print("You are not authorized")

activateFridayAI()