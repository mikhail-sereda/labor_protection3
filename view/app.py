import platform
import sys

import customtkinter as ctk
from PIL import Image

from view.exam_window.exam_app import ExamWindowApp
from view.frame_main import FrameMain
from view.frame_menu import FrameMenu


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry('900x600+500+200')
        self.minsize(600, 400)
        if "win" in sys.platform:
            try:
                self.lab = ctk.CTkImage(light_image=Image.open("static/img/ico.ico"),
                                        dark_image=Image.open("static/img/ico.ico"))
                self.iconphoto(True, self.lab)
            except:
                ...
        self.title('Экзамен по охране труда')
        self.exam_window = None
        self.frame_main = None
        self.frame_menu = None
        self.view_frame_main()

    def view_frame_main(self):
        self.frame_main = FrameMain(self)
        self.frame_main.pack(expand=True, fill="both")

    def view_frame_menu(self):
        self.frame_main = FrameMenu(self)
        self.frame_main.pack(expand=True, fill="both")

    def open_exam_app(self):
        if self.exam_window is None or not self.exam_window.winfo_exists():
            self.exam_window = ExamWindowApp(self)  # create window if its None or destroyed
        else:
            self.exam_window.focus()
