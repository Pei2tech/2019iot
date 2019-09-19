from tkinter import *
from gpiozero import MCP3008
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from threading import Timer

class MCP3008app:
    def __init__(self,w):
        self.window = w;
        self.channel0 = MCP3008(0,max_voltage=5.0);
        cred = credentials.Certificate('/home/pi/Documents/raspberryfirebase-firebase-adminsdk-q4ht6-3282b25b5b.json')
        firebase_admin.initialize_app(cred, {'databaseURL': 'https://raspberryfirebase.firebaseio.com/',
                                             'databaseAuthVariableOverride': {'uid': 'NatxhTYp4AaiI2Uge648cNQjSIE3'}
                                             })
        self.registerRef  = db.reference('iot0624/MCP3008/register')
        print(self.registerRef.get())
        self.createGUI();
        self.timer = Timer(1.0,self.checkRegister);
        self.timer.start();
        
        
    def createGUI(self):
        mainFrame = Frame(self.window,borderwidth=2,relief=GROOVE);
        Label(mainFrame,text="可變電阻:").pack(anchor=W,padx=5,pady=5);
        self.scaleValue = DoubleVar();
        self.scaleValue.set(67)
        Scale(mainFrame,from_=0, to=100,variable=self.scaleValue, orient=HORIZONTAL,length=400,state=DISABLED).pack()
        
        
        mainFrame.pack(padx=30,pady=30);
    
    def checkRegister(self):
        value = self.channel0.value;
        print("now value:{}".format(value));


if __name__ == "__main__":
    window = Tk();
    window.title("MCP3008");
    window.option_add("*font",("verdana",18));
    window.option_add("*background","#068587");
    window.option_add("*foreground", "#ffffff");
    app = MCP3008app(w=window);    
    window.mainloop();