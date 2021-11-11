from tkinter import *
from tkinter import font
from tkinter import ttk
# from tkinter.ttk import *
from PIL import Image, ImageTk
window = Tk()
window.title("로스트아크 제작 효율 계산기")
window.geometry("640x400+100+100")
window.resizable(False, False)


# img = Image.open(r'.\0_source\done.png')
# resized_img = img.resize((16, 16))
# resized_img.save(r'.\0_source\button_done_16x16.png')


################################
#       윗부분 프레임            #
################################
upperFrame = Frame(window, bd=1)
upperFrame.grid(row=0, column=0)
logo = Canvas(upperFrame, width=240, height=66)

# logo.place(x=5, y=5, width=50, height=50)
# logo.pack(side="top", anchor="w")
# title = Label(window, text='제작 효율 계산기', height=3, font=font.Font(family="Lucida Grande", size=20))

logoImage = PhotoImage(file='0_source\lostark_logo_240x66.png')
logo.create_image(5, 5, anchor=NW, image=logoImage)
logo.grid(row=0, column=0)

titleFrame = Frame(upperFrame, bd=1)
titleFrame.grid(row=0, column=1, padx=3)

title0 = Label(titleFrame)
title0.grid(row=0, column=0, padx=3)
title = Label(titleFrame, text='제작 효율 계산기', font=font.Font(size=12))
title.grid(row=1, column=0, padx=3, sticky="s")
title2 = Label(titleFrame, text='ver0.1', font=font.Font(size=8))
title2.grid(row=2, column=0, pady=3)


buttonCurrPrice = Button(upperFrame, text='현재가 확인', fg='black', bg='lightgray', width=15, height=3)
buttonLatestPrice = Button(upperFrame, text='시세 그래프', fg='black', bg='lightgray', width=15, height=3)


buttonCurrPrice.grid(row=0, column=2, padx=10)
buttonLatestPrice.grid(row=0, column=3, sticky="e")


################################
#       밑부분 프레임            #
################################
lowerFrame = Frame(window, bd=1, bg="lightblue")
lowerFrame.grid(row=1, column=0, sticky="ewsn")

listbox = Listbox(lowerFrame, selectmode='extended', width=20, height=18)
listbox.insert(0, "고급 회복약")
listbox.insert(1, "정령의 회복약")
listbox.insert(2, "중급 오레하 재료")
listbox.insert(3, "명예의 돌파석")
listbox.grid(row=0, column=0, padx=2, pady=19, sticky="wns")
# 나중에 scrollbar 연결하기 - frame으로

resultFrame = Frame(lowerFrame, relief="solid", bd=1, bg='pink', width=480)
resultFrame.grid(row=0, column=1, padx=3, pady=19, sticky="ewsn")

# graphCanvas = Canvas(resultFrame, width=240, height=66)
# logoImage = PhotoImage(file='.\0_source\lostark_logo_240x66.png')
# logo.create_image(5, 5, anchor=NW, image=logoImage)
# graphCanvas.grid(row=0, column=0, sticky="n")
# lowerFrame.grid_rowconfigure(0, weight=1)
# lowerFrame.grid_rowconfigure(1, weight=100)



################################
#       메시지 프레임            #
################################
messageFrame = Frame(resultFrame, relief="solid")
messageFrame.place(x=480, y=290, height=20, anchor="se")
# messageLable = Label(resultFrame, text='제작 효율 계산기', height=3, font=font.Font(size=12))
# buttonRefresh = Button(resultFrame, text='현재가 확인', fg='black', bg='lightgray', width=15, height=3)
buttonImage = PhotoImage(file=r'0_source\button_refresh_16x16.png')
buttonRefresh = Button(messageFrame, fg='black', bg='white', image=buttonImage)
messageLable = Label(messageFrame, text='제작 효율 계산기ver0.1', font=font.Font(size=8))

# messageLable.place(x=5, y=5, width=50, height=50)
# buttonRefresh.place(x=5, y=5, width=50, height=50)
buttonRefresh.pack(side='right', anchor="s")
messageLable.pack(side='right', anchor="s")


window.mainloop()


from tkinter import *

fenster = Tk()
fenster.title("Window")

def switch():
    if b1["state"] == "normal":
        b1["state"] = "disabled"
        b2["text"] = "enable"
    else:
        b1["state"] = "normal"
        b2["text"] = "disable"

#--Buttons
b1 = Button(fenster, text="Button", height=5, width=7)
b1.grid(row=0, column=0)

b2 = Button(text="disable", command=switch)
b2.grid(row=0, column=1)

fenster.mainloop()