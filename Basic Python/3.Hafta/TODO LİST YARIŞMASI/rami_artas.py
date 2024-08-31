gorevlerim = ["spor yap", "kod yaz"]
while True:
    print("1)Yapılacaklar listesi")
    print("2)yeni görev ekle")
    print("3)görev sil")
    print("4) çıkış yap")
    sayi = int(input("yapacak seç: "))
    if sayi == 1:
        for i in gorevlerim:
            print(i)
    elif sayi == 2:
        yeni_gorev = input("yeni görev ekle: ")
        gorevlerim.append(yeni_gorev)
        for i in gorevlerim:
            print(i)
    elif  sayi ==3:
        kaldir = input("kaldırılacak görevi seç: ")
        gorevlerim.remove(kaldir)
        for i in gorevlerim:
            print(i)
    elif sayi == 4:
        break
