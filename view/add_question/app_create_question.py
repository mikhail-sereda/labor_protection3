import customtkinter as ctk
from CTkMessagebox import CTkMessagebox

from view.add_question.frame_create_question import FrameCreateQuestion
from view.exam_window.farme_registration import FrameRegistration
from view.exam_window.frame_test import FrameTest


class AppCreateQuestion(ctk.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("400x300")
        # self.geometry(f"{self.winfo_screenwidth()}x{self.winfo_screenheight()}+0+0")
        self.attributes("-topmost", True)
        self.title("Редактор вопроса")
        # self.protocol("WM_DELETE_WINDOW", self.show_warning)

        self.frame_create_question = None

        self.view_frame_create_question()

    def view_frame_create_question(self):
        self.frame_create_question = FrameCreateQuestion(self)
        self.frame_create_question.pack(expand=True, fill="both")

    # TODO Сделать проверку сохранения вопроса перед выходом
    # def show_warning(self):
    #     # Show some retry/cancel warnings
    #     self.msg = CTkMessagebox(
    #         title="Завершить экзамен?",
    #         message="Закрыть окно экзамена?\n"
    #         "Незавершённая проверка знаний не будет "
    #         "сохранена!\n"
    #         "Выйти из экзамена?",
    #         icon="warning",
    #         option_1="Нет",
    #         option_2="Выйти",
    #     )
    #
    #     if self.msg.get() == "Выйти":
    #         self.exit_exam()

    def exit_create_question(self):
        self.destroy()
