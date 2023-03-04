#!/usr/bin/python3
import yt_dlp
from tkinter import filedialog
import validators as check
import tkinter as tk
import os
def downloadVideo(url,path):
    URLS = url


    ydl_opts = {
        'format': 'm4a/bestaudio/best',


        'postprocessors': [{  # Extract audio using ffmpeg
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'm4a',
        }]
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
       ydl.download(URLS)
       tk.messagebox.showinfo('Info',"Download Successful!!!")

class GUI:
    def __init__(self, master=None):
        # build ui
        self.main_window = tk.Tk() if master is None else tk.Toplevel(master)
        self.main_window.configure(background="#515460", height=200, width=200)
        self.main_window.geometry("800x480")
        self.main_window.resizable(False, False)
        self.main_window.title("Youtube Downloader")
        self.frm_main = tk.Frame(self.main_window)
        self.frm_main.configure(background="#515460", height=480, width=800)
        self.lbl_appname = tk.Label(self.frm_main)
        self.lbl_appname.configure(
            anchor="n",
            background="#515460",
            compound="top",
            font="{Arial} 24 {bold}",
            foreground="#f9fafb",
            justify="left",
            takefocus=False,
            text='Youtube Downloader\n')
        self.lbl_appname.pack(pady=30, side="top")
        self.url_entry = tk.Entry(self.frm_main)
        self.url = tk.StringVar(value='Βάλε link\n')
        self.url_entry.configure(
            font="{Arial} 12 {}",
            justify="center",
            textvariable=self.url,
            width=60)
        _text_ = 'Βάλε link\n'
        self.url_entry.delete("0", "end")
        self.url_entry.insert("0", _text_)
        self.url_entry.pack(ipadx=30, pady=30, side="top")
        self.btn_download = tk.Button(self.frm_main)
        self.btn_download.configure(
            activebackground="#ff0404",
            compound="center",
            font="{arial} 8 {}",
            text='Download\n',
            width=10)
        self.btn_download.pack(pady=110, side="bottom")
        self.btn_download.configure(command=self.download_button)
        self.frm_main.pack(side="top")

        # Main widget
        self.mainwindow = self.main_window

    def run(self):
        self.mainwindow.mainloop()

    def download_button(self):

        path = self.path.get()
        link = self.url.get()
        if check.url(link):
            downloadVideo(link,path)


        else:
            tk.messagebox.showerror("Error", "Δεν έβαλες σωστό Link")



if __name__ == "__main__":
    app = GUI()
    app.run()

