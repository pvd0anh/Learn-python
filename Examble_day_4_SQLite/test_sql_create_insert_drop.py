import sqlite3

def input_work():
    command = ["Hiển thị danh sách sản phẩm",
               "Thêm sản phẩm mới",
               "Tìm kiếm thông tin sản phẩm theo tên",
               "Cập nhật sản phẩm",
               "Xóa sản phẩm theo tên"]
    print("Nhập công việc cần làm [Từ 1 đến 5]")
    for i in range(1, len(command) + 1, 1):
        print("\t", i, ":", command[i - 1])
    work = int(input())
    print(work)
    i = 1
    while work < 1 or work > 5:
        print("nhập lại công việc cần làm [số tự nhiên từ 1 đến 5]")
        work = int(input())
        i += 1
        if i > 5:
            print("Bạn đã nhập sai quá 5 lần \nbye bye baby")
            exit(0)
    print("ok man", work)
    return work

conn = sqlite3.connect("sql_test_statements.db")

work = input_work()
if work ==1:
    f = open('data_sql/sql_test_show.sql','r',encoding='utf-8')
    print("Thực hiện công việc: show data")
if work ==2:
    f = open('data_sql/sql_test_create.sql','r',encoding='utf-8')
    print("Thực hiện công việc: Create data")
    print(f)
if work ==3:
    f = open('data_sql/sql_test_search.sql','r',encoding='utf-8')
    print("Thực hiện công việc: Search data")
if work ==4:
    f = open('data_sql/sql_test_update.sql','r',encoding='utf-8')
    print("Thực hiện công việc: Update data")
if work ==5:
    f = open('data_sql/sql_test_drop.sql','r',encoding='utf-8')
    print("Thực hiện công việc: Drop data")

script = f.read()
conn.executescript(script)
conn.commit()
conn.close()