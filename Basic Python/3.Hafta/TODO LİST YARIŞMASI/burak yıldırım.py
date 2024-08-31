
list1 = ["film izle" , "yüzmeye git"]
while True:
    print("1) yapılacaklar listesi")
    print("2) yeni görev")
    print("3) görev sil")
    print("4) çıkış yap")

    secim = input("bir seçenecek seçiniz: ")
    if secim == '1':
        for i in list1:
            print(i)
    elif secim == '2':
        gorev = input("görev ekleyiniz: ")
        list1.append(gorev)
    elif secim == '3':
        list1.pop()
        print("görev silindi.")
    elif secim == '4':
        if len(list1) < 1:
            print("başarıyla çıkış yapıldı.")
            break
        elif len(list1) >= 1:
            print("görevler henüz bitmedi.")

