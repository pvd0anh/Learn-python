import xml.dom.minidom


def tao_nut_con(ten_nut_con, ten, nuoc, nam):
    nut_bai_hat = tai_lieu.createElement(ten_nut_con)
    Nut_goc.appendChild(nut_bai_hat)

    nut_con = tai_lieu.createElement("ten")
    nut_bai_hat.appendChild(nut_con)
    nut_con.appendChild(tai_lieu.createTextNode(ten))

    nut_con = tai_lieu.createElement("nước")
    nut_bai_hat.appendChild(nut_con)
    nut_con.appendChild(tai_lieu.createTextNode(nuoc))

    nut_con = tai_lieu.createElement("nam")
    nut_bai_hat.appendChild(nut_con)
    nut_con.appendChild(tai_lieu.createTextNode(nam))

    return nut_bai_hat


# tạo ra một object ( giống 1 kiểu dữ  liệu)
tai_lieu = xml.dom.minidom.Document()

# tạo nút gốc
Nut_goc = tai_lieu.createElement("DANH_SACH")
tai_lieu.appendChild(Nut_goc)

# tạo nút con
Nut_goc.appendChild(tao_nut_con("BAI_HAT", "hello", "my", "2001"))
Nut_goc.appendChild(tao_nut_con("BAI_HAT", "byebye", "anh", "2002"))
Nut_goc.appendChild(tao_nut_con("BAI_HAT", "hi", "phap", "2003"))

# ghi ra tập tin
f = open("Bai_hat_write.xml", mode="w", encoding="utf-8")
tai_lieu.writexml(f, indent="", addindent="\t", newl="\n")
f.close()
