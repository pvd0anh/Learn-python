import sqlite3

conn = sqlite3.connect("qlsinhvien.db")
f = open("ket_qua.txt", "r", encoding="utf-8")
for l in f:
    l = l.strip()
    sql = "insert into ket_qua values(?,?,?)"
    a = l.split(",")
    conn.execute(sql, (a[0].strip(), a[1].strip(), a[2].strip()))
conn.commit()
f.close()
conn.close()
