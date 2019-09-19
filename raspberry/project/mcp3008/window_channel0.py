from tkinter import *
from gpiozero import MCP3008

class MCP3008app:
    def __init__(self,w):
        self.window = w;
        self.createGUI();
        
    def createGUI(self):
        print(self.window);


if __name__ == "__main__":
    window = Tk();
    window.title("MCP3008");
    app = MCP3008app(w=window);    
    window.mainloop();