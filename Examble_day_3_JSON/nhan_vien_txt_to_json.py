import json


def trans_txt2dict(file):
    data = {}  # dictinary
    data['nhan_vien'] = []  # tạo 1 list trong dictinary
    # data['nhan_vien'] #cách truy cập 1 phần tử trong dictinary
    f = open(file, "r", encoding="utf-8")
    for line in f:
        line = line.strip()  # bỏ dấu cách và enter ở 2 bên string
        infor = line.split(",")  # tách từng phần tử bằng dấu ","
        ho = infor[0].strip()
        ten = infor[1].strip()
        luong = float(infor[2].strip())
        ngay_vao = infor[3].strip()

        # chuyển sang dữ liệu json
        # trong list chứa các dictionary
        data['nhan_vien'].append({'first_name': ho, 'last_name': ten, 'salary': luong, 'hire date': ngay_vao})
    f.close()
    return data


if __name__ == "__main__":
    data = trans_txt2dict("nhan_vien.txt")
    ff = open('nhan_vien.json', 'w', encoding="utf-8")
    json.dump(data, ff, indent=4)
    ff.close()

    # uodate ; sửa ;  xóa ; thêm data => đọc file json về rồi xử lý như là 1 dict hoặc list

    print(data)
