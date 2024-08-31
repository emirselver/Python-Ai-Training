# def pisagor_ucgeni_bul():
#     for a in range(1, 1000):
#         for b in range(a + 1, 1000):
#             c = 1000 - a - b
#             if a * a + b * b == c * c:
#                 return a, b, c, a * b * c

# ucgen = pisagor_ucgeni_bul()
# print(ucgen)


for i in range(1, 500):
    for j in range(i, 500):
        for m in range(j, 500):
            if i*i + j*j == m**2 and i+j+m == 1000:
                print(f"{i}, {j}, {m}")
            # else:
            #     print("Bulunamadı!")