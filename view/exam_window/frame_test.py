import customtkinter as ctk
from PIL import Image

from database.crud.crud_profession import db_get_all_profession


class FrameTest(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.master = master
        self.ico_arrow = ctk.CTkImage(
            light_image=Image.open("static/img/arrow_back.png"),
            dark_image=Image.open("static/img/arrow_back.png"),
            size=(130, 35),
        )
        self.ico_instructions = ctk.CTkImage(
            light_image=Image.open("static/img/question_mark.png"),
            dark_image=Image.open("static/img/question_mark.png"),
            size=(40, 40),
        )
        # self.configure(fg_color="red")
        # self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.variable_profession = ctk.Variable()
        self.list_profession = [i.professionName for i in db_get_all_profession()]

        self.button_instructions = ctk.CTkButton(
            self,
            text="",
            width=40,
            height=40,
            font=("Arial", 22),
            fg_color="#63c0f2",
            border_width=1,
            image=self.ico_instructions,
            command=None,
        )
        self.label_registration = ctk.CTkLabel(
            self, text="Регистрация", font=("Arial", 32, "bold")
        )

        self.combo_profession = ctk.CTkComboBox(
            self,
            variable=self.variable_profession,
            values=self.list_profession,
            width=365,
            height=50,
            dropdown_font=("Arial", 22),
            font=("Arial", 22),
        )
        self.combo_department = ctk.CTkComboBox(
            self,
            values=self.list_profession,
            width=365,
            height=50,
            dropdown_font=("Arial", 22),
            font=("Arial", 22),
        )

        self.button_start_exam = ctk.CTkButton(
            self,
            text="Начать тест",
            font=("Arial", 22),
            border_width=1,
            fg_color="#63c0f2",
            command=self.start_test,
        )

        self.put_widgets()

    def put_widgets(self):
        self.button_instructions.grid(
            row=0, column=3, padx=10, pady=10, ipadx=0, ipady=0
        )
        self.label_registration.grid(row=1, column=1, padx=20, pady=50)

        self.combo_profession.grid(row=5, column=1, padx=4, pady=4)
        self.combo_department.grid(row=6, column=1, padx=4, pady=4)
        self.button_start_exam.grid(row=7, column=1, padx=4, pady=4, ipadx=20, ipady=15)

    def start_test(self):
        self.master.view_frame_main()
        self.destroy()

    def back(self):
        self.destroy()
