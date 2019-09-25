from tkinter import *
from gpiozero import Buzzer
from threading import Timer
import RPi.GPIO as GPIO

class App:
    def __init__(self,window):
        #buzzer button
        buzzerFrame = Frame(window);
        Button(buzzerFrame,text="Buzzer Control", padx=10, pady=10,command=self.userClickBuzzer).pack(padx=30,pady=10);
        buzzerFrame.pack();
        
        #buzzer init
        #self.buzzer = Buzzer(16);
        GPIO.setwarnings(False);
        GPIO.setmode(GPIO.BCM);
        GPIO.setup(16,GPIO.OUT);
        
        
        self.buzzer = GPIO.PWM(16, 50);
        
        
    def userClickBuzzer(self):
        print("user click");
        self.buzzer.start(100);
        t = Timer(0.3,self.closeBuzzer);
        t.start();
        #self.buzzer.on();
        
    
    def closeBuzzer(self):
        self.buzzer.stop();

if __name__ == "__main__":
    root = Tk();
    root.title("RFID_LCD_BUZZER");
    root.option_add("*font",("verdana", 18, "bold"));
    root.option_add("*background", "gold");
    root.option_add("*forground","#888888");
    app = App(root);
    root.mainloop();