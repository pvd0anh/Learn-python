def In_tieu_de():
    print("Từ".ljust(20, " "), "Nghĩa".ljust(40, " "))
    print("==".ljust(20, " "), "=====".ljust(40, " "))


def In_tu(row):
    tu = row[0].strip()
    nghia = row[1].strip()
    print(tu.ljust(20, " "), nghia.ljust(40, " "))


def In_tu_dien(conn):
    # đọc
    sql = "SELECT * FROM TU_DIEN ORDER BY tu"
    cur = conn.execute(sql)
    rows = cur.fetchall()
    # in
    In_tieu_de()
    for row in rows:
        In_tu(row)
    print("Số từ:", len(rows))


def Tra_tu(conn):
    tu_tra = input("Từ muốn tra: ")
    if tu_tra.strip() == "":
        print("Bạn chưa nhập từ muốn tra!")
        return
    sql = "SELECT * FROM TU_DIEN WHERE UPPER(tu)=?"
    cur = conn.execute(sql, (tu_tra.upper(),))
    rows = cur.fetchall()
    if len(rows) > 0:
        In_tieu_de()
        for row in rows:
            In_tu(row)
    else:
        print("Không tìm thấy từ này!")


def Them_tu_moi(conn):
    tu_them = input("Từ muốn thêm mới: ")
    if tu_them.strip() == "":
        print("Bạn chưa nhập từ muốn thêm!")
        return
    nghia_them = input("Nghĩa: ")
    sql = "SELECT * FROM TU_DIEN WHERE tu=?"
    cur = conn.execute(sql, (tu_them,))
    rows = cur.fetchall()
    if len(rows) == 0:
        sql = "INSERT INTO TU_DIEN VALUES(?,?)"
        conn.execute(sql, (tu_them, nghia_them))
        conn.commit()
        print("Đã thêm thành công.")
    else:
        print("Đã có từ này!")


def Xoa_tu(conn):
    tu_xoa = input("Từ muốn xóa: ")
    if tu_xoa.strip() == "":
        print("Bạn chưa nhập từ muốn xóa!")
        return
    sql = "DELETE FROM TU_DIEN WHERE UPPER(tu)=?"
    cur = conn.execute(sql, (tu_xoa.upper(),))
    conn.commit()
    n = cur.rowcount
    if n > 0:
        print("Đã xóa thành công.")


def Sua_nghia_cua_tu(conn):
    tu_sua = input("Từ muốn sửa nghĩa: ")
    if tu_sua.strip() == "":
        print("Bạn chưa nhập từ muốn sửa!")
        return
    nghia_sua = input("Nghĩa mới: ")
    sql = "UPDATE TU_DIEN SET nghia=? WHERE UPPER(tu)=?"
    cur = conn.execute(sql, (nghia_sua, tu_sua.upper()))
    conn.commit()
    n = cur.rowcount
    if n > 0:
        print("Đã sửa thành công.")
