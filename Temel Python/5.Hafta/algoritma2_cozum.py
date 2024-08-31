# num = 2**1000
# numnum= num
# sumnumnum = 0
# while numnum>0:
#     basamak = numnum % 10
#     sumnumnum = sumnumnum + basamak
#     numnum = numnum // 10
# #---------------------------------------------------#
# summary = 0
# num = 2**1000
# stringnum =str(num)
# for i in stringnum:
#     summary += int(i)
# print(summary)

def toplamSonuc(a,b):
     toplam=0
     sayi=pow(a,b)
     for i in str(sayi):
         toplam+=int(i)
     return topla
a=int(input("a: "))
b=int(input("b: "))
print("sonuç: ", toplamSonuc(a,b))