from tkinter import *
from tkinter import font
import turtle
from numpy import pad 
from pytube import YouTube
import webbrowser as wb

root = Tk()
root.geometry('500x300')
root.resizable(0,0)
root.title("Youtube Video Downloader")
root.configure(bg='black')
print('''\U0001f600 \U0001f600 Welcome to the Youtube Vodeo downloader program
        * Copy the link of any youtube video by clicking on share button and paste it in the GUI
        * Enjoy \U0001f600 \U0001f600''')

Label(root,text="YOUTUBE VIDEO DOWNLOADER",bg='black',fg="cyan",font='arial 15 bold').pack()

link = StringVar()

Label(root, text = 'Paste Link Here:',fg='white', font = 'arial 15 bold',bg='black').place(x= 160 , y = 60)
enteredlink = Entry(root, width = 190,textvariable = link, ).place(x = 32, y = 90 ,height=25)

def Downloader():
    if link!="":
        url = YouTube(str(link.get()))
        video = url.streams.filter(file_extension='mp4').first()
        video.download()
        Label(root,text = 'Downloaded Successfully',font='arial 15',fg='black',bg='green').place(x=140,y=210)
        Label(root,text="By DarkFire",bg="black",fg='cyan',font='arial 15 bold').pack(side="bottom")
    else:
        Label(root,text="Please enter a link",bg='black',fg='red').pack(side='bottom')

Button(root,text = 'DOWNLOAD', font = 'arial 15 bold' ,bg = 'red', padx = 2, command = Downloader).place(x=180 ,y = 150)

root.mainloop()