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
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=20)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=10)

        self.answers = [
            {"text": "первый", "bu": True, "id": 1},
            {"text": "второйj", "bu": False, "id": 1},
            {"text": "33333j", "bu": False, "id": 1},
            {"text": "444444", "bu": True, "id": 1},
        ]

        self.frame_choice = ctk.CTkFrame(self)  #  fg_color="red"
        self.frame_add_question = ctk.CTkFrame(self)
        self.frame_add_answers = ctk.CTkScrollableFrame(self, orientation="vertical")
        self.frame_add_answers.grid_columnconfigure(0, weight=1)
        self.frame_add_answers.grid_columnconfigure(1, weight=30)
        self.frame_add_answers.grid_columnconfigure(2, weight=1)

        self.combo_choice_category = ctk.CTkComboBox(
            self.frame_choice, values=["option 1", "option 2"]
        )
        self.check_choice_professions = ctk.CTkCheckBox(
            self.frame_choice, text="option 1"
        )
        self.button_save = ctk.CTkButton(
            self.frame_choice,
            text="Сохранить",
            font=("Arial", 20),
            border_width=1,
            fg_color="#63c0f2",
            command=None,
        )

        self.text_question = ctk.CTkTextbox(self.frame_add_question, font=("Arial", 18))

        self.put_frame()

    def put_frame(self):
        self.frame_choice.grid(
            column=0, row=0, rowspan=2, sticky="ewns", padx=5, pady=5
        )
        self.frame_add_question.grid(
            column=1, row=0, sticky="ewns", padx=(0, 5), pady=(5, 5)
        )
        self.frame_add_answers.grid(
            column=1, row=1, sticky="ewns", padx=(0, 5), pady=(0, 5)
        )
        self.put_widget_choice()
        self.put_widget_question()
        self.put_widget_answer()

    def put_widget_choice(self):
        self.combo_choice_category.pack()
        self.check_choice_professions.pack()
        self.button_save.pack(
            padx=15, pady=10, ipadx=10, ipady=10, fill="x", side="bottom"
        )

    def put_widget_question(self):
        self.text_question.pack(
            expand=True, fill="both", ipadx=20, ipady=20, anchor="center"
        )

    def put_widget_answer(self):
        for answer in range(len(self.answers)):
            self.checkbox_var = ctk.IntVar(value=self.answers[answer]["bu"])
            chek = ctk.CTkCheckBox(self.frame_add_answers, text="", width=0, variable=self.checkbox_var).grid(
                column=0, row=answer, padx=5, pady=5
            )
            self.text = ctk.CTkTextbox(self.frame_add_answers, height=70)
            self.text.grid(column=1, row=answer, sticky="ew", padx=5, pady=5)
            self.text.insert("1.0", self.answers[answer]["text"])
            btn = ctk.CTkButton(
                self.frame_add_answers, text="Удалить", height=50, width=50
            ).grid(
                column=3,
                row=answer,
                columnspan=1,
                padx=5,
                pady=5,
            )
        self.button_add_answer_form = ctk.CTkButton(self.frame_add_answers, text="Добавить вариант ответа", height=50)
        self.button_add_answer_form.grid(column=0,
                                  row=len(self.answers) + 1,
                                  columnspan=3,
                                  padx=5,
                                  pady=5, )
        for i in self.frame_add_answers.winfo_children():
            print(i.__dict__)
