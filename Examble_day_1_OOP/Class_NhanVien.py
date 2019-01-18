"""
class Nhan Vien
    first name, last name, date into, lương

in thông tin: in hồ sơ; in dòng
"""
import datetime


class NhanVien:
    def __init__(self, ho, ten, ngay_vaolam, luong):
        self.ho = ho
        self.ten = ten
        self.ngay_vaolam = ngay_vaolam
        self.luong = luong

    def in_hoso(self):
        print("-" * 25)
        print("Họ Tên: ", self.ho + " " + self.ten)
        print("Ngày vào: ", self.ngay_vaolam.strftime("%d/%m/%Y"))
        print("Lương: ", "{:,.2f}$".format(self.luong))
        print("-" * 25)


if __name__ == "__main__":
    danh_sach_NhanVien = []
    danh_sach_NhanVien.append(NhanVien("Pham", "Doanh", datetime.date(1996, 5, 29), 1200))
    danh_sach_NhanVien.append(NhanVien("Pham", "Van", datetime.date(1111, 2, 2), 222.232))

    Tong_luong = 0

    for nhanvien in danh_sach_NhanVien:
        nhanvien.in_hoso()
        Tong_luong += nhanvien.luong
    print("Tổng lương: ","{:,.3f}$".format(Tong_luong))
