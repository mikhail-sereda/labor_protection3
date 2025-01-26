import customtkinter as ctk
from PIL import Image


class FrameQuestions(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.button_exa = ctk.CTkButton(
            self,
            text="Настройка экзамена",
            font=("Arial", 22),
            border_width=1,
            fg_color="#63c0f2",
            width=350,
            height=50,
            command=None,
        )

        self.put_widgets()

    def put_widgets(self):
        self.button_exa.pack(expand=True, ipadx=20, ipady=15)
