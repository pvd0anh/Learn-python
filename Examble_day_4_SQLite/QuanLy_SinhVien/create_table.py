import sqlite3

conn = sqlite3.connect("qlsinhvien.db")

scrip = open('create_tables.sql','r',encoding='UTF-8')
script = scrip.read()
conn.executescript(script)
conn.commit()
conn.close()
scrip.close()