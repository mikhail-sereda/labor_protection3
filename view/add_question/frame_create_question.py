import customtkinter as ctk
from PIL import Image


class FrameCreateQuestion(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # self.ico_arrow = ctk.CTkImage(light_image=Image.open("static/img/arrow_back.png"),
        #                               dark_image=Image.open("static/img/arrow_back.png"),
        #                               size=(130, 35))
        self.ico_instructions = ctk.CTkImage(
            light_image=Image.open("static/img/question_mark.png"),
            dark_image=Image.open("static/img/question_mark.png"),
            size=(40, 40),
        )
        # TODO Наполнить фрейм добавления вопроса: Выбор должности(выпадающий список), выбор профессий,
        self.grid_columnconfigure(1, weight=1)
