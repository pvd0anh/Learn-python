import json


def Doc_tap_tin_json(duong_dan):
    f = open(duong_dan, "r", encoding="UTF-8")
    data = json.load(f)
    f.close()
    return data


def In_sinh_vien(sinh_vien):  # xử lý theo từng dictionary
    for thuoc_tinh, gia_tri in sinh_vien.items():  # phân chia key và value
        print(thuoc_tinh, ":", gia_tri)
    print("\n")


duong_dan = "dang_2_danh_sach.json"
danh_sach_sinh_vien = Doc_tap_tin_json(duong_dan)  # kiểu list

for sinh_vien in danh_sach_sinh_vien:  # trong  list có nhiều dictinary nên chia nhỏ ra để xly
    In_sinh_vien(sinh_vien)
