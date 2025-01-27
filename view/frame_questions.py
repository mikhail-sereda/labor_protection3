from tkinter import ttk

import customtkinter as ctk
from PIL import Image


class FrameQuestions(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(1, weight=1)

        self.configure(fg_color="red")

        self.tree = ttk.Treeview(self, columns=("Name", "Age"), show="headings")
        self.tree.heading("Name", text="Имя")
        self.tree.heading("Age", text="Возраст")

        # Добавляем данные в Treeview
        self.tree.insert("", "end", values=("Алексей", 30), open=False)
        self.tree.insert("", "end", values=("Мария", 25))
        self.tree.insert("", "end", values=("Иван", 35))

        self.button_del_question = ctk.CTkButton(
            self,
            text="Настройка экзамена",
            font=("Arial", 22),
            border_width=1,
            fg_color="#63c0f2",
            width=350,
            height=50,
            command=None,
        )
        self.button_modify_question = ctk.CTkButton(
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
        self.tree.grid(row=1, column=1, columnspan=2, rowspan=2, sticky="wne")
        self.button_del_question.grid(row=3, column=1, padx=10, pady=10, sticky="s")
        self.button_modify_question.grid(row=3, column=2, padx=10, pady=10, sticky="s")


    def delete_question(self):
        print("удаляю вопрос")
        pass


    def modify_question(self):
        print("изменяю вопрос")
        pass
