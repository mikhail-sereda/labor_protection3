from tkinter import ttk

import customtkinter as ctk
from PIL import Image


class FrameQuestions(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.tree = ttk.Treeview(self, columns=("Name", "Age"), show="headings")
        self.tree.heading("Name", text="Имя")
        self.tree.heading("Age", text="Возраст")

        # Добавляем данные в Treeview
        self.tree.insert("", "end", values=("Алексей", 30))
        self.tree.insert("", "end", values=("Мария", 25))
        self.tree.insert("", "end", values=("Иван", 35))

        # Упаковываем Treeview
        self.tree.pack(fill="both", expand=True)

    # def put_widgets(self):
    #     self.button_exa.pack(expand=True, ipadx=20, ipady=15)
