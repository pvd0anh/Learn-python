# cho nhập các thông tin của một sinh viên khoa CN và thêm vào bảng sinh_vien
import sqlite3

conn = sqlite3.connect("qlsinhvien.db")
# nhập ma_so, ho, ten, ma_khoa
ma_so = input("Mã sinh viên: ")
ho = input("Họ: ")
ten = input("Tên: ")
ma_khoa = input("Mã khoa: ")
# kiểm tra
if ma_so == "":
    print("Phải nhập mã số!")
    exit()

sql = "SELECT * FROM sinh_vien WHERE UPPER(ma_so)=?"
cursor = conn.execute(sql, (ma_so.upper(),))
rows = cursor.fetchall()
if len(rows) > 0:
    print("Mã số bị trùng!")
    exit()

# thêm
sql = "INSERT INTO sinh_vien(ma_so,ho,ten,ma_khoa) VALUES(?,?,?,?)"
conn.execute(sql, (ma_so, ho, ten, ma_khoa))

#
conn.commit()

conn.close()
