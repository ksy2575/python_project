from lostark_practice_using_mvc.model import *
from lostark_practice_using_mvc.controller.controller import *
from lostark_practice_using_mvc.view.view import *

def main():
    print("main start")
    v = View()
    c = Controller(v)
    c.run()

if __name__ == "__main__":
    main()