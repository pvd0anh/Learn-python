class ConNguoi:
    def __init__(self, Ho_Ten, Gioi_Tinh, Ngay_Sinh):
        self.Ho_Ten = Ho_Ten
        self.Gioi_Tinh = Gioi_Tinh
        self.Ngay_Sinh = Ngay_Sinh

    def in_thong_tin(self):
        print("Ho ten:", self.Ho_Ten)
        print("Gioi Tinh:", self.Gioi_Tinh)
        print("Ngay Sinh:", self.Ngay_Sinh)

    def __str__(self):  # hàm trả về chuỗi của một object
        return "Người:" + self.Ho_Ten


class NhanVien(ConNguoi):
    Muc_luong_co_ban = 1390

    def __init__(self, ho_ten, gioi_tinh, ngay_sinh, ma_so, he_so_luong):
        ConNguoi.__init__(self, ho_ten, gioi_tinh, ngay_sinh)
        self.ma_so = ma_so
        self.he_so_luong = he_so_luong

    def in_thong_tin(self):
        ConNguoi.in_thong_tin(self)
        print("Ma So:", self.ma_so)
        print("He so luong:", self.he_so_luong)
        print("Tien Luong:", "{:,.2f}".format(self.Tinh_Luong(), ))

    def Tinh_Luong(self):
        tien_luong = NhanVien.Muc_luong_co_ban * self.he_so_luong
        return tien_luong


if __name__ == "__main__":
    # NhanVien.Muc_luong_co_ban += 50
    # print("muc luong co ban", NhanVien.Muc_luong_co_ban)
    nguoi = ConNguoi("Pham Van Doanh", True, "29/05/1996")
    # nguoi.in_thong_tin()
    # NhanVien.Muc_luong_co_ban += 50
    # print("muc luong co ban", NhanVien.Muc_luong_co_ban)
    # print("_"*20)
    # nhanvien = NhanVien("PVD",True,"29/05/1996","A01",12.5)
    # nhanvien.in_thong_tin()
    # print("_" * 20)

    print(nguoi)
