# Notları saklamak için bir liste oluşturuyoruz
notlar = [0]

while True:
    # Menü seçeneklerini gösteriyoruz
    print("\n1. Not Ekle")
    print("2. Notları Görüntüle")
    print("3. Not Düzenle")
    print("4. Not Sil")
    print("5. Çıkış")
    secim = input("Seçiminizi yapın: ")

    if secim == '1':
        # Kullanıcıdan not başlığı ve içeriğini alıyoruz
        baslik = input("Not Başlığı: ")
        icerik = input("Not İçeriği: ")
        # Notu listeye ekliyoruz
        notlar.append({"başlık": baslik, "içerik": icerik})
        print("Not eklendi.")
    elif secim == '2':
        # Notların başlıklarını listeliyoruz
        for i, not_ in enumerate(notlar):
            print(f"{i + 1}. {not_['başlık']}")
        if notlar:
            # Kullanıcıya detayını görmek istediği notun numarasını soruyoruz
            detay = input("Detayını görmek istediğiniz not numarasını girin (geri dönmek için Enter'a basın): ")
            if detay.isdigit():
                index = int(detay) - 1
                if 0 <= index < len(notlar):
                    # Seçilen notun başlığını ve içeriğini gösteriyoruz
                    print(f"Başlık: {notlar[index]['başlık']}")
                    print(f"İçerik: {notlar[index]['içerik']}")
    elif secim == '3':
        # Notların başlıklarını listeliyoruz
        for i, not_ in enumerate(notlar):
            print(f"{i + 1}. {not_['başlık']}")
        if notlar:
            # Kullanıcıya düzenlemek istediği notun numarasını soruyoruz
            duzenle = input("Düzenlemek istediğiniz not numarasını girin: ")
            if duzenle.isdigit():
                index = int(duzenle) - 1
                if 0 <= index < len(notlar):
                    # Kullanıcıdan yeni başlık ve içerik alıyoruz
                    yeni_baslik = input("Yeni Başlık: ")
                    yeni_icerik = input("Yeni İçerik: ")
                    # Seçilen notu güncelliyoruz
                    notlar[index]['başlık'] = yeni_baslik
                    notlar[index]['içerik'] = yeni_icerik
                    print("Not düzenlendi.")
    elif secim == '4':
        # Notların başlıklarını listeliyoruz
        for i, not_ in enumerate(notlar):
            print(f"{i + 1}. {not_['başlık']}")
        if notlar:
            # Kullanıcıya silmek istediği notun numarasını soruyoruz
            sil = input("Silmek istediğiniz not numarasını girin: ")
            if sil.isdigit():
                index = int(sil) - 1
                if 0 <= index < len(notlar):
                    # Seçilen notu listeden çıkarıyoruz
                    notlar.pop(index)
                    print("Not silindi.")
    elif secim == '5':
        # Programı bitiriyoruz
        break
    else:
        print("Geçersiz seçim, tekrar deneyin.")
