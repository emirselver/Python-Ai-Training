notlar = {}


def notlari_listele():
    if len(notlar) < 1:
        print("Henüz bir not bulunmamaktadır")
    else:
        for indeks, (baslik, icerik) in enumerate(notlar.items(), start=1):
            print(f"{indeks}) Başlık: {baslik}, İçerik: {icerik}")


while True:
    print("\n 1) Not Görüntüleme \n 2) Not Ekleme \n 3) Not Düzenleme \n 4) Not Silme \n 5) Çıkış Yap")
    secim = input("Bir seçim yapınız: ")

    if secim == '1':
        notlari_listele()

    elif secim == '2':
        baslik = input("Bir başlık giriniz: ")
        if baslik in notlar:
            print("Bu başlık zaten mevcut. Lütfen farklı bir başlık giriniz.")
        else:
            konu = input("Bir konu giriniz: ")
            notlar[baslik] = konu
            print("Not başarıyla eklendi.")
        notlari_listele()

    elif secim == '3':
        if len(notlar) < 1:
            print("Henüz bir not bulunmamaktadır")
        else:
            print(" 1) Başlık Düzenleme \n 2) İçerik Düzenleme")
            duzenleme_secim = input("Bir seçim yapınız: ")

            if duzenleme_secim == '1':
                eski_baslik = input("Düzenlemek istediğiniz notun eski başlığını giriniz: ")
                if eski_baslik in notlar:
                    yeni_baslik = input("Yeni başlığı giriniz: ")
                    notlar[yeni_baslik] = notlar.pop(eski_baslik)
                    print("Başlık başarıyla düzenlendi.")
                else:
                    print("Bu başlıkta bir not bulunmamaktadır.")

            elif duzenleme_secim == '2':
                baslik = input("Düzenlemek istediğiniz notun başlığını giriniz: ")
                if baslik in notlar:
                    yeni_konu = input("Yeni konuyu giriniz: ")
                    notlar[baslik] = yeni_konu
                    print("Not içeriği başarıyla düzenlendi.")
                else:
                    print("Bu başlıkta bir not bulunmamaktadır.")
            else:
                print("Geçersiz seçim, lütfen tekrar deneyiniz.")
        notlari_listele()

    elif secim == '4':
        if len(notlar) < 1:
            print("Henüz bir not bulunmamaktadır")
        else:
            baslik = input("Silmek istediğiniz notun başlığını giriniz: ")
            if baslik in notlar:
                del notlar[baslik]
                print("Not başarıyla silindi.")
            else:
                print("Bu başlıkta bir not bulunmamaktadır.")
        notlari_listele()

    elif secim == '5':
        print("Çıkış yapılıyor...")
        break

    else:
        print("Geçersiz seçim, lütfen tekrar deneyiniz.")
