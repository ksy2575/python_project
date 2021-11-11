from lostark_practice_using_mvc.view.frame.abstract_frame import *
from tkinter import font

STATE_LOADING = 0
STATE_REFRESH = 1
STATE_COMPLETE = 2


class MessageFrame(AbstractFrame):

    def __init__(self, root, view):
        print("class MessageFrame initialized")
        super().__init__(root)
        self.view = view
        self.view.set_frames("message_frame", self)

        self.grid(row=1, column=1, padx=3, sticky="ewsn")

        self.btn_refresh = None
        self.message_label = None

        self.create_widgets()
        self.set_widgets()

    def create_widgets(self):
        self.btn_refresh = Button(self)
        self.message_label = Label(self, text='메시지 출력단입니다.',
                                   font=font.Font(size=8), width=65, anchor="e")

    def set_widgets(self):
        self.message_label.grid(row=0, column=0, padx=0, pady=0)
        self.btn_refresh.grid(row=0, column=1, padx=0, pady=0)
