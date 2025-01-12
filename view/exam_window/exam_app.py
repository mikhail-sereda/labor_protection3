import customtkinter as ctk
from CTkMessagebox import CTkMessagebox


from view.frame_main import FrameMain


class ExamWindowApp(ctk.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.geometry("400x300")
        self.geometry(f"{self.winfo_screenwidth()}x{self.winfo_screenheight()}+0+0")
        self.attributes("-topmost", True)
        self.protocol("WM_DELETE_WINDOW", self.show_warning)

        self.label = ctk.CTkLabel(self, text="ToplevelWindow")
        self.label.pack()

    def show_warning(self):
        # Show some retry/cancel warnings
        self.msg = CTkMessagebox(title="Завершить экзамен?", message="Закрыть окно экзамена?\n"
                                                                     "Незавершённая проверка знаний не будет "
                                                                     "сохранена!\n"
                                                                     "Выйти из экзамена?",
                                 icon="warning", option_1="Нет", option_2="Выйти")

        if self.msg.get() == "Выйти":
            self.exit_exam()

    def exit_exam(self):
        self.message = CTkMessagebox

        self.destroy()
        self.master.frame_main.button_start.configure(state="normal")
        self.master.frame_main.button_settings.configure(state="normal")
