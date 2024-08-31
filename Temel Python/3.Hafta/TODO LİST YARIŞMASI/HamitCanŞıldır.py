liste = []
while True:
    print("1) yapılacaklar listesi")
    print("2) yeni görev ekle")
    print("3) görev sil")
    print("4) çıkış yap")
    secim = int(input("istediğiniz şeyi seçin:"))
    if secim == 1:
        print(liste)
    elif secim ==  2:
        görev1 = input("yeni görev ekle:")
        liste.append(görev1)
        print(liste)
    elif secim == 3:
        görev2= input("silmek istediğiniz görevi yazın:")
        liste.remove(görev2)
        print(liste)
    else:
        break
