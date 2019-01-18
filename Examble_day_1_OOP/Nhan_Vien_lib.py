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


def Tao_NhanVien(data):
    infors = data.split(",")  # tách từng data bằng dấu ","
    ho = infors[0].strip()  # bỏ dấu cách
    ten = infors[1].strip()
    luong = float(infors[2].strip())  # ngày/tháng/năm => %d  /  %m  / %Y
    ngay_vaolam = datetime.datetime.strptime(infors[3].strip(), "%d/%m/%Y")  # đổi sang kiểu ngày từ kiểu chuỗi

    return NhanVien(ho, ten, ngay_vaolam, luong)


def Khoi_tao_nhan_vien(ten_tap_tin):
    f = open(ten_tap_tin, "r", encoding="utf-8")
    DanhSach_NhanVien = []
    for line in f:
        data = line.strip()  # bỏ dấu cách 2 bên của string
        NhanVien = Tao_NhanVien(data)

        DanhSach_NhanVien.append(NhanVien)
    f.close()
    return DanhSach_NhanVien


def In_DanhSach_NhanVien(DanhSach_NhanVien):
    Tong_luong = 0
    for nhanvien in DanhSach_NhanVien:
        nhanvien.in_hoso()
        Tong_luong += nhanvien.luong
    print("Tổng số nhân viên:", len(DanhSach_NhanVien))
    print("Tổng lương:", "{:,.2f}$".format(Tong_luong))
