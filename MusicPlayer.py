import os
from tkinter import *
from tkinter import filedialog, Tk
from pygame import mixer

# creating the tkinter window
master = Tk()
master.geometry("485x690")
master.title("Allegro")
master.configure(background="#96AD90")
master.resizable(False, False)
mixer.init()

logo = PhotoImage(file="icons/logo (1).png")
Label(master, image=logo, bg="#96AD90").place(x=40, y=40)

# creating a frame for the icons
frame1 = Frame(master, bg="#96AD90", width=485, height=100)
frame1.place(x=0, y=200)


def add_songs():
    path = filedialog.askdirectory()
    if path:
        os.chdir(path)
        songs = os.listdir(path)

        for song in songs:
            if song.endswith(".mp3"):
                listbox.insert(END, song)


paused = False


def play():
    global paused
    if paused:
        mixer.music.unpause()
        paused = False
    else:
        song = listbox.get(ACTIVE)
        mixer.music.load(song)
        mixer.music.play()


def pause():
    mixer.music.pause()
    global paused
    paused = True


pauseButton = PhotoImage(file="icons/pause.png")
Button(master, bg="#96AD90", image=pauseButton, cursor="hand2", command=pause).place(x=90, y=230)

playButton = PhotoImage(file="icons/play.png")
Button(master, bg="#96AD90", image=playButton, cursor="hand2", command=play).place(x=222, y=230)

stopButton = PhotoImage(file="icons/stop.png")
Button(master, bg="#96AD90", image=stopButton, cursor="hand2", command=mixer.music.stop).place(x=355, y=230)

button1 = Button(master, text="Browse Songs", width=20, justify=CENTER, font="courier 14", relief=RAISED,
                 cursor="hand2", command=add_songs)
button1.place(x=120, y=312)

frame2 = Frame(master, bg="black", width=485, height=350)
frame2.place(x=0, y=370)

scroll = Scrollbar(frame2)
listbox = Listbox(frame2, bg="black", width=42, height=14, cursor="hand2", yscrollcommand=scroll.set,
                  font="courier 14", fg="#96AD90")
scroll.config(command=listbox.yview, bg="#333333")
listbox.pack(side=LEFT, fill=BOTH)
scroll.pack(side=RIGHT, fill=Y)

master.mainloop()
