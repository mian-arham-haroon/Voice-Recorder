import tkinter
from tkinter import *
from tkinter import messagebox
import sounddevice as sound
from scipy.io.wavfile import write
import time
import wavio as wv
import random
root=Tk()
root.title("Voice Recorder")
root.geometry("600x700+400+80")
root.configure(background="#4a4a4a")
root.resizable(False,False)

def Record ():
    # pass
    freq=44100
    dur=int(duration.get())
    recording=sound.rec(dur*freq,samplerate=freq,channels=2)
    number=random.randint(1,100)
    #timer
    try:
        temp=int(duration.get())
    except:
        print("Please enter the correct value")
    while temp>0:
        root.update()
        time.sleep(1)
        temp-=1
        if(temp==0):
            messagebox.showinfo("Timer Countdown","Time'up")
        Label(text=f"{str(temp)}",font="arial 40",width=4,background="#4a4a4a").place(x=240,y=590)   

    sound.wait()
    write(f"recording{number}.war",freq,recording)


#icon
image_icon=PhotoImage(file="Record.png")
root.iconphoto(False,image_icon)

#logo
photo=PhotoImage(file="Record.png")
myimage=Label(image=photo,background="#4a4a4a")
myimage.pack(pady=5,padx=5)

#name
Label(text="Voice Recorder",font="arial 30 bold",background="#a4a4a4",fg="white").pack()

#entry box
duration=StringVar()
entry=Entry(root,textvariable=duration,font="arial 30",width=15)
entry.pack(pady=10)
Label(text="Entry time in seconds",font="arial 15",background="#a4a4a4",fg="white").pack()

#button
record=Button(root,font="arial 20",text="Record",bg="#111111",fg="white",border=0,command=Record).pack(pady=30)



root.mainloop()
