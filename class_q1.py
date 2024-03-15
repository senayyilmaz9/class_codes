class Ogrenci:
    def __init__(self,ogrenci_adi,ogrenci_soyadi,ogrenci_sinifi):
        self.ogrenci_adi = ogrenci_adi
        self.ogrenci_soyadi = ogrenci_soyadi
        self.ogrenci_sinifi = ogrenci_sinifi

class Soru:
    def net_sayisi(dogru_sayisi,yanlis_sayisi):
        if (dogru_sayisi + yanlis_sayisi>50 or yanlis_sayisi < 0 or dogru_sayisi < 0 ):
            print("Lütfen doğru değerleri giriniz.")
        else:
            net = dogru_sayisi - (yanlis_sayisi // 4)
            return net
    def hesapla(net):
        return net * 2

ogrenci_adi = input("Öğrenci adı: ")
ogrenci_soyadi = input("Öğrenci Soyadı: ")
ogrenci_sinifi = input("Öğrenci sınıfı: ")

dogru_sayisi = int(input("Doğru Sayısı: "))
yanlis_sayisi = int(input("Yanlış sayısı: "))

ogrenci = Ogrenci(ogrenci_adi,ogrenci_soyadi,ogrenci_sinifi)

net = Soru.net_sayisi(dogru_sayisi,yanlis_sayisi)
puan = Soru.hesapla(net)

print(f"Öğrenci : {ogrenci.ogrenci_adi} {ogrenci.ogrenci_soyadi}, Sınıf : {ogrenci.ogrenci_sinifi}")
print(f"Net : {net}, Puan : {puan}")