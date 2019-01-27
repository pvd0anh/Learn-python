import tkinter
from tkinter import messagebox

# tao cua so
win = tkinter.Tk()
win.title("My application 2019")
win.geometry("450x300")
#
text_1 = tkinter.StringVar()
text_2 = tkinter.StringVar()
text_3 = tkinter.StringVar()
text_4 = tkinter.StringVar()
text_5 = tkinter.StringVar()
#
text_1.set("Bơi lội")
text_2.set("Bóng đá")
text_3.set("Bóng bàn")
text_4.set("Bóng chuyền")
text_5.set("Cầu lồng")
#
var_1 = tkinter.IntVar()
var_2 = tkinter.IntVar()
var_3 = tkinter.IntVar()
var_4 = tkinter.IntVar()
var_5 = tkinter.IntVar()
#
var_1.set(1)
var_2.set(1)
# Tạo checkbutton
chk_1 = tkinter.Checkbutton(win, text=text_1.get(), variable=var_1,
                            onvalue=1, offvalue=0)
chk_2 = tkinter.Checkbutton(win, text=text_2.get(), variable=var_2,
                            onvalue=1, offvalue=0)
chk_3 = tkinter.Checkbutton(win, text=text_3.get(), variable=var_3,
                            onvalue=1, offvalue=0)
chk_4 = tkinter.Checkbutton(win, text=text_4.get(), variable=var_4,
                            onvalue=1, offvalue=0)
chk_5 = tkinter.Checkbutton(win, text=text_5.get(), variable=var_5,
                            onvalue=1, offvalue=0)

#
chk_1.pack(side=tkinter.LEFT)
chk_2.pack(side=tkinter.LEFT)
chk_3.pack(side=tkinter.LEFT)
chk_4.pack(side=tkinter.LEFT)
chk_5.pack(side=tkinter.LEFT)

#nut chon ket qua
def xl_xacnhan():
    str=""
    if var_1.get()==1:
        str+="\n- "+text_1.get()

    if var_2.get()==1:
        str+="\n- "+text_2.get()

    if var_3.get()==1:
        str+="\n- "+text_3.get()

    if var_4.get()==1:
        str+="\n-"+text_4.get()

    if var_5.get()==1:
        str+="\n- "+text_5.get()
    if  str=="":
        str="Bạn không biết chơi môn thể thao nào."
    else:
        str = "Bạn chơi được:" + str
    messagebox.showinfo("Xác nhận",str)

#
btn_xacnhan = tkinter.Button(win, text="Xác nhận",command =xl_xacnhan)
btn_xacnhan.pack(side=tkinter.LEFT)
# hiện cử sổ
win.mainloop()
