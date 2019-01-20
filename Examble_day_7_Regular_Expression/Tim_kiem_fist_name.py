import re

# tìm các fist name có tên là Fleaur
f = open("first_last_names.txt", 'r', encoding='UTF-8')
mau = r", Fleaur$"
for line in f:
    line = line.strip()
    ketqua = re.search(mau, line)
    if ketqua:
        print(line)
f.close()
print("\n")