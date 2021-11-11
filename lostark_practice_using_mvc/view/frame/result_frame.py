from lostark_practice_using_mvc.view.frame.abstract_frame import *
from tkinter import font


class ResultFrame(AbstractFrame):

    def __init__(self, root, view,  bg, width):
        print("class ResultFrame initialized")
        super().__init__(root, bg=bg, width=width)
        self.view = view
        self.view.set_frames("result_frame", self)

        self.grid(row=0, column=1, padx=3, pady=(5, 0), sticky="ewsn")

        self.image = None
        self.result_label = None

        self.create_widgets()
        self.set_widgets()

    def create_widgets(self):
        self.result_label = Label(self, text='결과 출력단입니다.',
                                  font=font.Font(size=11), compound="top")

    def set_widgets(self):
        self.result_label.grid(row=0, column=0)

    def clear_board(self):
        print("clear_board")
        # self.result_label.
