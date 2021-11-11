from collections import defaultdict
from selenium import webdriver
import csv
import time

class Product:
    def __init__(self, name):
        print("init", name)
        self.name = name
        self.curr_price = 0
        self.latest_price = 0

class Product_constructor:
    product_dict = defaultdict(Product)
    Recipe_dict = defaultdict(list)
    def __init__(self, directory):
        self.file_reader = open(directory, 'r')
        self.read_line()

    def read_line(self):
        csv_reader = csv.reader(self.file_reader)
        for line in csv_reader:
            print(line)
            self.create_product_dict(line)
        self.file_reader.close()


    def create_product_dict(self, line):
        for index in range(len(line)):
            curr = line[index]
            if index == 0:
                if curr not in self.product_dict:
                    self.product_dict[curr] = Product(curr)
                self.Recipe_dict[curr]
            elif not curr.isdigit():
                curr_name = curr
                if curr not in self.product_dict:
                    self.product_dict[curr] = Product(curr)
            elif curr_name != '' and curr.isdigit():
                curr_quantity = curr
                # print(curr_name, curr_quantity) # 득실 계산시 필요
                self.Recipe_dict[line[0]].append((curr_name, curr_quantity))

                curr_name = ''
            else:
                self.Recipe_dict[line[0]].append(curr)
        print('Recipe_dict :', self.Recipe_dict)
        print('')


class Crawler:
    def __init__(self):
        self.isReady = False
        options = webdriver.ChromeOptions()
        options.add_argument('headless')
        options.add_argument('window-size=1920x1080')
        options.add_argument("disable-gpu")
        self.chromedriver = '.\chromedriver\chromedriver.exe'
        self.driver = webdriver.Chrome(self.chromedriver, options=options)
        self.driver.get('https://lostark.game.onstove.com/Market')
        self.item_name_textfield = self.driver.find_element_by_xpath(
        "/html/body/div[2]/div/main/div/div[2]/div[2]/form/fieldset/div/div[1]/input")
        self.item_name_deleteBtn = self.driver.find_element_by_xpath(
        "/html/body/div[2]/div/main/div/div[2]/div[2]/form/fieldset/div/div[1]/button")
        self.searchBtn = self.driver.find_element_by_xpath(
            '/html/body/div[2]/div/main/div/div[2]/div[2]/form/fieldset/div/div[4]/button[1]')

        print("+" * 100)
        print(self.driver.title)
        print(self.driver.current_url)
        print("로아 거래소")
        print("-" * 100)

    def product_construct(self, product_dict):
        # if not self.isReady:
        #     time.sleep(1)
        for curr in product_dict:
            print(curr)
            self.item_name_textfield.send_keys(curr)
            self.searchBtn.click()
            time.sleep(1)
            self.table = self.driver.find_element_by_xpath('/html/body/div[2]/div/main/div/div[2]/div[2]/div/div/div[1]/table')
            self.tbody = self.table.find_element_by_tag_name("tbody")
            rows = self.tbody.find_elements_by_tag_name("tr")
            for row in enumerate(rows):
                index, value = row
                body = value.find_elements_by_tag_name("td")[0]
                cost = value.find_elements_by_tag_name("td")[3]
                if body.text.split('\n')[0] == curr:
                    print(index, body.text, cost.text)
            self.item_name_deleteBtn.click()

    def driver_quit(self):
        self.driver.quit()

constructor = Product_constructor('./practice.csv')
crawler = Crawler()
crawler.product_construct(constructor.product_dict)
print(constructor.product_dict)
crawler.driver_quit()