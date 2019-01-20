import re

# tìm các last name bắt đầu bằng Ba
f = open("last_names.txt", 'r', encoding='UTF-8')
mau = r"^Ba"
for line in f:
    line = line.strip()
    ketqua = re.search(mau, line)
    if ketqua:
        print(line)
f.close()
print("\n")

# tim last name ket thuc bang nt
f = open("last_names.txt", 'r', encoding='UTF-8')
mau = r"nt$"
for line in f:
    line = line.strip()
    ketqua = re.search(mau, line)
    if ketqua:
        print(line)
f.close()

print("\n")

# tim last name có chứa ree
f = open("last_names.txt", 'r', encoding='UTF-8')
mau = r"ree"
for line in f:
    line = line.strip()
    ketqua = re.search(mau, line)
    if ketqua:
        print(line)
f.close()
