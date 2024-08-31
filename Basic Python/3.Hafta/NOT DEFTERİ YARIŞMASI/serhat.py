while True:
    secim = int(input("1) Not ekle \n2) Notları görüntüle \n3) Not düzenleme : \n4) Not silme \n 5)cikis \nsecim yapin :"))
    print(50 * "*")
    if secim == 1:
        baslik_ekle = input("baslik ekleyin :")
        not_ekle = input("not ekleyin :")
        basliklar.append(baslik_ekle)
        notlar.append(not_ekle)
        print("baslik ve nolar eklendi...")
    elif secim == 2:
        if len(basliklar) != 0:
            for i in range(0,len(basliklar),1):
                print(f"listenin {i+1}. elemani :")
                print(f"baslik : {basliklar[i]} notlar: {notlar[i]}")
        else:
            print("dizi bos görüntülenecek not bulunmamaktadır")
    elif secim == 3:
        for i in range(0, len(basliklar), 1):
            print(f"listenin {i+1}. elemani :")
            print(f"baslik : {basliklar[i]} notlar: {notlar[i]}")

        notdüzenle = int(input("listenin kaçıncı notu düzenlensin? : "))

        if 0 < notdüzenle < len(basliklar):
            yenibaslik = input("yeni baslik girin :")
            yeninot = input("yeni not girin:")

            basliklar[notdüzenle] = yenibaslik
            notlar[notdüzenle] = yeninot
        else:
            print("yanlis secim yaptiniz menüye yönlendiriliyorsunuz")

    elif secim == 4:
        if len(basliklar) != 0:
            for i in range(0, len(basliklar), 1):
                print("listeniz: ")
                print(f"listenin {i}. elemani :")
                print(f"baslik : {basliklar[i]} notlar: {notlar[i]}")
            verisil = int(input("lsitenin kaçıncı verisini silmek istersiniz? ="))

            basliklar.remove(verisil)
            notlar.remove(verisil)
            print("veriniz basari ile silinmistir")


        else:
            print("liste boş veri silinemez nenüye aktarılıyorsunuz")

    elif secim == 5:
        emin = input("cikis yapmak istediğinden emin misin ? ")
        if emin.upper() == 'E':
            break