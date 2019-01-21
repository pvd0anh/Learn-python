import sqlite3

conn = sqlite3.connect("QL_NV.db")

f = open('create_nhan_vien.sql', 'r', encoding="UTF-8")
script = f.read()
conn.executescript(script)
f.close()
conn.close()
