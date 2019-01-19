import xml.dom.minidom

Tai_Lieu = xml.dom.minidom.parse("Bai_hat_2.xml")  # tải file về để xử lý
Nut_goc = Tai_Lieu.documentElement  # lấy nút gốc

cac_nut = Nut_goc.getElementsByTyagName("BAI_HAT")

for nut in cac_nut:
    ten = nut.getAttribute("ten")
    nam = nut.getAttribute("nam")
    nuoc = nut.getAttribute("nuoc")
    #
    nut_the_loai = nut.getElementsByTagName("THE_LOAI")[0]
    the_loai = nut_the_loai.childNodes[0].data

    nut_ca_si = nut.getElementsByTagName("CA_SI")[0]
    ca_si = nut_ca_si.childNodes[0].data

    print("-" * 30)
    print("Tên:", ten)
    print("Năm:", nam)
    print("Nước:", nuoc)
    print("Thể Loại:",the_loai)
    print("Ca Sĩ:",ca_si)
    print("-" * 30)