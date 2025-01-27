from tkinter import ttk, NO, YES

import customtkinter as ctk
from PIL import Image

from view.add_question.app_create_question import AppCreateQuestion


class FrameQuestions(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(1, weight=1)

        # self.configure(fg_color="red")

        self.tree = ttk.Treeview(
            self, columns=("profession", "category", "question"), show="headings"
        )
        self.tree.column("#1", stretch=NO, width=150)
        self.tree.column("#2", stretch=NO, width=80)

        self.tree.heading("profession", text="Должность", anchor="center")
        self.tree.heading("category", text="Категория", anchor="center")
        self.tree.heading("question", text="Вопрос", anchor="center")

        # Добавляем данные в Treeview
        self.tree.insert(
            "",
            "end",
            tags=("1",),
            values=(
                ["ДСП", "ДС"],
                "ghg",
                "Длинный вопрос олржрвыжолрафжрвы ф жылдвраждлывржадфлрывж  лфоывржадлржфывдлар жжфыдлвраж жлорждрждлр рждлрждлрж ржрждрлжлрж ждлрждлрррдлрывхщгэжээж оов вовшш воо вшшш",
            ),
        )
        self.tree.insert(
            "",
            "end",
            tags=("2",),
            values=(
                ["ДСП"],
                "OPO",
                "klhph'koh[oig['okh 'lkh 'h' '''' h'loiy[oiy 'poy",
            ),
        )
        self.tree.insert(
            "",
            "end",
            tags=("3",),
            values=(["ДСП", "LYW"], "B", "fghdfh fgf  fghf fgf fgh ghfgd fghfg"),
        )
        # self.tree.bind("<<TreeviewSelect>>", )
        self.tree.bind("<Double-Button-1>", self.modify_question)

        self.button_del_question = ctk.CTkButton(
            self,
            text="Добавить вопрос",
            font=("Arial", 22),
            border_width=1,
            fg_color="#63c0f2",
            width=350,
            height=50,
            command=self.create_question,
        )
        self.button_modify_question = ctk.CTkButton(
            self,
            text="Удалить вопрос",
            font=("Arial", 22),
            border_width=1,
            fg_color="#63c0f2",
            width=350,
            height=50,
            command=self.delete_question,
        )
        self.create_question_window = None
        self.put_widgets()

    def put_widgets(self):
        self.tree.grid(row=1, column=1, columnspan=2, rowspan=2, sticky="wnes")
        self.button_del_question.grid(row=3, column=1, padx=10, pady=10, sticky="s")
        self.button_modify_question.grid(row=3, column=2, padx=10, pady=10, sticky="s")

    def open_app_create_question(self):
        if (
            self.create_question_window is None
            or not self.create_question_window.winfo_exists()
        ):
            self.create_question_window = AppCreateQuestion(
                self
            )  # create window if its None or destroyed
        else:
            self.create_question_window.focus()

    def delete_question(self):
        for selected_item in self.tree.selection():
            print(self.tree.item(selected_item))
            print(self.tree.delete(selected_item))
            print("удаляю вопрос")

    def modify_question(self, event=None):
        self.open_app_create_question()
        print("Исправляем вопрос")
        print(self.tree.item(*self.tree.selection()))
        for selected_item in self.tree.selection():
            print(self.tree.item(selected_item))

    def create_question(self):
        self.open_app_create_question()
        print("добавляем новый вопрос")
