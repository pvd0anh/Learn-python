import sqlite3

conn = sqlite3.connect("qlsinhvien.db")
# liệt kê sinh viên tăng dần theo tên

sql = "SELECT * FROM sinh_vien where ma_khoa='CN' order by ten"
cursor = conn.execute(sql)
print(type(cursor))  # class

# for row in cursor:
#     print("*"*20)
#     print("Ma_so:",row[0])
#     print("Ho ten:",row[1], row[2])

rows = cursor.fetchall()
print(type(rows))  # list

for row in rows:
    print("*" * 20)
    print("Ma_so:", row[0])
    print("Ho ten:", row[1], row[2])

conn.close()
