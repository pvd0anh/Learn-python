import sqlite3
import my_lib
import menu_lib

if __name__ == "__main__":
    # mở kết nối
    conn = sqlite3.connect("qltratu.db")

    # thực đơn ứng dụng
    while True:
        chon = menu_lib.Hien_thuc_don()
        if chon == 1:
            my_lib.In_tu_dien(conn)
        elif chon == 2:
            my_lib.Tra_tu(conn)
        elif chon == 3:
            my_lib.Them_tu_moi(conn)
        elif chon == 4:
            my_lib.Sua_nghia_cua_tu(conn)
        elif chon == 5:
            my_lib.Xoa_tu(conn)
        elif chon == 6:
            break

    # đóng kết nối
    conn.close()
