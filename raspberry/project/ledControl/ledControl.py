from tkinter import *
import RPi.GPIO as GPIO



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