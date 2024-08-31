baslik = []
icerik = []
while True:
    print("----------------------")
    print("1) Not Ekleme: ")
    print("2) Not Görüntüleme: ")
    print("3) Not Düzenleme: ")
    print("4) Not Silme: ")
    print("5) Çıkış")

    secim = (input("İşlem seçiniz: "))

    if secim == '1':
        baslik.append(input("Not başlığı giriniz: "))
        icerik.append(input("Not içeriğini giriniz: "))
        print("Not eklendi!")

    elif secim == '2':
        if baslik == []:
            print("Not listeniz şu anda boş!")
        else:
            for i in range(len(baslik)):
               print(f"{i+1}){baslik[i]}")
            basliksecimi = input("Hangi içerği görmek istiyorsunuz?")
            if int(basliksecimi) > len(baslik):
                print("Geçersiz not seçimi!")
            else:
                print(icerik[int(basliksecimi)-1])

    elif secim == '3':
        if baslik == []:
            print("Not listeniz şu anda boş!")
        else:
            for i in range(len(baslik)):
               print(f"{i+1}){baslik[i]}")
            basliksecimi = input("Hangi içerği değiştirmek istiyorsunuz?")

            if int(basliksecimi)> len(baslik):
                print("Geçersiz not seçimi!")
            else:
                icerik[int(basliksecimi) - 1] = input("Notunuzu giriniz: ")

    elif secim == '4':
        if baslik == []:
            print("Not listeniz şu anda boş!")
        else:
            for i in range(len(baslik)):
               print(f"{i+1}){baslik[i]}")
            basliksecimi = input("Hangi içerği silmek istiyorsunuz?")
            if int(basliksecimi)> len(baslik):
                print("Geçersiz not seçimi!")
            else:
                baslik.pop(int(basliksecimi) - 1)
                icerik.pop(int(basliksecimi) - 1)

    elif secim == '5':
        print("Çıkış yapılıyor...")
        break
    else:
        print("Geçersiz işlem.")



