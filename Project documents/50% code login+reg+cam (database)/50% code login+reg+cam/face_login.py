'''Note:install this version in enviorment
   pip3 install opencv-contrib-python==4.6.0.66
   pip3 install opencv==4.6.0'''
   
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


flag=0
recognizer = cv2.face_LBPHFaceRecognizer.create()
#cv2.face.LBPHFaceRecognizer_create()
#    recognizer = cv2.face.FisherFaceRecognizer(0, 3000);

recognizer.read('trainingdata.yml')
cascadePath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascadePath);
font = cv2.FONT_HERSHEY_SIMPLEX
    #iniciate id counter
id = 0
    # names related to ids: example ==> Marcelo: id=1,  etc
    #names = ['None', 'Criminal person identified', 'Missing person', 'Criminal person identified', 'Criminal person identified', 'Missing person','Missing person'] 
    # Initialize and start realtime video capture
cam = cv2.VideoCapture(0)
cam.set(3, 640) # set video widht
cam.set(4, 480) # set video height
    # Define min window size to be recognized as a face
minW = 0.1*cam.get(3)
minH = 0.1*cam.get(4)
    
while True:
        ret, img =cam.read()
#        img = cv2.flip(img, -1) # Flip vertically

        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        faces=faceCascade.detectMultiScale(gray,1.3,8,minSize = (int(minW), int(minH)))
#        faces = faceCascade.detectMultiScale( 
#            gray,
#            scaleFactor = 1.2,
#            minNeighbors = 5,
#            minSize = (int(minW), int(minH)),
#           )
        for(x,y,w,h) in faces:
            cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)
            id, confidence = recognizer.predict(gray[y:y+h,x:x+w])
            
            # If confidence is less them 100 ==> "0" : perfect match
            
            if (confidence < 60):
                #print(id)
                #name = names[id]
                id = id
                
                print(type(id))
                
                #
                #id = names[id]
                confidence = "  {0}%".format(round(100 - confidence))
                
                         
                cv2.putText(img,str(id),(x+5,y-5),font,1,(255,255,255),2)
                cv2.putText(img,str(confidence),(x+5,y+h-5),font,1,(255,255,0),1)
                # my_conn = sqlite3.connect('face.db')
                # r_set=my_conn.execute("select * from User where id =" + str(id) +"");
                # i=0 # row value inside the loop 
                # for student in r_set: 
                # for j in range(len(student)):
                #         e =tk.Entry(frame_display, width=10, fg='blue') 
                #         e.grid(row=i, column=j) 
                #         e.insert(END, student[j])
                #     i=i+1
                
                cam.release()  
                
                TTS = gTTS(text='Authenticated User...login successfuly...... welcome new page')     
                    
                TTS.save("voice.mp3")
                os.system("voice.mp3")
                
                # r = sr.Recognizer()
                # print("Please talk")
                # with sr.Microphone() as source:        
                # #     # read the audio data from the default microphone
                #      audio_data = r.record(source, duration=10)
                #      print(audio_data)
                    
                              
                # print("Recognizing...")
                # #     # convert speech to text
                # text = r.recognize_google(audio_data)
                # if  text == 'ok': 
                #     from subprocess import call
                #     call(["python", "voice.py"])
                 
                         
               
            else:
#                print(confidence)
                id = "unknown Person Identified"
                confidence = "  {0}%".format(round(100 - confidence))
                
                cv2.putText(img,str(id),(x+5,y-5),font,1,(255,255,255),2)
                cv2.putText(img,str(confidence),(x+5,y+h-5),font,1,(255,255,0),1)  
                
                cam.release() 
                
                TTS = gTTS(text='Unauthenticated User...close......')     
                    
                TTS.save("voice.mp3")
                os.system("voice.mp3")
               # l = Label(frame_display1, text = "Ooops!!!!!....Unauthenticated User..") 
               # l.config(font =("Courier", 25,"bold"),fg= 'red4') 
                #l.place(x=330,y=400)
                #l.pack() 
                print('Ooops!!!!!....Unauthenticated User..')
               

#        time.sleep(0.2)
        cv2.imshow('camera',img) 
#        print(flag)
        if flag==10:
            flag=0
        if cv2.waitKey(1) == ord('Q'):
            break

cam.release()
cv2.destroyAllWindows()
            

     
        # k = cv2.waitKey(10) & 0xff # Press 'ESC' for exiting video
#        if k == 27:
#            break
        

