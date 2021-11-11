from lostark_practice_using_mvc.view.frame.abstract_frame import *
from lostark_practice_using_mvc.view.frame.result_frame import *
from lostark_practice_using_mvc.view.frame.message_frame import *


class LowerFrame(AbstractFrame):

    def __init__(self, root, view):
        print("class LowerFrame initialized")
        super().__init__(root)
        self.view = view
        self.view.set_frames("lower_frame", self)

        self.grid(row=1, column=0)

        self.listbox = None

        ############################
        #        결과 프레임         #
        ############################

        self.result_frame = ResultFrame(self, self.view, bg='pink', width=480)

        ############################
        #       메시지 프레임        #
        ############################

        self.message_frame = MessageFrame(self, self.view)

        self.create_widgets()
        self.set_widgets()

    def create_widgets(self):
        self.listbox = Listbox(self, selectmode='browse', width=20, height=18,
                               activestyle="none")
        # self.listbox.insert(0, "고급 회복약")
        # self.listbox.insert(1, "정령의 회복약")
        # self.listbox.insert(2, "중급 오레하 재료")
        # self.listbox.insert(3, "명예의 돌파석")
        # 나중에 scrollbar 연결하기 - frame으로

    def set_widgets(self):
        self.listbox.grid(row=0, column=0, padx=2, pady=(5, 0), sticky="wns")
