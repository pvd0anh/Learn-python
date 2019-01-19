import xml.dom.minidom
from xml.dom.minidom import parse

Tai_Lieu = xml.dom.minidom.parse("bai_hat_1.xml")  # tải file về để xử lý
Nut_goc = Tai_Lieu.documentElement  # lấy nút gốc

cac_nut = Nut_goc.getElementsByTagName("BAI_HAT")

for nut in cac_nut:
    ten = nut.getAttribute("ten")
    nam = nut.getAttribute("nam")
    nuoc = nut.getAttribute("nuoc")

    print("-" * 30)
    print("Tên:", ten)
    print("Năm:", nam)
    print("Nước:", nuoc)
    print("-" * 30)
