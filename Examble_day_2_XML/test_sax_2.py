# chỉ để test các biến cố
import xml.sax


class MyClass(xml.sax.ContentHandler):
    def __init__(self):
        self.CurrentData = ""
        self.ten = ""
        self.nam = ""
        self.nuoc = ""
        self.the_loai = ""
        self.ca_si = ""

    def startElement(self, tag, attributes):
        self.CurrentData = tag
        if tag == "BAI_HAT":
            self.ten = attributes["ten"]
            self.nam = attributes["nam"]
            self.nuoc = attributes["nuoc"]

    def endElement(self, tag):
        if tag == "BAI_HAT":
            print("-"*30)
            print("Tên:", self.ten)
            print("Năm:", self.nam)
            print("Nước:", self.nuoc)
            print("Thể loại:", self.the_loai)
            print("Ca sĩ:", self.ca_si)
            print("-"*30)
        # print(self.CurrentData)
        self.CurrentData = ""

    def characters(self, content):
        if self.CurrentData == "THE_LOAI":
            self.the_loai = content
        elif self.CurrentData == "CA_SI":
            self.ca_si = content


if __name__ == "__main__":
    parser = xml.sax.make_parser()
    xu_ly = MyClass()
    parser.setContentHandler(xu_ly)
    parser.parse("bai_hat_2.xml")
