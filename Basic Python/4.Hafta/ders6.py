# def toplama(*args):

#     toplam = 0
#     for sayi in sayilar:
#         toplam+= sayi

#     return toplam


# print(toplama(10,20,30))

# def bilgi_ver(**bilgiler):
#     for anahtar, deger in bilgiler.items():
#         print(f"{anahtar}: {deger}")

# bilgi_ver(ad="Ali",yas=20,sehir="Urfa",meslek="polis")

#ÖDEME GÜNÜ BULMA
#tc son hanesi çift ise return-> "pazartesi"
#tc son hanesi tek ise return-> "salı"

# def odeme_gunu(tc):
#     if tc % 2 == 0:
#         return "Pazartesi"

#     else:
#         return "Salı"

# tc_bilgisi = int(input("tc gir: "))
# gun = odeme_gunu(tc_bilgisi)
# print(f"Ödeme gününüz: {gun}")


# def odeme_gunu(tc):
#     tc_son_hanesi = int(tc[-1])
#     if tc_son_hanesi % 2 == 0:
#         return "Pazartesi", tc
#     else:
#         return "Salı", tc

# tc_bilgisi = input("tc gir: ")
# gun, tc = odeme_gunu(tc_bilgisi)
# print(f"Ödeme gününüz: {gun}")
# print(f"TC: {tc}")

#TRY - EXCEPT (HATA YÖNETİMİ)


# try:
#     yas = int(input("yas giriniz: "))
#     print(f"yasiniz : {yas}")
# except :
#     print("hata var!")


# try:
#     liste = ["a","b","c"]
#     print(liste[8])
# # except IndexError:
# #     print("listede olmayan eleman hatası!")
# # except Exception as ex:
# #     print(ex)

# try:
#     sayi1 = int(input("sayi gir: "))
#     sayi2 = int(input("sayi gir: "))

#     sonuc = sayi / sayi2
#     print(sonuc)
    
# except ValueError:
#     print("deger hatasi!")
# except ZeroDivisionError:
#     print("sifira bölünme hatasi!")

# except:
#     print("hata var!")


#SOLUTION OF DAILY TEMPERATURES 

#-----------------------------------SOLUTION - 1----------------------------------#

temperatures = [73,74,75,71,69,72,76,63]
output =[]

for i in range(len(temperatures)):
    for j in range(i,len(temperatures)):
        if temperatures[j] > temperatures[i]:
            output.append(j-i)
            break
    else:
        output.append(0)
print(output)


#-----------------------------------SOLUTION - 2----------------------------------#


sicakliklar = [73, 74, 75, 71, 69, 72, 76, 63]
sonuclar = []

for i in range(len(sicakliklar)):
    gun_sayisi = 0
    for j in range(i + 1, len(sicakliklar)):
        gun_sayisi += 1
        if sicakliklar[j] > sicakliklar[i]:
            sonuclar.append(gun_sayisi)
            break
    else:
        sonuclar.append(0)

print(sonuclar)