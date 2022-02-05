import tkinter
from tkinter import ttk
from tkinter import messagebox
from tkinter.ttk import Style
from pytube import YouTube
import os


def Download(videourl, path):

    yt = YouTube(videourl)
    yt = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
    if not os.path.exists(path):
        os.makedirs(path)
    yt.download(path)

def Button():

    url = link.get()
    try:
        Download(url, os.getcwd())
    except:
        messagebox.showerror("Error", "Try again")
    else:
        return messagebox.showinfo('Youtube Downloader', "The video has been downloaded")


root = tkinter.Tk()
root.title("Youtube Downloader")

root.geometry("385x120")
root.resizable(False, False)


root.configure(bg='#d85454')
s = Style()
s.configure('Red.TFrame', background='#d85454')


frame = ttk.Label(root, style='Red.TFrame')
frame.grid(row=0, column=0, padx=10, pady=10)


label = ttk.Label(frame, text="Enter Video URL: ", font = ('Arial', 18, 'bold'), background="#d85454", foreground="white")
label.grid(row=0, column=0, sticky=tkinter.W)
link = tkinter.StringVar()


yturl = ttk.Entry(frame, width=60, textvariable=link)
yturl.grid(row=1, columnspan=3, padx=0, pady=3)
yturl.focus()

button = ttk.Button(frame, text="Download Video",
                  width=15, command=Button)
button.grid(row=7, columnspan=3, padx=13, pady=7)


root.mainloop()