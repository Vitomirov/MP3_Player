# Importing necessary libraries
import os
from tkinter import *
from tkinter import filedialog
from pygame import mixer

# Initializing the Tkinter window
root = Tk()
root.title("Deki DeVito")
root.geometry("485x700+290+10")
root.configure(background="#30302f")
root.resizable(False, False)
mixer.init()

# Function to add music to the playlist
def addMusic():
    path = filedialog.askdirectory()
    if path:
        os.chdir(path)
        songs = os.listdir(path)

        for song in songs:
            if song.endswith(".mp3"):
                Playlist.insert(END, song)

# Function to play music
def playMusic():
    musicName = Playlist.get(ACTIVE)
    print(musicName[0:-4])
    mixer.music.load(Playlist.get(ACTIVE))
    mixer.music.play()

# Function to increase volume
def increaseVolume():
    global currentVolume
    currentVolume = min(currentVolume + 0.1, 1.0)
    mixer.music.set_volume(currentVolume)

# Function to decrease volume
def decreaseVolume():
    global currentVolume
    currentVolume = max(currentVolume - 0.1, 0.0)
    mixer.music.set_volume(currentVolume)

# Function to pause music
def pause():
    global paused
    if paused:
        mixer.music.unpause()
        paused = False
    else:
        mixer.music.pause()
        paused = True

# Creating a lower frame for the music player controls
lowerFrame = Frame(root, background="#dbd9d5", width=485, height=200)
lowerFrame.place(x=0, y=400)

# Setting the icon for the Tkinter window
imageIcon = PhotoImage(file="logo.png")
root.iconphoto(False, imageIcon)

# Creating a GIF animation for the background
frameCnt = 5
frames = [PhotoImage(file="giphy.gif", format='gif -index %i' % i) for i in range(frameCnt)]

# Function to update the GIF animation
def update(ind):
    frame = frames[ind]
    ind += 1
    if ind == frameCnt:
        ind = 0
    label.configure(image=frame)
    root.after(50, update, ind)

# Creating a label to display the GIF animation
label = Label(root)
label.place(x=0, y=0, height=485)
root.after(0, update, 0)

# Creating buttons for music player controls
ButtonPlay = PhotoImage(file="play.png")
Button(root, image=ButtonPlay, bg="#FFFFFF", bd=0, height=60, width=60,
       command=playMusic).place(x=258, y=487)

ButtonStop = PhotoImage(file="stop.png")
Button(root, image=ButtonStop, bg="#FFFFFF", bd=0, height=60, width=60,
       command=mixer.music.stop).place(x=195.2, y=487)

currentVolume = 0.5

ButtonVolumeUp = PhotoImage(file="volumeUp.png")
Button(root, image=ButtonVolumeUp, bg="#FFFFFF", bd=0, height=60, width=60,
       command=lambda: increaseVolume()).place(x=132, y=487)

ButtonVolumeDown = PhotoImage(file="volumeDown.png")
Button(root, image=ButtonVolumeDown, bg="#FFFFFF", bd=0, height=60, width=60,
       command=lambda: decreaseVolume()).place(x=72, y=487)

paused = False
ButtonPause = PhotoImage(file="pause.png")
Button(root, image=ButtonPause, bg="#FFFFFF", bd=0, height=60, width=60,
       command=pause).place(x=320, y=487)

# Creating a menu button
Menu = PhotoImage(file="menu.png")
Label(root, image=Menu).place(x=0, y=650, width=485, height=100)

# Creating a frame for the music playlist
Frame_Music = Frame(root, bd=4, relief=RIDGE)
Frame_Music.place(x=0, y=585, width=485, height=100)

# Creating a button to add music to the playlist
Button(root, text="Add Music", width=59, height=1, font=("ariel", 12, "bold"),
       fg="Black", bg="#FFFFFF", command=addMusic).place(x=-120, y=550)

# Creating a scrollbar for the music playlist
Scroll = Scrollbar(Frame_Music)

# Creating a listbox for the music playlist
Playlist = Listbox(Frame_Music, width=100, font=("Ariel", 10),
                   bg="#333333", fg="Grey", selectbackground="lightblue",
                   cursor="hand2", bd=0, yscrollcommand=Scroll.set)

# Configuring the scrollbar for the music playlist
Scroll.config(command=Playlist.yview)
Scroll.pack(side=RIGHT, fill=Y)

# Packing the listbox for the music playlist
Playlist.pack(side=RIGHT, fill=BOTH)

# Starting the Tkinter mainloop
root.mainloop()
