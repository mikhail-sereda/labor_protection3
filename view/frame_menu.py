import customtkinter as ctk
from PIL import Image


class FrameMenu(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.master = master
        self.ico_arrow = ctk.CTkImage(light_image=Image.open("static/img/arrow_back.png"),
                                        dark_image=Image.open("static/img/arrow_back.png"),
                                        size=(130, 35))
        self.configure()

        self.label_main = ctk.CTkLabel(self,
                                       text='Проверка знаний по охране труда',
                                       font=('Arial', 32, "bold"))
        self.button_exam_setting = ctk.CTkButton(self, text="Настройка экзамена",
                                                 font=('Arial', 22),
                                                 border_width=1, fg_color="#63c0f2",
                                                 width=350, height=50,
                                                 command=None)
        self.button_questions_setting = ctk.CTkButton(self, text="Вопросы",
                                                      font=('Arial', 22),
                                                      border_width=1, fg_color="#63c0f2",
                                                      width=350, height=50,
                                                      command=None)
        self.button_archive_setting = ctk.CTkButton(self, text="Архив",
                                                    font=('Arial', 22),
                                                    border_width=1, fg_color="#63c0f2",
                                                    width=350, height=50,
                                                    command=None)
        self.button_back_setting = ctk.CTkButton(self, text="", image=self.ico_arrow,
                                                 font=('Arial', 22),
                                                 border_width=1, fg_color="#63c0f2",
                                                 width=350, height=50,
                                                 command=self.back)

        self.put_widgets()

    def put_widgets(self):
        self.label_main.pack(padx=50,
                             pady=50)
        self.button_exam_setting.pack(expand=True, ipadx=20, ipady=15)
        self.button_questions_setting.pack(expand=True, ipadx=20, ipady=15)
        self.button_archive_setting.pack(expand=True, ipadx=20, ipady=15)
        self.button_back_setting.pack(expand=True, ipadx=20, ipady=15)

    def back(self):
        self.master.view_frame_main()
        self.destroy()
