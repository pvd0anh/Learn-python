'''
mục đích: test các biến cố, xem cách hoạt động với file .xml
'''

import xml.sax


class MyClass(xml.sax.ContentHandler):
    def __init__(self):
        self.ten = ""
        self.nam = ""
        self.Nuoc = ""

    def startElement(self, tag, attributes):
        if tag == "Bai_Hat":
            self.ten = attributes["ten"]
            self.nam = attributes["nam"]
            self.Nuoc = attributes["nuoc"]

    def endElement(self, tag):
        if tag == "Bai_Hat":
            print("*" * 30)
            print("Ten: ", self.ten)
            print("Nam: ", self.nam)
            print("nuoc: ", self.Nuoc)
            print("*" * 30)


if __name__ == "__main__":
    parser = xml.sax.make_parser()  # tạo ra một phân tích , phải cần 1 người phân tích file xml
    xu_ly = MyClass()
    parser.setContentHandler(xu_ly)
    parser.parse("bai_hat.xml")
