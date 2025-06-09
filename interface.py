import os
import flet as ft
from tkinter import messagebox
import yt_dlp


class YoutubeDownloader:
    def __init__(self, page: ft.Page):
        self.page = page

        self.label = None
        self.url_entry = None
        self.download_button = None
        self.open_dir = None

        self.page.title = "Youtube Video Downloader"

        self.page.window.width = 350
        self.page.window.height = 400
        self.page.window.icon = "../assets/icon/icon.ico"
        self.page.window.resizable = False
        self.page.window.maximizable = False

        self.page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        self.page.vertical_alignment = ft.MainAxisAlignment.CENTER

    async def create_widgets(self):

        self.label = ft.Text(
            "Youtube Video Downloader",
            size=20,
            font_family="Arial"
        )

        self.url_entry = ft.TextField(
            width=350,
            height=40,
            hint_text="Insert A Youtube Video Link"
        )

        self.download_button = ft.ElevatedButton(
            "Download video",
            on_click=self.download_video
        )

        self.open_dir = ft.ElevatedButton(
            "Open output",
            on_click=self.open_output_dir
        )

        self.page.add(
            ft.Column(
                [
                    self.label,
                    self.url_entry,
                    self.download_button,
                    self.open_dir,
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=15,
            )
        )

        self.page.update()

    async def download_video(self, e):
        try:
            yt_link = self.url_entry.value

            ydl_opts = {
                "outtmpl": "output/%(title)s.%(ext)s",
                "format": "best",
            }

            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([yt_link])

            messagebox.showinfo(
                "Success",
                "Download completed!"
            )

        except Exception as ex:
            messagebox.showerror(
                "Error",
                f"Something went wrong:\n{ex}"
            )

    async def open_output_dir(self, e):
        try:
            os.startfile("output")

        except (FileExistsError, FileNotFoundError):
            print("FileNotFound")


class App:
    async def main(self, page: ft.Page):
        downloader = YoutubeDownloader(page)
        await downloader.create_widgets()


if __name__ == "__main__":
    ft.app(target=App().main)