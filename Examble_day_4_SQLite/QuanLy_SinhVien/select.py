import sqlite3

conn = sqlite3.connect("qlsinhvien.db")
# liệt kê các sinh viên khoa Công nghệ thông tin và sắp tăng theo tên
sql = "SELECT * FROM sinh_vien WHERE ma_khoa='CN' ORDER BY ten"
cursor = conn.execute(sql)
"""
for row in cursor:
    print('= '*20)
    print("Mã số:", row[0])
    print("Họ tên:", row[1], row[2])
    print('= '*20)
"""
rows = cursor.fetchall() # kiểu list
for row in rows:
    print('= '*20)
    print("Mã số:", row[0])
    print("Họ tên:", row[1], row[2])
    print('= '*20)

conn.close()
