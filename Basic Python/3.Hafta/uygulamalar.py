#1) Kullanıcının klavyeden girdiği sayi çift olana kadar devam eden döngü örneği


# while True:
#     sayi = int(input("sayi gir: "))
#     if sayi % 2 == 0:
#         print("sayi cift", sayi)
#         break
#     else:
#         print("sayi tek", sayi)


#2) Kullanıcı giriş işlemi (kullanıcının 3 hakkı olacak, giriş hakkı dolmadan doğru 
# giriş yaparsa giriş yapıldı yazıp döngüyü sonlandıracak 
# eğer 3 hakkında da doğru giriş yapamazsa giriş başarısız yazıp döngüden çıkacak)

kullaniciAdi = "admin"
kullaniciSifre = "admin1234"

sayac = 3

while sayac > 0:
    adi = input("kullanıcı adi giriniz: ")
    sifre = input("şifre giriniz: ")
    if adi == kullaniciAdi and  sifre == kullaniciSifre:
        print("giriş başarılı")
        break
    else:
        sayac -= 1
        print(f"giriş hatalı {sayac} hakkınız kaldı")
        if sayac == 0:
            print("hakkınızı doldurdunuz.")

# giris = 0
# while giris <3:
#     adi = input("kullanıcı adi giriniz: ")
#     sifre = input("şifre giriniz: ")
#     if adi == kullaniciAdi and sifre == kullaniciSifre:
#         print("giriş başarılı.")
#         break
#     elif adi != kullaniciAdi and sifre != kullaniciSifre: 
#         print("giriş başarısız")
#         giris += 1
#         continue
#     print("deneme hakkını doldurdunuz.")
