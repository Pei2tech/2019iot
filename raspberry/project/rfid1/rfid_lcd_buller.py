from tkinter import *
from threading import Timer
import RPi.GPIO as GPIO
import mfrc522 as MFRC522

class App:
    def __init__(self,window):
        #buzzer frame button
        buzzerFrame = Frame(window);
        Button(buzzerFrame,text="Buzzer Control", padx=10, pady=10,command=self.userClickBuzzer).pack(padx=30,pady=10);
        buzzerFrame.pack();
        
        #lcd frame
        lcdFrame = Frame(window);
        self.entryString1 = StringVar();
        self.entryString2 = StringVar();
        #entry1Frame
        entry1Frame = Frame(lcdFrame);
        Label(entry1Frame,text="name").pack(side=LEFT);
        Entry(entry1Frame,textvariable=self.entryString1,width=50).pack(side=LEFT,padx=10);
        self.entryString1.set("First Line");
        entry1Frame.pack();
        
        #entry2Frame
        
        
        entry2Frame = Frame(lcdFrame);
        Label(entry2Frame,text="pwd").pack(side=LEFT);
        Entry(entry2Frame,textvariable=self.entryString2,width=50).pack(side=LEFT,padx=10);
        self.entryString2.set("Second Line");
        entry2Frame.pack();
        
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