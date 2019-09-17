from tkinter import *



def appInterface(window):    
    buttonText.set("ON")
    frame = Frame(window,borderwidth=2,relief=GROOVE);
    ledButton = Button(frame,textvariable = buttonText,padx=30,pady=10,command=userClick).pack(padx=40,pady=40);
    frame.pack(padx=10,pady=10);

def userClick():
    buttonText.set("OFF")
    print("user click");
    

if __name__ == '__main__':
    buttonText = StringVar();
    app = Tk();
    app.title("LEDControl");
    #app.geometry("500x600");
    appInterface(window = app);
    app.mainloop();