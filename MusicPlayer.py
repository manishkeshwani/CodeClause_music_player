from tkinter import *
import tkinter as tk
from tkinter import ttk,filedialog
from PIL import Image, ImageTk
from pygame import mixer
import os

root = tk.Tk()
root.title("Music Player")
root.geometry("920x670+290+85")
root.configure(bg="#0f1a2b")
root.resizable(False,False)

mixer.init()

def open_folder():
    path = filedialog.askdirectory()
    if path:
        os.chdir(path)
        songs=os.listdir(path)
        # print(songs)
        for song in songs:
            if song.endswith(".mp3"):
                playlist.insert(END,song)


def play_song():
    music_name = playlist.get(ACTIVE)
    # print(music_name[0:-4])
    mixer.music.load(playlist.get(ACTIVE))
    mixer.music.play()
    music.config(text=music_name[0:-4])

def play_next():
    next_song = playlist.curselection()
    next_song = next_song[0] + 1
    next_song_name = playlist.get(next_song)
    music.config(text=next_song_name)

    playlist.select_clear(0,'end')
    playlist.activate(next_song)
    playlist.select_set(next_song)

    mixer.music.load(playlist.get(ACTIVE))
    mixer.music.play()


def play_prev():
    next_song = playlist.curselection()
    next_song = next_song[0] - 1
    next_song_name = playlist.get(next_song)
    music.config(text=next_song_name)

    playlist.select_clear(0,'end')
    playlist.activate(next_song)
    playlist.select_set(next_song)

    mixer.music.load(playlist.get(ACTIVE))
    mixer.music.play()

#icon
image_icon = PhotoImage(file="logo.png")
root.iconphoto(False,image_icon)

Top=PhotoImage(file='top.png')
Label(root,image=Top,bg="#0f1a2b").pack()

#logo
Logo = PhotoImage(file="logo.png")
Label(root,image=Logo,bg="#0f1a2b").place(x=65,y=115)

#button
play_button = PhotoImage(file="play.png")
Button(root,
       image=play_button,
       bg="#0f1a2b",
       relief=FLAT,
       command=play_song).place(x=55,y=400)

img = Image.open("pause.png")
image = img.resize((94,94))
pause2_button = ImageTk.PhotoImage(image)
Button(root,
       image=pause2_button,
       bg="#0f1a2b",
       relief=FLAT,
       command=mixer.music.pause).place(x=150,y=400)

img = Image.open("prev.png")
image = img.resize((65,65))
prev_button = ImageTk.PhotoImage(image)
Button(root,
       image=prev_button,
       bg="#0f1a2b",
       relief=FLAT,
       command=play_prev).place(x=30,y=500)

resume_button = PhotoImage(file="resume.png")
Button(root,
       image=resume_button,
       bg="#0f1a2b",
       relief=FLAT,
       command=mixer.music.unpause).place(x=115,y=500)

img = Image.open("next.png")
image = img.resize((65,65))
next_button = ImageTk.PhotoImage(image)
Button(root,
       image=next_button,
        bg="#0f1a2b",
        relief=FLAT,
        command=play_next).place(x=200,y=500)

#label
music=Label(root,text="",font=("arial",15),fg="white",bg="#0f1a2b")
music.place(x=150,y=340,anchor="center")

#music menu
img = Image.open("menu.png")
image = img.resize((597,370))
Menu = ImageTk.PhotoImage(image)
Label(root,image=Menu,bg="#0f1a2b").pack(padx=10,pady=50,side=RIGHT)

music_frame = Frame(root,bd=2,bg="#0f1a2b")
music_frame.place(x=330,y=350,width=560,height=250)

Button(root,text="Open Folder",
       width=15,
       height=2,
       font=("arial",10,"bold"),
       fg='white',bg="#21b3de",
       command=open_folder).place(x=330,y=300)


scroll = Scrollbar(music_frame)
playlist=Listbox(music_frame,width=100,
                 font=("arial",10),
                 bg="#333333",
                 fg="white",
                 selectbackground="lightblue",
                 cursor="hand2",
                 bd=0,
                 yscrollcommand=scroll.set)

scroll.config(command=playlist.yview)
scroll.pack(side=RIGHT,fill=Y)
playlist.pack(side=LEFT,fill=BOTH)


root.mainloop()

