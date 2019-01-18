from Nhan_Vien_lib import *  # cho sử dụng tất cả thư viện trong Nhan_Vien_lib mà không cần khai báo.

if __name__ == "__main__":
    # tạo danh sách nhân viên
    DanhSach_NhanVien = Khoi_tao_nhan_vien("nhan_vien.txt")

    # in danh sách nhân viên
    In_DanhSach_NhanVien(DanhSach_NhanVien)
