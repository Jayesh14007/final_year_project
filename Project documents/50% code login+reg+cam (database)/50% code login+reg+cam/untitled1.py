import tkinter as tk
# from tkinter import *
from tkinter import messagebox as ms
import sqlite3
from PIL import Image, ImageTk
import re
import random
import speech_recognition as sr
import time
from playsound import playsound
from translate import Translator
import os
from gtts import gTTS
import cv2


# Database connection and creation
def create_db():
    conn = sqlite3.connect('user_data.db')
    cursor = conn.cursor()
    
    # Create table if it doesn't exist
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        first_name TEXT,
                        last_name TEXT,
                        username TEXT,
                        user_id TEXT)''')
    
    conn.commit()
    conn.close()

def insert_user(first_name, last_name, username, user_id):
    conn = sqlite3.connect('user_data.db')
    cursor = conn.cursor()
    
    cursor.execute("INSERT INTO users (first_name, last_name, username, user_id) VALUES (?, ?, ?, ?)",
                   (first_name, last_name, username, user_id))
    
    conn.commit()
    conn.close()


global translation11, translation1

# Create the database and table
create_db()

TTS = gTTS(text='Welcome to your Blind Email Registration. Speak Your First name')
TTS.save("voice.mp3")
os.system("voice.mp3")

try:
    r = sr.Recognizer()
    print("Please talk")
    with sr.Microphone() as source:
        audio_data = r.record(source, duration=10)
        print("Recognizing...")
        text = r.recognize_google(audio_data)
        print("First Name is: " + text)
        first_name = text  # Store the first name for the database
        translator = Translator(from_lang="English", to_lang="English")
        translation1 = translator.translate(text)
        TTS = gTTS(text=translation1)
        TTS.save("voice.mp3")
        os.system("voice.mp3")
        time.sleep(3)

    TTS = gTTS(text='Speak Your Last Name')
    TTS.save("voice.mp3")
    os.system("voice.mp3")
    time.sleep(3)
    r = sr.Recognizer()
    print("Please talk")
    with sr.Microphone() as source:
        audio_data = r.record(source, duration=10)
        print("Recognizing...")
        text = r.recognize_google(audio_data)
        print("Last Name is: " + text)
        last_name = text  # Store the last name for the database
        translator = Translator(from_lang="English", to_lang="English")
        translation1 = translator.translate(text)
        TTS = gTTS(text=translation1)
        TTS.save("voice.mp3")
        os.system("voice.mp3")
        time.sleep(3)

    TTS = gTTS(text='Please Say Your Username')
    TTS.save("voice.mp3")
    os.system("voice.mp3")
    time.sleep(3)
    r = sr.Recognizer()
    print("Please talk")
    with sr.Microphone() as source:
        audio_data = r.record(source, duration=10)
        print("Recognizing...")
        text = r.recognize_google(audio_data)
        print("Username is: " + text)
        username = text  # Store the username for the database
        translator = Translator(from_lang="English", to_lang="English")
        translation1 = translator.translate(text)
        TTS = gTTS(text=translation1)
        TTS.save("voice.mp3")
        os.system("voice.mp3")
        time.sleep(3)

    TTS = gTTS(text='Please enter your user ID, for example, 1 2 3')
    TTS.save("voice.mp3")
    os.system("voice.mp3")
    time.sleep(5)
    r = sr.Recognizer()
    print("Please talk")
    with sr.Microphone() as source:
        audio_data = r.record(source, duration=10)
        print("Recognizing...")
        user_id = r.recognize_google(audio_data)
        print("User ID is: " + user_id)
        
        if user_id.lower()=="one" or user_id.lower()=="one one" or user_id=="1":
            user_id="1"
            print(user_id)
        if user_id.lower()=="two" or user_id.lower()=="two two" or user_id=="2" or user_id.lower()=="to" or user_id.lower()=="too":
            user_id="2"
            print(user_id)
        if user_id.lower()=="three" or user_id.lower()=="three three" or user_id=="3":
            user_id="3"
            print(user_id)
        if user_id.lower()=="four" or user_id.lower()=="four four" or user_id=="4":
             user_id="4"
             print(user_id)
        if user_id.lower()=="five" or user_id.lower()=="five five" or user_id=="5":
             user_id="5"
             print(user_id)
        
        translator = Translator(from_lang="English", to_lang="English")
        translation1 = translator.translate(user_id)
        TTS = gTTS(text=translation1)
        TTS.save("voice.mp3")
        os.system("voice.mp3")
        time.sleep(3)

    

    TTS = gTTS(text='Do you want to capture your photo?')
    TTS.save("voice.mp3")
    os.system("voice.mp3")
    time.sleep(3)
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio_data = r.record(source, duration=10)
        text = r.recognize_google(audio_data)
        if text.lower() == 'yes':
            TTS = gTTS(text='Camera is Open and capture images')
            TTS.save("voice.mp3")
            os.system("voice.mp3")
            time.sleep(3)
            face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
            cap = cv2.VideoCapture(0)
            sampleN = 0
            while True:
                ret, img = cap.read()
                gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                faces = face_cascade.detectMultiScale(gray, 1.3, 5)
                for (x, y, w, h) in faces:
                    sampleN += 1
                    cv2.imwrite(f"Image/User.{user_id}.{sampleN}.jpg", gray[y:y+h, x:x+w])
                    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
                    cv2.waitKey(100)
                cv2.imshow('img', img)
                cv2.waitKey(1)
                if sampleN > 40:
                    break
            cap.release()
            cv2.destroyAllWindows()

    TTS = gTTS(text='Do you want to train your photo?')
    TTS.save("voice.mp3")
    os.system("voice.mp3")
    time.sleep(3)
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio_data = r.record(source, duration=10)
        text = r.recognize_google(audio_data)
        if text.lower() == 'yes':
            TTS = gTTS(text='Training Start')
            TTS.save("voice.mp3")
            os.system("voice.mp3")
            time.sleep(3)
            from subprocess import call
            call(["python", "train.py"])
            # Insert user data into the database
            insert_user(first_name, last_name, username, user_id)

            TTS = gTTS(text='Registration Successful. Welcome to the Login Page')
            TTS.save("voice.mp3")
            os.system("voice.mp3")
            from subprocess import call
            call(["python", "face_login.py"])
        else :
            print("Unsuccessfully, Data is Not trained")

except sr.UnknownValueError:
    TTS = gTTS(text='Google Speech Recognition could not understand audio.')
    TTS.save("voice1.mp3")
    os.system("voice1.mp3")
    print("Google Speech Recognition could not understand audio.")

except sr.RequestError as e:
    TTS = gTTS(text=f'Could not request results from Google Speech Recognition service; {e}')
    TTS.save("voice.mp3")
    os.system("voice.mp3")
    print(f"Could not request results from Google Speech Recognition service; {e}")
