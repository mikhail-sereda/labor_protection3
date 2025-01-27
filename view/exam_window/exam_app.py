import customtkinter as ctk
from CTkMessagebox import CTkMessagebox

from view.exam_window.farme_registration import FrameRegistration
from view.exam_window.frame_test import FrameTest


class ExamWindowApp(ctk.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.geometry("400x300")
        self.geometry(f"{self.winfo_screenwidth()}x{self.winfo_screenheight()}+0+0")
        self.attributes("-topmost", True)
        self.title("Экзамен по охране труда")
        self.protocol("WM_DELETE_WINDOW", self.show_warning)

        self.frame_registration = None

        self.view_frame_registration()

    def view_frame_registration(self):
        self.frame_registration = FrameRegistration(self)
        self.frame_registration.pack(expand=True, fill="both")

    def view_frame_test(self):
        self.frame_registration = FrameTest(self)
        self.frame_registration.pack(expand=True, fill="both")

    def show_warning(self):
        # Show some retry/cancel warnings
        self.msg = CTkMessagebox(
            title="Завершить экзамен?",
            message="Закрыть окно экзамена?\n"
            "Незавершённая проверка знаний не будет "
            "сохранена!\n"
            "Выйти из экзамена?",
            icon="warning",
            option_1="Нет",
            option_2="Выйти",
        )

        if self.msg.get() == "Выйти":
            self.exit_exam()

    def exit_exam(self):
        self.destroy()
        self.master.frame_main.button_start.configure(state="normal")
        self.master.frame_main.button_settings.configure(state="normal")
