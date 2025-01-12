from tkinter import Menu

import customtkinter as ctk
from PIL import Image


class FrameMain(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        # super().__init__(parent)
        # self.master = parent
        super().__init__(master, **kwargs)
        self.master = master
        self.ico_setting = ctk.CTkImage(light_image=Image.open("static/img/ico_setting3.png"),
                                        dark_image=Image.open("static/img/ico_setting3.png"),
                                        size=(40, 40))
        self.label_main = ctk.CTkLabel(self, text='Проверка знаний по охране труда', font=('Arial', 32, "bold"))
        self.button_settings = ctk.CTkButton(self, text="", width=40, height=40, font=('Arial', 22),
                                    fg_color="#63c0f2", border_width=1, image=self.ico_setting, command=self.put_frame_menu)
        self.button_start = ctk.CTkButton(self, text="Приступить к проверке знаний", font=('Arial', 22),
                                    border_width=1, fg_color="#63c0f2", command=self.start_exam)
        self.put_widgets()

    def put_widgets(self):
        self.button_settings.pack(anchor="ne", padx=10, pady=10, ipadx=0, ipady=0)
        self.label_main.pack(padx=50, pady=50)
        self.button_start.pack(expand=True, ipadx=20, ipady=15)

    def put_frame_menu(self):
        self.master.view_frame_menu()
        self.destroy()

    def start_exam(self):
        self.button_start.configure(state="disabled")
        self.button_settings.configure(state="disabled")
        self.master.open_exam_app()

    def exit_exam(self):
        self.button_start.configure(state="enable")
        self.button_settings.configure(state="disabled")
        self.master.open_exam_app()





