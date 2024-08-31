yapilacaklist = []
while True:
    print("""
    1-Yapılacaklar listesini listele
    2-Yeni görev ekle
    3-Görev sil
    4-Çıkış yap""")
    a = int(input("İşlemi seçiniz:"))
    if a == 1:
        print(yapilacaklist)
    if a== 2:
        yapilacaklist.append(input("Yapılacak görevi giriniz: "))
        print(yapilacaklist[-1], "Görevi eklendi.")
    if a== 3:
        print(yapilacaklist)
        yapilacaklist.remove(input("Silinecek görev"))
    if a == 4:
        print("Çıkış yapıldı.")
        break