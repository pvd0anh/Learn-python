import json
import pprint

f = open("dang_1_doi_tuong.json", encoding="UTF-8")
sinh_vien = json.load(f)
f.close()
print(type(sinh_vien))

# ff = pprint.PrettyPrinter(indent=4)
# ff.pprint(f)
# pprint(sinh_vien)

for thuoc_tinh in sinh_vien:
    print(thuoc_tinh, ":", sinh_vien[thuoc_tinh])

# print("\n")
#
for thuoc_tinh, gia_tri in sinh_vien.items():  # tương tự như distionary, giá trị 1 là key, giá trị 2 là value
    print(thuoc_tinh, ":", gia_tri)
