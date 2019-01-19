# chỉ để test các biến cố
import xml.sax


class MyClass(xml.sax.ContentHandler):
    def __init__(self):
        self.ten = ""
        self.nam = ""
        self.nuoc = ""

    def startElement(self, tag, attributes):
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
            print("-"*30)

if __name__ == "__main__":
    parser = xml.sax.make_parser()
    xu_ly = MyClass()
    parser.setContentHandler(xu_ly)
    parser.parse("bai_hat_1.xml")
