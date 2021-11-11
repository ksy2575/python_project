import csv
import pandas
from tkinter import PhotoImage

import lostark_practice_using_mvc.view.view as view
import lostark_practice_using_mvc.model.product as model


class Controller:
    # MODE STATES
    STATE_DEFAULT = 0
    STATE_CURR_PRICE = 1
    STATE_LATEST_PRICE = 2

    # CRAWLER STATES
    STATE_REFRESHABLE = 0
    STATE_CRAWLING = 1
    STATE_FINISHED = 2

    def __init__(self, my_view):
        print("class Controller initialized")
        
        # 유저의 선호 품목을 csv로 저장 및 불러오기,
        # 로스트아크의 전체 제작식을 DB로 사전에 저장 및 불러오기 <-무슨 DB?
        self.product_list = []
        self.product_dict = {}
        self.get_user_product_from_csv('./1_datas/user_products.csv')
        self.view = my_view
        self.view.set_controller(self)
        self.mode_state = self.STATE_DEFAULT

        # 현재 품목, None이면 도움말을 출력하도록 설계하기(default=None)
        self.curr_product = None

        # 이미지 할당 <- 많아지면 팩토리
        self.image_btn_refresh = PhotoImage(file=r'0_source\button_refresh_16x16.png')
        self.image_logo = PhotoImage(file='0_source\lostark_logo_240x66.png')
        self.set_image()

        self.set_list_box()
        
        # 초기 시작 시 크롤러를 돌리며 STATE_REFRESHABLE -> STATE_FINISHED로 변경하기
        self.crawler_state = self.STATE_REFRESHABLE
        self.bind_commands()

    # tk 메인 루프 시작(GUI 출력), 크롤러 시작
    def run(self):
        view.View.start_mainloop(self.view)

    def get_user_product_from_csv(self, directory):
        print("get_user_product_from_csv")
        try:
            file_reader = open(directory, 'r', encoding='UTF8')
        except FileNotFoundError:
            # 파일이 없다면 새로 생성
            temp_product_list = ['고급 회복약', '각성 각인서', '역천지체 각인서']
            self.save_user_product_to_csv(temp_product_list)
            file_reader = open(directory, 'r', encoding='UTF8')

        csv_reader = csv.reader(file_reader)
        for line in csv_reader:
            print(line)
            self.create_product_list(line[0])
        file_reader.close()

    def create_product_list(self, name):
        print("create_product_dict")
        if name.isdigit():
            pass
        else:
            self.product_list.append(name)
            self.product_dict[name] = model.Product(name)

    @staticmethod
    def save_user_product_to_csv(product_list):
        data_frame = pandas.DataFrame(product_list)
        data_frame.to_csv('./user_products.csv', index=False)

    def btn_curr_price_clicked(self):
        print("btn_curr_price_clicked")
        if self.mode_state == self.STATE_CURR_PRICE:
            self.mode_state = self.STATE_DEFAULT
        else:
            self.mode_state = self.STATE_CURR_PRICE
        self.btn_change_state()

    def btn_latest_price_clicked(self):
        print("btn_latest_price_clicked")
        if self.mode_state == self.STATE_LATEST_PRICE:
            self.mode_state = self.STATE_DEFAULT
        else:
            self.mode_state = self.STATE_LATEST_PRICE
        self.btn_change_state()

    def btn_change_state(self):
        print("btn_state :", self.mode_state)
        btn_curr_price = self.view.frame_dict["button_frame"].btn_curr_price
        btn_latest_price = self.view.frame_dict["button_frame"].btn_latest_price

        if self.mode_state == self.STATE_DEFAULT:
            btn_curr_price.configure(bg="lightgray")
            btn_latest_price.configure(bg="lightgray")
        elif self.mode_state == self.STATE_CURR_PRICE:
            btn_curr_price.configure(bg="gray")
            btn_latest_price.configure(bg="lightgray")
        elif self.mode_state == self.STATE_LATEST_PRICE:
            btn_curr_price.configure(bg="lightgray")
            btn_latest_price.configure(bg="gray")

    def btn_refresh_clicked(self):
        print("btn_refresh_clicked")
        #
        btn_refresh = self.view.frame_dict["message_frame"].btn_refresh
        print(self.image_btn_refresh)
        if self.crawler_state == self.STATE_REFRESHABLE:
            self.image_btn_refresh = PhotoImage(file=r'0_source\button_loading_16x16.png')
            self.crawler_state = self.STATE_CRAWLING
        elif self.crawler_state == self.STATE_CRAWLING:
            self.image_btn_refresh = PhotoImage(file=r'0_source\button_done_16x16.png')
            self.crawler_state = self.STATE_FINISHED
        elif self.crawler_state == self.STATE_FINISHED:
            self.image_btn_refresh = PhotoImage(file=r'0_source\button_refresh_16x16.png')
            self.crawler_state = self.STATE_REFRESHABLE

        btn_refresh.configure(image=self.image_btn_refresh)

    def listbox_clicked(self, event):
        w = event.widget
        index = w.curselection()[0]
        print(index)
        data = event.widget.get(index)
        print(data)


    def set_list_box(self):
        # 컨트롤러가 뷰의 각 위젯을 동작시키도록 설계
        # 그러기 위해서는 컨트롤러 - 뷰 : 단방향 연관 관계
        for i in range(len(self.product_list)):
            self.view.frame_dict["lower_frame"].listbox.insert(i, self.product_list[i])
        print("set_list_box finished")

    def bind_commands(self):
        # buttons
        btn_curr_price = self.view.frame_dict["button_frame"].btn_curr_price
        btn_latest_price = self.view.frame_dict["button_frame"].btn_latest_price
        btn_refresh = self.view.frame_dict["message_frame"].btn_refresh

        btn_curr_price.configure(command=self.btn_curr_price_clicked)
        btn_latest_price.configure(command=self.btn_latest_price_clicked)
        btn_refresh.configure(command=self.btn_refresh_clicked)

        # listbox
        listbox = self.view.frame_dict["lower_frame"].listbox
        listbox.bind("<<ListboxSelect>>", self.listbox_clicked)
        print("bind_commands finished")

    def set_image(self):
        btn_refresh = self.view.frame_dict["message_frame"].btn_refresh
        canvas_logo = self.view.frame_dict["upper_frame"].logo

        btn_refresh.configure(image=self.image_btn_refresh)
        canvas_logo.configure(image=self.image_logo)
