from lostark_practice_using_mvc.view.frame.main_frame import *
from lostark_practice_using_mvc.view.frame.lower_frame import *


class View:

    def __init__(self):
        print("class View initialized")
        self.root = Tk()
        self.controller = None
        
        # 많은 프레임들을 dict로 추적 및 관리
        self.frame_dict = {}
        # self.main_frame = None
        # self.upper_frame = None
        # self.lower_frame = None
        # self.button_frame = None
        # self.message_frame = None
        self.initialize_form()

    def initialize_form(self):
        print("start initialize Form")
        MainFrame(self.root, self)
        print("end initialize Form")
        print("in frame_dict :", list(self.frame_dict.keys()))

    def set_controller(self, controller):
        self.controller = controller

    def set_frames(self, frame_name, instance):
        self.frame_dict[frame_name] = instance


    def start_mainloop(self):
        # 둘 다 가능
        # tk.mainloop()
        self.root.mainloop()  # <- 컨트롤러 run에서 작동시키기