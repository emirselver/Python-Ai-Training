#Faktöriyel Hesaplama:

# faktoriyel = int(input("Sayi giriniz: "))
# toplam = 1
# for i in range(1, faktoriyel + 1):
#     toplam *= i

# print(f"{faktoriyel}! işleminin sonucu {toplam}")

#Kullanıcıdan döngüyle sayı alınır --> 
# - Alınan her bir sayı tek tek listeye eklenir. 
# - Kullanıcı klavyeden "q" işareti girene kadar kullanıcıdan girdi almaya devam eder.
# - Sayı girme işlemi tamamlanınca listedeki elemanlardan çift olanlar toplanır ve tek olanların toplamına bölünür.
# - Sonuç ekrana yazdırılır. 

# sayilar = []
# tek_toplam = 0
# cift_toplam = 0


# while True:
#     sayi = input("Sayi giriniz: ")
#     if sayi == "q":
#         print("Çıkış yapılıyor\n")
#         for sayi_kontrol in sayilar:
#             if sayi_kontrol % 2 == 0:
#                 cift_toplam += sayi_kontrol
#             else:
#                 tek_toplam += sayi_kontrol
#         break
    
#     else:
#         sayilar.append(int(sayi))

# print(f"Listedeki çift sayıların toplamı: {cift_toplam}\n")
# print(f"Listedeki tek sayıların toplamı: {tek_toplam}\n")
# print(f"Listedeki çift sayıların toplamının tek sayıların toplamına bölümü: {cift_toplam / tek_toplam}")





#if tek_toplam == 0:
#    print("Tek sayıların toplamı 0 olduğundan tanımsızlık oluştu!!")
#else:
#    print(f"Listedeki çift sayıların toplamının tek sayıların toplamına bölümü: {cift_toplam / tek_toplam}")

#----------------------# ÇÖZÜM #----------------------#



sayilar = []
cift_toplam = 0
tek_toplam = 0

while True:
    sayi = input("Sayi giriniz: ")

    if sayi == "q":
        print("Çıkış yapılıyor...")
        for sayi_kontrol in sayilar:
            if sayi_kontrol % 2 == 0:
                cift_toplam += sayi_kontrol
            else:
                tek_toplam += sayi_kontrol
        break
    else:
        sayilar.append(int(sayi))

if tek_toplam == 0:
    print("Tek sayıların toplamı 0 olduğu için tanımsızlık durumu mevcut!")
else:
    print(f"Çift sayıların toplamı: {cift_toplam}\n")
    print(f"Tek sayıların toplamı: {tek_toplam}\n")
    print(f"Listedeki çift sayıların toplamının tek sayıların toplamına bölümü {cift_toplam / tek_toplam}")


















