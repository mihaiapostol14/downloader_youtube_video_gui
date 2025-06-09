import os
from tkinter import messagebox
import customtkinter
import yt_dlp


class Frame(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        # add widgets to app
        self.label = customtkinter.CTkLabel(self, text='Insert A Youtube Video Link')
        self.label.pack(padx=10, pady=10)

        self.url_entry = customtkinter.CTkEntry(self, width=350, height=40)
        self.url_entry.pack(padx=10, pady=10)

        self.download_button = customtkinter.CTkButton(self, text='Download video', command=self.download_video)
        self.download_button.pack(padx=20, pady=10)

        self.open_dir = customtkinter.CTkButton(self, text='Open output', command=self.open_output_dir)
        self.open_dir.pack(padx=20, pady=20)

    # add methods to app
    def download_video(self):
        try:
            yt_link = self.url_entry.get()
            ydl_opts = {
                'outtmpl': "output/%(title)s.%(ext)s",  # Save inside 'output' folder
                'format': 'best',
            }
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([yt_link])
            messagebox.showinfo("Success", "Download completed!")
        except Exception as ex:
            messagebox.showerror("Error", f"Something went wrong:\n{ex}")

    def open_output_dir(self):
        try:
            os.startfile('output')
        except(FileExistsError, FileNotFoundError):
            print('FileNotFound')


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title('Youtube Video Downloader')
        self.geometry('350x400')
        self.resizable(False,False)
        self.grid_rowconfigure(0, weight=1)  # configure grid system
        self.grid_columnconfigure(0, weight=1)

        self.frame = Frame(master=self)
        self.frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")


app = App()
app.mainloop()