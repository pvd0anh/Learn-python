import math


class HINH:
    def Dien_Tich(self):
        pass

    def Chu_Vi(self):
        pass

    def inthongtin(self):
        print("Dien Tich: ", self.Dien_Tich())
        print("Chu vi: ", self.Chu_Vi())


class HINH_CHU_NHAT(HINH):
    def __init__(self, dai, rong):
        self.dai = dai
        self.rong = rong

    def Dien_Tich(self):
        return self.dai * self.rong

    def Chu_Vi(self):
        return (self.dai + self.rong) * 2


class HINH_VUONG(HINH):
    def __init__(self, canh):
        self.canh = canh

    def Dien_Tich(self):
        return self.canh * self.canh

    def Chu_Vi(self):
        return self.canh * 4


class HINH_TRON(HINH):
    def __init__(self, bankinh):
        self.r = bankinh

    def Dien_Tich(self):
        return math.pi * self.r * self.r

    def Chu_Vi(self):
        return 2 * math.pi * self.r


class HINH_TAM_GIAC(HINH):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def Dien_Tich(self):
        nuachuvi = self.Chu_vi() / 2  # đã tính chu vi ở trên nên dùng lại công thức heror
        return (math.sqrt(nuachuvi * (nuachuvi - self.a) * (nuachuvi - self.b) * (nuachuvi - self.c)))

    def Chu_Vi(self):
        return self.a + self.b + self.c
