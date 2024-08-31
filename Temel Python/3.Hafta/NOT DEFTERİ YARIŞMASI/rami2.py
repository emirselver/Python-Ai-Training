notlar = []  # Notları saklamak için boş bir liste oluşturuyorum
menu = ["Not Ekleme", "Notları Görüntüle", "Not Düzenle", "Not Sil", "Çıkış"]  # Menü seçeneklerini tanımlıyorum

# Kullanıcıdan sürekli olarak seçim almak için bir döngü başlatıyorum
while True:
    # Menü seçeneklerini kullanıcıya göstermek için döngü oluşturuyorum
    for i in range(len(menu)):
        print(i + 1, ")", menu[i])
    
    # Kullanıcıdan seçim yapmasını istiyorum
    secim = int(input("Bir seçim yapın: "))
    
    if secim == 1:  # Not Ekleme
        # Kullanıcıdan not başlığı ve içeriği girmesini istiyorum
        başlık = input("Not Başlığı: ")
        içerik = input("Not İçeriği: ")
        # Yeni notu notlar listesine ekliyorum
        notlar.append({"başlık": başlık, "içerik": içerik})
        # Not eklendi mesajını gösteriyorum
        print("Not eklendi.\n")
    
    elif secim == 2:  # Notları Görüntüle
        # Eğer hiç not yoksa kullanıcıya bildiriyorum
        if not notlar:
            print("Hiç not bulunmamaktadır.\n")
        else:
            # Mevcut notları liste halinde kullanıcıya gösteriyorum
            for i in range(len(notlar)):
                print(f"{i + 1}. Başlık: {notlar[i]['başlık']}, İçerik: {notlar[i]['içerik']}")
            print()
    
    elif secim == 3:  # Not Düzenle
        # Eğer hiç not yoksa kullanıcıya bildiriyorum
        if not notlar:
            print("Hiç not bulunmamaktadır.\n")
        else:
            # Mevcut notları liste halinde kullanıcıya gösteriyorum
            for i in range(len(notlar)):
                print(f"{i + 1}. Başlık: {notlar[i]['başlık']}, İçerik: {notlar[i]['içerik']}")
            # Kullanıcıdan düzenlemek istediği notun numarasını seçmesini istiyorum
            düzenle_secim = int(input("Düzenlemek istediğiniz notun numarasını seçin: ")) - 1
            # Geçerli bir not numarası seçilmişse düzenleme işlemini yapıyorum
            if 0 <= düzenle_secim < len(notlar):
                yeni_başlık = input("Yeni Başlık: ")
                yeni_içerik = input("Yeni İçerik: ")
                notlar[düzenle_secim] = {"başlık": yeni_başlık, "içerik": yeni_içerik}
                print("Not düzenlendi.\n")
            else:
                # Geçersiz bir not numarası seçilmişse kullanıcıya bildiriyorum
                print("Geçersiz seçim.\n")
    
    elif secim == 4:  # Not Sil
        # Eğer hiç not yoksa kullanıcıya bildiriyorum
        if not notlar:
            print("Hiç not bulunmamaktadır.\n")
        else:
            # Mevcut notları liste halinde kullanıcıya gösteriyorum
            for i in range(len(notlar)):
                print(f"{i + 1}. Başlık: {notlar[i]['başlık']}, İçerik: {notlar[i]['içerik']}")
            # Kullanıcıdan silmek istediği notun numarasını seçmesini istiyorum
            sil_secim = int(input("Silmek istediğiniz notun numarasını seçin: ")) - 1
            # Geçerli bir not numarası seçilmişse silme işlemini yapıyorum
            if 0 <= sil_secim < len(notlar):
                del notlar[sil_secim]
                print("Not silindi.\n")
            else:
                # Geçersiz bir not numarası seçilmişse kullanıcıya bildiriyorum
                print("Geçersiz seçim.\n")
    
    elif secim == 5:  # Çıkış
        # Kullanıcı çıkış yapmak istediğinde programı sonlandırıyorum
        print("Programdan çıkılıyor.")
        break
    
    else:
        # Geçersiz bir seçim yapılmışsa kullanıcıya bildiriyorum
        print("Geçersiz seçim. Tekrar deneyin.\n")