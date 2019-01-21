import sqlite3


if __name__ == "__main__":
    # mở kết nối
    conn = sqlite3.connect("qltratu.db")

    # yêu cầu 1: đọc và in danh sách các từ và nghĩa
    # đọc
    sql = "SELECT * FROM TU_DIEN"
    cur = conn.execute(sql)
    rows = cur.fetchall()
    # in
    print("Từ".ljust(20, " "), "Nghĩa".ljust(40, " "))
    print("==".ljust(20, " "), "=====".ljust(40, " "))
    for row in rows:
        tu = row[0].strip()
        nghia = row[1].strip()
        print(tu.ljust(20, " "), nghia.ljust(40, " "))

    # yêu cầu 2: nhập từ muốn tra và in ra các nghĩa của từ
    tu_tra = input("Từ muốn tra: ")
    sql = "SELECT * FROM TU_DIEN WHERE tu='" + tu_tra + "'"
    cur = conn.execute(sql)
    rows = cur.fetchall()
    if len(rows) > 0:
        print("Từ".ljust(20, " "), "Nghĩa".ljust(40, " "))
        print("==".ljust(20, " "), "=====".ljust(40, " "))
        for row in rows:
            tu = row[0].strip()
            nghia = row[1].strip()
            print(tu.ljust(20, " "), nghia.ljust(40, " "))
    else:
        print("Không tìm thấy từ này!")

    # yêu cầu 3: thêm một từ mới
    tu_them = input("Từ muốn thêm mới: ")
    nghia_them = input("Nghĩa: ")
    sql = "SELECT * FROM TU_DIEN WHERE tu='" + tu_them + "'"
    cur = conn.execute(sql)
    rows = cur.fetchall()
    if len(rows) == 0:
        sql = "INSERT INTO TU_DIEN VALUES(?,?)"
        conn.execute(sql, (tu_them, nghia_them))
        conn.commit()
        print("Đã thêm thành công.")
    else:
        print("Đã có từ này!")

    # yêu cầu 4: xóa một từ
    tu_xoa = input("Từ muốn xóa: ")
    sql = "DELETE FROM TU_DIEN WHERE tu=?"
    cur = conn.execute(sql, (tu_xoa,))
    conn.commit()
    n = cur.rowcount
    if n > 0:
        print("Đã xóa thành công.")
    # yêu cầu 5: sửa nghĩa của một từ
    tu_sua = input("Từ muốn sửa nghĩa: ")
    nghia_sua = input("Nghĩa mới: ")
    sql = "UPDATE TU_DIEN SET nghia=? WHERE tu=?"
    cur = conn.execute(sql, (nghia_sua, tu_sua))
    conn.commit()
    n = cur.rowcount
    if n > 0:
        print("Đã sửa thành công.")

    # đóng kết nối
    conn.close()
