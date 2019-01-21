import sqlite3

# mở kết nối
conn = sqlite3.connect("QL_SV.db")
print("ket noi thanh cong")

# xóa table
sql = "DROP TABLE users"
conn.execute(sql)
# tạo table
sql = "create table users( id integer primary key autoincrement, name text not null)"
conn.execute(sql)

# thêm users
sql = "insert into users(name) values('Tom')"
conn.execute(sql)

sql = "insert into users(name) values('Tep')"
conn.execute(sql)

sql = "insert into users(name) values('bong')"
conn.execute(sql)

conn.commit()

# thêm khác
sql = "insert into users(name) values(?)"
conn.execute(sql, ("miss lion",))
conn.commit()
# đóng kết nối
conn.close()
