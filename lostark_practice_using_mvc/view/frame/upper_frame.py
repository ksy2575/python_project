from lostark_practice_using_mvc.view.frame.title_frame import *
from lostark_practice_using_mvc.view.frame.button_frame import *
from lostark_practice_using_mvc.view.frame.abstract_frame import *


class UpperFrame(AbstractFrame):

    def __init__(self, root, view):
        print("class UpperFrame initialized")
        super().__init__(root)
        self.view = view
        self.view.set_frames("upper_frame", self)

        self.grid()

        self.logo = None
        self.logo_image = None

        ############################
        #       타이틀 프레임        #
        ############################

        self.title_frame = TitleFrame(self)

        ############################
        #        버튼 프레임         #
        ############################

        self.button_frame = ButtonFrame(self, self.view)

        self.create_widgets()
        self.set_widgets()

    def create_widgets(self):
        self.logo = Label(self, width=240, height=66, anchor=NW)
        # self.logo_image = PhotoImage(file='0_source\lostark_logo_240x66.png',
        #                              master=self)
        # self.logo.create_image(5, 5, anchor=NW, image=self.logo_image)

    def set_widgets(self):
        self.logo.grid(row=0, column=0, pady=(10, 0))
