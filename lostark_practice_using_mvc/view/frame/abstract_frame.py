from tkinter import *
import abc


############################
#        추상 프레임         #
############################
# tkinter 위젯을 배치할 프레임들의 추상 메서드를 사전 정의

class AbstractFrame(Frame, metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def create_widgets(self):
        raise NotImplementedError

    @abc.abstractmethod
    def set_widgets(self):
        raise NotImplementedError
