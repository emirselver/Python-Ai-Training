
# #CLASS - NESNE TÜRETME:

# class Araba:
#     def __init__(self, marka, model, yil):
#         self.marka = marka
#         self.model = model
#         self.yil = yil

#     def bilgileri_goster(self):
#         return f"Marka: {self.marka} - Model: {self.model} - Yıl: {self.yil}"


# #NESNE TÜRETME:

# araba1 = Araba("Toyota","Corolla",2020)
# print(araba1.bilgileri_goster())


# #KALITIM:

# class ElektrikliAraba(Araba):
#     def __init__(self,marka, model, yil, batarya_kapasitesi):
#         super().__init__(marka, model, yil)
#         self.batarya_kapasitesi = batarya_kapasitesi

#     def bilgileri_goster(self):
#         bilgi = super().bilgileri_goster()
#         return f"{bilgi}, Batarya Kapasitesi {self.batarya_kapasitesi} kwh"

# elektrikli_araba = ElektrikliAraba("Tesla","Model 3",2024,40)
# print(elektrikli_araba.bilgileri_goster())

#KAPSÜLLEME:

# class Personel:
#     def __init__(self, ad, yas):
#         self.ad = ad
#         self.__yas = yas

#     def yas_goster(self):
#         return self.__yas
    
#     def yas_guncelle(self, yeni_yas):
#         if yeni_yas > self.__yas:
#             self.__yas = yeni_yas

# calisan = Personel("Ahmet", 25)
# print(calisan.yas)


#BANKA SİMÜLASYONU:
import random
import time

class Banka:

    def __init__(self):
        pass

    def hesap_olusutur(self):
        self.ad = input("Adınız: ")
        self.soyad = input("Soyadınız: ")
        self.tc = int(input("T.C Giriniz: "))

        self.hesap_numarasi = random.randint(100000,999999)
        self.bakiye = 100

        print(f"Hesap Oluşturma İşlemi Başarılı! Ad: {self.ad} - Soyad: {self.soyad} - Hesap Numarası: {self.hesap_numarasi}")
        print(f"Hesap açmaya özel tanımlanan bakiye tutarı: {self.bakiye} TL")

    def para_cek(self):
        while True:
            tutar = int(input("Lütfen çekmek istediğiniz tutarı giriniz: "))
            if tutar > self.bakiye:
                print("Çekmek istediğiniz tutar bakiyenizden fazla olamaz!")
            else:
                self.bakiye -= tutar
                print(f"Para çekme işlemi sonrası bakiyeniz: {self.bakiye} TL ")
                break

    def para_yatir(self):
        tutar = int(input("Lütfen yatırmak istediğiniz tutarı giriniz: "))
        self.bakiye += tutar
        print(f"Para yatırma işlemi sonrası bakiyeniz: {self.bakiye} TL ")

    def bilgileri_goster(self):
        print(f"Ad: {self.ad} - Soyad: {self.soyad} - Hesap Numarası: {self.hesap_numarasi}")
        print(f"Bakiyeniz: {self.bakiye} TL")


musteri1 = Banka()
musteri1.hesap_olusutur()
time.sleep(5)
musteri1.para_yatir()
time.sleep(5)
musteri1.para_cek()
time.sleep(5)
musteri1.bilgileri_goster()
time.sleep(5)
print("program sonlandı...")
