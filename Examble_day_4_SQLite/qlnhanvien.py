import sqlite3

# mở kết nối
conn = sqlite3.connect("QL_NV.db")
print("ket noi thanh cong")

# xóa table
sql = "DROP TABLE PHONG_BAN"
conn.execute(sql)
# tạo table
sql = "create table PHONG_BAN( id integer primary key autoincrement, " \
      "Ma_Phong TEXT not null unique, " \
      "ten_phong text not null)"
conn.execute(sql)

sql = "insert into PHONG_BAN(Ma_Phong,ten_phong) values(?,?)"
conn.execute(sql, ("kk", "ket ket"))
conn.execute(sql, ("cc", "ka ka"))
conn.commit()
# đóng kết nối
conn.close()
