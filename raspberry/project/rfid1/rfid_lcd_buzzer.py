from tkinter import *
from threading import Timer
import RPi.GPIO as GPIO
import mfrc522 as MFRC522
from lcd_display import lcd as Lcd

import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from firebase_admin import auth






class App:
    def __init__(self,window):
        #init firebase
        self.cred = credentials.Certificate('/home/pi/Documents/raspberryfirebase-firebase-adminsdk-q4ht6-3282b25b5b.json')
        firebase_admin.initialize_app(self.cred, {
    'databaseURL': 'https://raspberryfirebase.firebaseio.com/',
    'databaseAuthVariableOverride': {'uid': 'NatxhTYp4AaiI2Uge648cNQjSIE3'}
    })

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
        
        Label(lcdFrame,text="name").grid(row=0, column=0, sticky=W,padx=5,pady=5);
        Entry(lcdFrame,textvariable=self.entryString1,width=16).grid(row=0, column=1, sticky=W,padx=5,pady=5);
        self.entryString1.set("First Line");
        
        Label(lcdFrame,text="pwd").grid(row=1, column=0, sticky=W,padx=5, pady=5);
        Entry(lcdFrame,textvariable=self.entryString2,width=16).grid(row=1, column=1, sticky=W,padx=5,pady=5);
        self.entryString2.set("Second Line");
        
        Button(lcdFrame,text="send",command=self.userClickSend,padx=10,pady=10).grid(row=2,column=0, columnspan=2,sticky=NSEW,padx=5,pady=5);
        lcdFrame.pack();
        
        #buzzer init
        #self.buzzer = Buzzer(16);
        GPIO.setwarnings(False);
        GPIO.setmode(GPIO.BOARD);
        GPIO.setup(36,GPIO.OUT);
        self.buzzer = GPIO.PWM(36, 50);
        
        
        
        #rfid init
        self.uid = [];
        self.preUid0 = 0
        self.preUid1 = 0
        self.preUid2 = 0
        self.preUid3 = 0
        self.MIFAREReader = MFRC522.MFRC522();
        self.rfidHandler();
        #lcd init
        self.lcd = Lcd()
        
        
    def userClickBuzzer(self):
        print("user click");
        self.buzzer.start(100);
        t = Timer(0.1,self.closeBuzzer);
        t.start();
        
        
    
    def closeBuzzer(self):
        self.buzzer.stop();
    
    def userClickSend(self):
        '''
        entry1Words = self.entryString1.get();
        entry2Words = self.entryString2.get();
        self.lcd.display_string(entry1Words,1);
        self.lcd.display_string(entry2Words,2);
        '''
        try:
            entryEmail = self.entryString1.get();        
            user = auth.get_user_by_email(entryEmail);
            self.lcd.display_string(user.uid,1);
            self.lcd.display_string('success',2);
            print(user.uid);
        except:
            self.lcd.display_string('incorrect',1);
            self.lcd.display_string('who are you?',2);
            
    def rfidHandler(self):
        #scan for cards
        
        (status,tagType) = self.MIFAREReader.MFRC522_Request(self.MIFAREReader.PICC_REQIDL);
        
        if status == self.MIFAREReader.MI_OK:
            print("ok");
        
        Timer(0.1,self.rfidHandler).start();

if __name__ == "__main__":
    root = Tk();
    root.title("RFID_LCD_BUZZER");
    root.option_add("*font",("verdana", 18));
    root.option_add("*background", "#cccccc");
    root.option_add("*forground","#888888");
    app = App(root);
    root.mainloop();