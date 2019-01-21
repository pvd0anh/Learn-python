# cho nhập các thông tin của một sinh viên khoa CN và thêm vào bảng sinh_vien
import sqlite3


def nhap_sinh_vien():
    # nhập ma_so, ho, ten, ma_khoa
    ma_so = input("Mã sinh viên: ")
    ho = input("Họ: ")
    ten = input("Tên: ")
    ma_khoa = input("Mã khoa: ")
    return (ma_so, ho, ten, ma_khoa)


def kiem_tra_sinh_vien(ma_so):
    # kiểm tra ma_so phải khác rỗng
    if ma_so == "":
        print("phải nhập mã số!")
        return False
    # kiểm tra ma_so phải duy nhất
    sql = "SELECT * FROM sinh_vien WHERE UPPER(ma_so)=?"
    cursor = conn.execute(sql, (ma_so.upper(),))
    rows = cursor.fetchall()
    if len(rows) > 0:
        print("Mã số bị trùng!")
        return False
    return True


def them_sinh_vien(ma_so, ho, ten, ma_khoa):
    sql = "INSERT INTO sinh_vien(ma_so,ho,ten,ma_khoa) VALUES(?,?,?,?)"
    conn.execute(sql, (ma_so, ho, ten, ma_khoa))
    conn.commit()


if __name__ == "__main__":
    conn = sqlite3.connect("qlsinhvien.db")

    ma_so, ho, ten, ma_khoa = nhap_sinh_vien()

    hop_le = kiem_tra_sinh_vien(ma_so)
    if hop_le:
        them_sinh_vien(ma_so, ho, ten, ma_khoa)

    conn.close()
