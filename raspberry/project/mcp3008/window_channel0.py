from tkinter import *
from gpiozero import MCP3008

class MCP3008app:
    def __init__(self,w):
        self.window = w;
        self.createGUI();
        
    def createGUI(self):
        mainFrame = Frame(self.window,borderwidth=2,relief=GROOVE);
        Label(mainFrame,text="可變電阻:").pack();
        scaleValue = DoubleVar();
        scaleValue.set(67)
        Scale(mainFrame,from_=0, to=100,variable=scaleValue, orient=HORIZONTAL,length=400,state=DISABLED).pack()
        
        
        mainFrame.pack(padx=30,pady=30);


if __name__ == "__main__":
    window = Tk();
    window.title("MCP3008");
    window.option_add("*font",("verdana",18));
    window.option_add("*background","#068587");
    window.option_add("*foreground", "#ffffff");
    app = MCP3008app(w=window);    
    window.mainloop();