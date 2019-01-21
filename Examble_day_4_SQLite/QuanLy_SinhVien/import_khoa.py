import sqlite3

conn = sqlite3.connect("qlsinhvien.db")
f = open("khoa.txt", "r", encoding="utf-8")
for l in f:
    l = l.strip()
    sql = "insert into khoa values(?,?)"
    a = l.split(",")
    conn.execute(sql, (a[0].strip(), a[1].strip()))
conn.commit()                       
f.close()
conn.close()
