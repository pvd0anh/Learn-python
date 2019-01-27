import tkinter
from tkinter import messagebox

# tao cua so
win = tkinter.Tk()
win.title("My application 2019")
win.geometry("450x300")
# tao danh sach chua cac mon the thao
lst = ["Bơi lội", "Bóng đá", "Bóng bàn", "Bóng chuyền", "Cầu lông", "Thể hình"]
#

vars = [] #các biến trong vars là kiểu tkinter
for item in lst:
    vars.append(tkinter.IntVar())
for i in range(len(vars)):
    vars[i].set(1)
# Tạo checkbutton
i = 0
for item in lst:
    chk = tkinter.Checkbutton(win, text=item, variable=vars[i],
                              onvalue=1, offvalue=0)
    chk.pack(side=tkinter.LEFT)
    i += 1


# nut chon ket qua
def xl_xacnhan():
    str = ""
    for i in range(len(lst)):
        if vars[i].get() == 1:
            str += "\n- " + lst[i]
    if str == "":
        str = "Bạn không biết chơi môn thể thao nào."
    else:
        str = "Bạn chơi được:" + str
    messagebox.showinfo("Xác nhận", str)


#
btn_xacnhan = tkinter.Button(win, text="Xác nhận", command=xl_xacnhan)
btn_xacnhan.pack(side=tkinter.LEFT)
# hiện cửa sổ
win.mainloop()
