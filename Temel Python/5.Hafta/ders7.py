#OOP - > Nesne Yönelimli Programlama:

#DRY - > Do Not Repeat Yourself

# class Araba:
#     def __init__(self, renk, marka, motor ):
#         self.renk = renk
#         self.marka = marka
#         self.motor = motor

#         self.araba_bilgileri = f"{self.marka} - {self.motor} - {self.renk}"

#     def bilgileri_goster(self):
#         print(self.araba_bilgileri)



# araba_mavi = Araba("Mavi","Audi","1.6")
# araba_mavi.bilgileri_goster()
# araba_beyaz = Araba("Beyaz","Audi","1.6")
# araba_beyaz.bilgileri_goster()

# class Ogrenci:
#     def __init__(self):
#         pass

#     def bilgi_al(self, ad, no, sinif):
#         self.ad = ad
#         self.no = no
#         self.sinif = sinif

#     def bilgileri_goster(self):
#         print(f"Öğrencinin Adı: {self.ad} ")
#         print(f"Öğrencinin No'su: {self.no} ")
#         print(f"Öğrencinin Sınıfı: {self.sinif} ")

# ogrenci1 = Ogrenci()
# ogrenci1.bilgi_al("Mehmet", 25, "5-B")
# ogrenci1.bilgileri_goster()

# print()

# ogrenci2 = Ogrenci()
# ogrenci2.bilgi_al("Ahmet",21,"6-C")
# ogrenci2.bilgileri_goster()
    

class Personel:
    def __init__(self,firma_adi):
        self.f_adi = firma_adi
        print(f"Hoş Geldiniz: {self.f_adi} ")
    
    def personel_ekle(self):
        self.ad = input("Adınız: ")
        self.soyad = input("Soyadınız: ")
        self.tc = int(input("T.C Giriniz: "))

    def maas_belirle(self):

        if self.tc % 2 == 0:
            self.maas = 5000

        else:
            self.maas = 10000

    def bilgileri_goster(self):
        self.maas_belirle()
        print(f"Personelin Adı: {self.ad} ")
        print(f"Personelin Soyadı: {self.soyad} ")
        print(f"Personelin Maaşı: {self.maas} ")

personel1 = Personel("Tesla")
personel1.personel_ekle()
personel1.bilgileri_goster()


print("--------------------------")

personel2 = Personel("Tesla")
personel2.personel_ekle()
personel2.bilgileri_goster()


