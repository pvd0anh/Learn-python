# danh ssách các món ăn có kèm theo đơn giá
# cho bieetscacs món được chọn và tiền phải trả

import tkinter
from tkinter import messagebox

win = tkinter.Tk()
win.title("My application 2019")
win.geometry("400x300")
#
danhsach_monan = ["Mì xào giòn", "Cơm gà xối mỡ", "Mì vịt tiềm", "Bò kho"]
danhsach_dongia = [40000, 25000, 120000, 40000]

lbMenu = tkinter.Listbox(win, selectmode=tkinter.MULTIPLE)
for i in range(len(danhsach_monan)):
    lbMenu.insert(tkinter.END, danhsach_monan[i])

lbMenu.grid(row=0, column=0)


def xl_dot_mon():
    ketqua = lbMenu.curselection()
    str_ = "Bạn đã chọn:"
    tong_tien = 0
    for item in ketqua:
        str_ += "\n" + lbMenu.get(item)
        tong_tien +=danhsach_dongia[item]
    # tính tiền

    # for i in range(len(ketqua)):
    #     for j in range(len(danhsach_monan)):
    #         if lbMenu.get(ketqua[i]) == danhsach_monan[j]:
    #             tong_tien += danhsach_dongia[j]
    str_ += "\nTổng tiền phải thanh toán: " + str((tong_tien)) + "VNĐ"
    messagebox.showinfo("Món ăn", str_)


btnDatMon = tkinter.Button(win, text="Đặt món", command=xl_dot_mon)
btnDatMon.grid(row=1, column=0)

win.mainloop()
