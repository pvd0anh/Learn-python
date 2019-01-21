import sqlite3

conn = sqlite3.connect("qlsinhvien.db")
f = open("sinh_vien.txt", "r", encoding="utf-8")
for l in f:
    l = l.strip()
    sql = "insert into sinh_vien values(?,?,?,?,?,?,?,?,?,?)"
    a = l.split(",")
    gioi_tinh = "1"
    if a[3] == "False":
        gioi_tinh = "0"
    conn.execute(sql, (a[0].strip(), a[1].strip(), a[2].strip(), gioi_tinh, a[4]
                       [0:10], a[5].strip(), a[6].strip(), a[7].strip(), a[8].strip(), a[9].strip()))
conn.commit()                       
f.close()
conn.close()
