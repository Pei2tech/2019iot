from tkinter import *
from threading import Timer
import RPi.GPIO as GPIO
import mfrc522 as MFRC522

class App:
    def __init__(self,window):
        #buzzer frame button
        buzzerFrame = Frame(window);
        Button(buzzerFrame,text="Buzzer Control", padx=10, pady=10,command=self.userClickBuzzer).pack(expand=YES, fill=BOTH,padx=30,pady=10);
        buzzerFrame.pack(expand=YES, fill=BOTH);
        
        #lcd frame
        lcdFrame = Frame(window);
        self.entryString1 = StringVar();
        self.entryString2 = StringVar();
        
        #grid
        #entry1Frame
        
        Label(lcdFrame,text="name").grid(row=0, column=0, sticky=W);
        Entry(lcdFrame,textvariable=self.entryString1,width=16).grid(row=0, column=1, sticky=W);
        self.entryString1.set("First Line");
        
        Label(lcdFrame,text="pwd").grid(row=1, column=0, sticky=W);
        Entry(lcdFrame,textvariable=self.entryString2,width=16).grid(row=1, column=1, sticky=W);
        self.entryString2.set("Second Line");
        lcdFrame.pack();
        
        #buzzer init
        #self.buzzer = Buzzer(16);
        GPIO.setwarnings(False);
        GPIO.setmode(GPIO.BOARD);
        GPIO.setup(36,GPIO.OUT);
        self.buzzer = GPIO.PWM(36, 50);
        
        #rfid init
        self.MIFAREReader = MFRC522.MFRC522();
        
        
    def userClickBuzzer(self):
        print("user click");
        self.buzzer.start(100);
        t = Timer(0.1,self.closeBuzzer);
        t.start();
        
        
    
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