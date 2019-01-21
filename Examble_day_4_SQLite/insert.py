import  sqlite3

conn = sqlite3.connect("qlsinhvien.db")
#nhap ma so, ho, ten, ma khoa
ma_so = input("Ma Sinh vien:")
Ho = input("Ho:")
Ten = input("Ten:")
Ma_khoa = input("Ma Khoa:")

#kiem tra
if ma_so == "":
    print("Phải nhập mã số!")
    exit()
print(ma_so)
sql = "select * from sinh_vien where upper(ma_so)=?"
cursor = conn.execute(sql,(ma_so.upper(),)) #upper để in hoa dữ liệu lên
rows = cursor.fetchall()
if len(rows)>0:
    print("Mã số bị trùng")
    exit()
#them
sql = "insert into sinh_vien (ma_so, ho, ten,ma_khoa)" \
      "values(?,?,?,?)"

conn.execute(sql,(ma_so,Ho, Ten, Ma_khoa))
conn.commit()
conn.close()