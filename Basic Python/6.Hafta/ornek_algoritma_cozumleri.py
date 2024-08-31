#1) 2 ile 1000 arasındaki asal sayıların toplamını bulunuz.

# toplam = 0

# for sayi in range(2, 1001):
#     asal = True
#     if sayi < 2:
#         asal = False
#     for i in range(2, sayi):
#         if sayi % i == 0:
#             asal = False
#             break
#     if asal:
#         toplam += sayi

# print(f"{2} ile {1000} arasındaki asal sayıların toplamı: {toplam}")


# toplam = 0

# for sayi in range(2, 1001):
#     if sayi % 2 == 0:
#         toplam += sayi

# print(toplam)


#asal:

# asal_toplam = 0

# for sayi in range(2,1001):
#     asal_mi = True

#     for bolenler in range(2, sayi):
#         if sayi % bolenler == 0:
#             asal_mi = False
#             break

#     if asal_mi == True:
#         asal_toplam += sayi

# print(asal_toplam)

#PROBLEM -> Mükemmel Sayılar Bulma

#TANIMI -> Mükemmel sayı, kendisi hariç pozitif bölenlerinin toplamı kendisine eşit olan sayıdır.

#ÖRNEK ->, 6 bir mükemmel sayıdır çünkü 1, 2 ve 3 bölenleri toplamı 6 eder (1 + 2 + 3 = 6)

#SORU -> 1 ile 1000 arasındaki mükemmel sayıları bulun.

# mukemmel_toplam = 0
# mukemmel_sayilar = []

# for sayi in range(1,1000):
#     tam_bolenler = []

#     for tam_bolen in range(1, sayi):
#         if sayi % tam_bolen == 0:
#             tam_bolenler.append(tam_bolen)

#     if sum(tam_bolenler) == sayi:
#         mukemmel_sayilar.append(sayi)
#         mukemmel_toplam += sayi
#         print("Mükemmel Sayi! ", sayi)

# print("1 - 1000 arasındaki Mükemmel Sayilar: ")
# print(mukemmel_sayilar)
# print("Bu sayilarin toplami: ", mukemmel_toplam)


#Soru Kaydırma Şifreleme (Caesar Cipher)
#Açıklama: Verilen bir metindeki her harfi belirli bir miktarda kaydırarak şifreleyin. Kaydırma miktarını modül kullanmadan gerçekleştireceğiz. Bunun için, harflerin yer aldığı diziyi doğrudan işleyerek kaydırma işlemi yapacağız.

#örnek :
#Şifrelenecek metin: "Merhaba Dünya!"
#Şifrelenmiş metin: "Phukded Gxqdb!"

alfabe_kucuk = "abcdefghijklmnopqrstuvwxyz"
alfabe_buyuk = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

metin = input("Şifrelenecek metni girin: ")

sifreli_metin = ""

for karakter in metin:
    if karakter in alfabe_kucuk:
        indeks = alfabe_kucuk.index(karakter)
        yeni_indeks = indeks + 1
        if yeni_indeks >= len(alfabe_kucuk):
            yeni_indeks -= len(alfabe_kucuk)
        sifreli_metin += alfabe_kucuk[yeni_indeks]
    elif karakter in alfabe_buyuk:
        indeks = alfabe_buyuk.index(karakter)
        yeni_indeks = indeks + 1
        if yeni_indeks >= len(alfabe_buyuk):
            yeni_indeks -= len(alfabe_buyuk)
        sifreli_metin += alfabe_buyuk[yeni_indeks]
    else:
        sifreli_metin += karakter

print("Şifrelenmiş metin:", sifreli_metin)

        
        
