import xml.dom.minidom
import pandas as pd

Bang_tigia = xml.dom.minidom.parse("bang_ty_gia.xml")
Nut_goc = Bang_tigia.documentElement
Cac_nut = Nut_goc.getElementsByTagName("Exrate")

print(str.ljust("Mã", 5) + str.ljust("Tên", 25) +
      str.center("Mua Vào", 20) +
      str.center("Bán ra", 20))
columns = ['Mã', 'Tên', 'Mua', 'Bán']

Code = []
Name = []
Buy = []
Sell = []
for Noi_dung in Cac_nut:
    CurrencyCode = Noi_dung.getAttribute("CurrencyCode")
    CurrencyName = Noi_dung.getAttribute("CurrencyName")
    Buy_t = Noi_dung.getAttribute("Buy")
    Sell_t = Noi_dung.getAttribute("Sell")

    Code.append(CurrencyCode)
    Name.append(CurrencyName)
    Sell.append(Sell_t)
    Buy.append(Buy_t)
    # print("-" * 30)
    # print("Code:",CurrencyCode)
    # print("Name:",CurrencyName)
    # print("Buy:","{:,.2f} VNĐ".format(float(Buy)))
    # print("Sell:","{:,.2f} VNĐ".format(float(Sell)))
    # print("-" * 30)

    print(str.ljust(CurrencyCode, 5) + str.ljust(CurrencyName, 25) +
          str.rjust("{:,.2f} VNĐ".format(float(Buy_t)), 20) +
          str.rjust("{:,.2f} VNĐ".format(float(Sell_t)), 20))
    inn = pd.DataFrame(dict(Ma = Code, Ten = Name, Mua = Buy, Ban = Sell))
print(inn)
