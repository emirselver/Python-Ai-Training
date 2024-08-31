#LİSTELER
sehirler = ["İstanbul", "Ankara","İzmir","Bursa","Trabzon","Şanlıurfa"]

# sehirler_kopya = sehirler.copy()
# print(sehirler_kopya)

# sehirler.append("Aydın")

# sehirler.insert(3,"Maraş")
# print(sehirler)

# buyuksehirler = ["Samsun","Hatay"]
# sehirler.extend(buyuksehirler)
# yeni_sehir = buyuksehirler[0]
# sehirler.append(yeni_sehir)
# sehirler.remove("İstanbul")
# sehirler.pop()

# del sehirler[3],
# sehirler.reverse()
# ilceler.sort(reverse=True)
# print(ilceler)

ilceler = ["Karaköprü","Haliliye","Ceylanpınar"]

# ilceler_birlestirilmis = ",".join(ilceler)
# ayrilmis_ilceler = ilceler_birlestirilmis.split(",")

# print(type(ayrilmis_ilceler))

# for ilce in ilceler:
#     if ilce != "Ceylanpınar":
#         print(ilce)

# notlar = [80, 50, 100]
# print(150 in notlar)
# print(sum(notlar))
# print(min(notlar))
# print(max(notlar))


#TUPLE (DEMET)

# sayilar = (25,30,35,40)
# print(sayilar[0])

#SET (KÜME)
# meyveler = {"Elma","Portakal","Kiraz"}

# sayi_kumesi1 = {1,3,5,8,9,13}
# sayi_kumesi2 = {1,5,9,13,18,7}
# print(sayi_kumesi1.union(sayi_kumesi2))

#DICTIONARY (SÖZLÜK)

# sozluk = {'Adi': "Ali",'Soyadi':'Yılmaz','Telefon':545212356}
# sozluk['Sehir'] = 'İzmir'
# sozluk['Telefon'] = 8464613
# print(sozluk.keys())
# print(sozluk.values())

# ogrenci_notlari = [80,52,79,78,65]

# toplam = 0

# for not_bilgisi in ogrenci_notlari:
#     toplam += not_bilgisi

# print("Sonuç:", toplam)

#KOŞUL YAPILARI


# bke 18 den küçükse ----> zayıf
# bke 18 den büyükse ----> normal
# bke 25 den büyükse ----> fazla kilolu
# bke 30 dan büyükse ----> obez

# boy = float(input('Lütfen Boyunuzu m Cinsinden Giriniz: örnek:1.70 '))
# kilo=  float(input('Lütfen Kilonuzu kg Cinsinden Giriniz: '))

# bke = (kilo / (boy * boy))

# if bke < 18:
#     print('Zayıf' ,bke)

# elif bke > 18:
#     print('Normal', bke)

# elif bke > 25:
#     print('Fazla Kilolu', bke)

# elif bke > 30:
#     print('Obez', bke)

# boy = float(input('Lütfen Boyunuzu m Cinsinden Giriniz: '))
# kilo=  float(input('Lütfen Kilonuzu kg Cinsinden Giriniz: '))

# bke = (kilo / (boy * boy))

# if bke < 18:
#     print('Zayıf' ,bke)
# elif (bke > 18 and bke < 25):
#     print('Normal' ,bke)
# elif (bke> 25 and bke < 30):
#     print('Fazla Kilolu' ,bke)
# elif bke>30:
#     print('Obez' ,bke)

x = 5
y = 10

if x > 0 and y > 0:
    print("x ve y pozitif sayilardir")

elif x > 0 or y > 0:
    print("x veya y pozitif sayidir")

if not x < 0:
    print("x negatif degil")

yas = 10
whi










