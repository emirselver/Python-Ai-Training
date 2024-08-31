liste = []
while True:
    # print(50*"*")
    # print("TODO List Uygulaması")
    # print(50*"*")
    menu = ["Listeyi Göster", "Yeni Görev Ekle", "Görev Sil", "Çıkış Yap"]
    for i in menu:
        print(menu.index(i) + 1, i)
    # print(50*"*")
    secim = int(input("Bir işlem seçiniz: "))
    if secim == 1:
        print(liste)
    elif secim == 2:
        yeniGorev = input("Yeni görevi yazın: ")
        liste.append(yeniGorev)
    elif secim == 3:
        gorevSilme = input("Silmek istediğiniz görevi yazın: ")
        liste.remove(gorevSilme)
        print("Görev Silindi!")
    elif secim == 4:
        break
    else:
        print("Lütfen geçerli bir sayı giriniz!")


