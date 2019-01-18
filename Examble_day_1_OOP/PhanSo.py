class PhanSo:
    def __init__(self, tu_so, mau_so):
        self.tu_so, self.mau_so = tu_so, mau_so

    def __str__(self):
        return "Phan So:" + str(self.tu_so) + "/" + str(self.mau_so)

    def __add__(self, other):
        tu = self.tu_so * other.mau_so + other.tu_so * self.mau_so
        mau = self.mau_so * other.mau_so
        return PhanSo(tu, mau)


if __name__ == "__main__":
    ps_1 = PhanSo(2, 3)
    ps_2 = PhanSo(4, 5)

    print("Phan so 1:", ps_1)
    print("Phan so 2:", ps_2)

    ps_tong = ps_1 + ps_2
    print(ps_tong)
