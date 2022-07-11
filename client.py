#-----------Bolierplate Code Start -----
import socket
from threading import Thread
from tkinter import *
from tkinter import ttk
from tkinter import filedialog

PORT  = 8080
IP_ADDRESS = '127.0.0.1'
SERVER = None
BUFFER_SIZE = 4096


name = None
listbox =  None
textarea= None
labelchat = None
text_message = None


def openMusicWindow():

   
    print("\n\t\t\t\tMUSIC WINDOW")

    #Client GUI starts here
    window=Tk()

    window.title('MUSIC WINDOW')
    window.geometry("300x300")
    window.configure(bg = "LightSkyBlue")

    global name
    global listbox
    global textarea
    global labelchat
    global text_message
    global filePathLabel

    namelabel = Label(window, text= "Select Song", font = ("Calibri",10))
    namelabel.place(x=2, y=1)

   # name = Entry(window,width =30,font = ("Calibri",10))
   # name.place(x=120,y=8)
   # name.focus()

    #connectserver = Button(window,text="Connect to Chat Server",bd=1, font = ("Calibri",10))
    #connectserver.place(x=350,y=6)

    separator = ttk.Separator(window, orient='horizontal')
    separator.place(x=0, y=35, relwidth=1, height=0.1)

    labelusers = Label(window, text= "Songs", font = ("Calibri",10))
    labelusers.place(x=10, y=50)

    listbox = Listbox(window,height = 5,width = 67,activestyle = 'dotbox', font = ("Calibri",10))
    listbox.place(x=10, y=70)

    scrollbar1 = Scrollbar(listbox)
    scrollbar1.place(relheight = 1,relx = 1)
    scrollbar1.config(command = listbox.yview)

    playButton=Button(window,text="Play",bd=1, font = ("Calibri",10))
    playButton.place(x=30,y=200)

    stopButton=Button(window,text="Stop",bd=1, font = ("Calibri",10))
    stopButton.place(x=200,y=200)

    upload=Button(window,text="Upload",bd=1, font = ("Calibri",10))
    upload.place(x=30,y=250)
    
    #labelChat = Label(window,text="Chat Window" , font = ("Calibri",10))
    #labelChat.place(x = 10 , y = 180)

   # textArea = Text(window , width = 67 , height = 6 , font = ("Calibri" , 10))
    #textArea.place(x = 10 , y = 200)

   # scrollbar2 = Scrollbar(textArea)
   # scrollbar2.place(relheight = 1,relx = 1)
   # scrollbar2.config(command = listbox.yview)
    
    #textMessage = Entry(window , width = 43 , font = ("Calibri" , 10))
  #  textMessage.pack()
   # textMessage.place (x = 100 , y = 304)

    download = Button(window , text = "Download" , bd = 1, font = ("Calibri",10))
    download.place(x = 200 , y = 250)

    #send = Button(window , text = "Send" , bd = 1, font = ("Calibri",10))
    #send.place(x = 450 , y = 305)


    infoLabel = Label(window , text = "" , fg = "blue" , font = ("Calibri",8))
    infoLabel.place(x = 4 , y = 250)


    
  
  
  
    window.mainloop()




def setup():
    global SERVER
    global PORT
    global IP_ADDRESS

    SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    SERVER.connect((IP_ADDRESS, PORT))

   
    openMusicWindow()

setup()
