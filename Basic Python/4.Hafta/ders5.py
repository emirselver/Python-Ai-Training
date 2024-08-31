# def kare_al(x):
#     sonuc = x ** 2
#     return sonuc
#     # print(sonuc)

# deger = kare_al(5)
# # print(deger)


# def selamla(isim):
#     print("merhaba ",isim)

# # ad = input("adınız: ")

# selamla(isim="ahmet")

#ASAL SAYI BULAN FONKSİYON


# def asal_sayi_bulma(sayi):
    
#     if sayi <= 1:
#         return False

#     else:
#         for i in range(2, sayi):
#             if sayi % i == 0:
#                 return False

#         return True
 
# sayi_gir = int(input("sayi gir: "))
# sonuc = asal_sayi_bulma(sayi_gir)

# if sonuc == True:
#     print(f"{sayi_gir} sayısı asal sayidir.")

# else:
#     print(f"{sayi_gir} sayısı asal sayi degildir.")



# def sayilari_carp(sayi1, sayi2 = 1):
#     sonuc = sayi1 * sayi2
#     print(sonuc)

# sayilari_carp(5,10)

#ALAN HESAPLAMA:
# 

def programi_calistir():

    def islem_menuleri():
        print("1. Karenin Alanını Hesapla")
        print("2. Dikdörgenin Alanını Hesapla")

    def kare_alani(kenar1, kenar2):

        if kenar1 == kenar2:
            alan = kenar1 * kenar2
            print("Karenin alanı: ", alan)

        else:
            print("Hatalı islem! Karenin kenarlari birbirine esit degil!")

    def dikdortgen_alani(uzun_kenar, kisa_kenar):
        
        alan = uzun_kenar * kisa_kenar
        print("Dikdörtgenin alani:" , alan)

    def kenarlari_al():
        kenar1 = int(input("1.Kenar: "))
        kenar2 = int(input("2.Kenar: "))

        if kenar1 == 0 or kenar2 == 0:
            print("Herhangibir kenar 0 olamaz!")
            kenarlari_al()

        return kenar1, kenar2
    #--------------------------------------------------------------------

    islem_menuleri()

    islem = int(input("Yapmak istediginiz islemi seciniz: "))

    if islem == 1:
        kenar1, kenar2 = kenarlari_al()
        kare_alani(kenar1, kenar2)

    elif islem == 2:
        kenar1, kenar2 = kenarlari_al()
        dikdortgen_alani(kenar1, kenar2)

programi_calistir()












# def alan_hesap(kenar1,kenar2,sekil ):
#     if sekil == 1:
#         if kenar1 != kenar2:
#             print("Karennin kenarları eşit olmadılır tekrar deneyiniz.")
#         else:
#             sonuc = kenar1 * kenar2
#             print(f"Karenin alanı {sonuc} m^2'dir.")
#     elif sekil == 2:
#         sonuc = kenar1 * kenar2
#         print(f"dikdörtgenin alanı {sonuc} m^2 dir.")
#     else:
#         print("Geçerli karakter giriniz.")
# print("")
# kenar1 = int(input("Bir kenar giriniz: "))
# kenar2 = int(input("Bir kenar giriniz: "))
# sekil = int(input("Kare için 1'i, Dikdörtgen için 2 yazınız: "))
# alan_hesap(kenar1,kenar2,sekil)













