class Insan:
    def __init__(self):
        self.ad = "Senay"
        self.soyad = "Yılmaz"
        self.yas = 23
        self.ulke ="Türkiye"
        self.sehir = "İstanbul"
        self.yetenekler = []

    def kisi_bilgileri(self):
        return self.ad, self.soyad, self.yas, self.ulke, self.sehir
    def yetenek_ekle(self,yetenekler):
        self.yetenekler.append(yetenekler)

Insan1 = Insan()
print(Insan1.kisi_bilgileri())
Insan1.yetenek_ekle("bisiklete binmek")
Insan1.yetenek_ekle("Python")
print(Insan1.yetenekler)

