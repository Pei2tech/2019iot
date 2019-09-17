#! /usr/bin/python3
#pip3 install RPi.GPIO

from tkinter import *
import RPi.GPIO as GPIO

import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate('/home/pi/Documents/raspberryfirebase-firebase-adminsdk-q4ht6-3282b25b5b.json')
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://raspberryfirebase.firebaseio.com/',
    'databaseAuthVariableOverride': None
})



def appInterface(window):    
    buttonText.set("ON")
    frame = Frame(window,borderwidth=2,relief=GROOVE);
    ledButton = Button(frame,textvariable = buttonText,padx=30,pady=10,command=userClick,width=10).pack(padx=40,pady=40);
    frame.pack(padx=10,pady=10);

def userClick():
    text = buttonText.get();
    if text == 'ON':
        buttonText.set('OFF')
        GPIO.output(25, GPIO.HIGH)
    else:
        buttonText.set('ON')
        GPIO.output(25, GPIO.LOW)
    
    

if __name__ == '__main__':
    GPIO.setmode(GPIO.BCM)
    GPIO.cleanup()
    GPIO.setwarnings(False)
    GPIO.setup(25, GPIO.OUT)
    
    app = Tk();
    buttonText = StringVar();
    app.title("LEDControl");
    #app.geometry("500x600");
    appInterface(window = app);
    app.mainloop();