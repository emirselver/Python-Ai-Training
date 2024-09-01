"""
 numerical python
 """
import numpy as np
# 1. Numpy Dizi Oluşturma

# python_list = [1, 2, 3, 4]
# print(type(python_list))
# print(python_list)

# 1D Dizi Oluşturma
array_1d = np.array([1002, 20, 30, 4, 50])
# print(array_1d)

# 2D Dizi Oluşturma
array_2d = np.array([[1, 2, 3], [4, 5, 6]])
# print(array_2d)
array_3d = np.array([[[4, 5, 6], [100, 20, 3], [700, 8, 90]]])
print(array_3d)
# Dizinin Boyutunu Öğrenme

# print(np.ndim(array_1d))
# print(np.ndim(array_3d))

# Boş Dizi Oluşturma
# empty_array = np.empty((2, 3))
# print(empty_array)

# Sıfırlarla Dolu Dizi Oluşturma
zeros_array = np.zeros((4, 3), dtype=int)
# print(zeros_array)

# Birlerle Dolu Dizi Oluşturma
ones_array = np.ones((5,8), dtype=int)
# print(ones_array)

# Rastgele Sayılarla Dolu Dizi Oluşturma
random_array = np.random.rand(3,3)
# print(random_array)

# Aralıklarla Dizi Oluşturma
range_array = np.arange(0, 10, 2)
# print(range_array)

# Belirli Aralıkta Sabit Sayıda  Değerler İçeren Dizi Oluşturma
linspace_array = np.linspace(10, 20, 5)
# print(linspace_array)

# 2. Numpy İle Temel Dizi Operasyonları

# Dizi Boyutları (Shape) ve Tipini (dtype) Öğrenme
# print(array_2d.shape)
# print(array_2d.dtype)

# Dizi Elemanlarına Erişme
# print(array_2d[0][2])
# print(array_2d[0, 1])

# Dizi Yeniden Şekillendirme
# reshaped_array = array_1d.reshape((5, 1))
# print(reshaped_array)

# Dizi Birleştirme (Concatenation)
# new_array = np.concatenate((array_1d, range_array))
# print(new_array)

# 3. Numpy İle Basit Matematiksel İşlemler

# Toplama ve Çıkarma
# array_sum = np.add(array_1d, 5) # Her elemana 5 ekleme
# print(array_sum)

# array_diff = np.subtract(array_1d, 2) # Her elemandan 2 çıkarma
# print(array_diff)

# Çarpma ve Bölme
# array_mult = np.multiply(array_2d, 4)
# print(array_mult)

# array_div = np.divide(array_2d, 8)
# print(array_div)

# Elemanların Hepsini Toplama

# array_sum = np.sum(array_2d)
# print(array_sum)

# Elemanların Ortalamasını (Mean) Alma

# array_mean = np.mean(array_2d)
# print(array_mean)

# Standart Sapma (Standart Deviation) Hesaplama
# array_std = np.std(array_2d)
# print(array_std)

# Transpozunu Alma
# example_array = np.array([[1, 2, 3],
#               [4, 5, 6]])
# # print(example_array)
# example_array_transpose = example_array.T
# print(example_array_transpose)

# Maksimum ve Minimum Değer Bulma

# max_value = np.argmax(array_1d)
# min_value = np.argmin(array_1d)
# print(max_value)
# print(min_value)

# Dizi Elemanlarını Sıralama
# sorted_array = np.sort(array_3d, axis=0) # Sütunlara göre sıralama
# print(sorted_array)




#1) Sınıf Notlarını Analiz Etme : Ortalama, medyan, standart sapma gibi temel istatistiksel değerleri hesaplayın.
# Notları sıralayın ve en yüksek ile en düşük notu bulun.

#kod:
# grades = np.array([70, 85, 90, 78, 65, 92, 88, 76, 83, 95])
#
# mean = np.mean(grades)
# print(f"Ortalama: {mean}")
#
# median = np.median(grades)
# print(f"Medyan: {median}")
#
# std_dev = np.std(grades)
# print(f"Standart Sapma: {std_dev}")
#
# sorted_grades = np.sort(grades)
# print(f"Sıralanmış Notlar: {sorted_grades}")
#
# highest_grade = np.max(grades)
# print(f"En Yüksek Not: {highest_grade}")
#
# lowest_grade = np.min(grades)
# print(f"En Düşük Not: {lowest_grade}")



# """
# # 2) Numpy ile Dizi Manipülasyonu
# # Proje: "Sıcaklık Verileri Analizi"
# Hedef: Numpy ile dizi oluşturma, dilimleme ve temel istatistiksel fonksiyonları kullanma.
# Adımlar:
# Bir haftalık (7 gün) sıcaklık verilerini temsil eden bir Numpy array’i oluşturun (örneğin, [22, 24, 19, 21, 23, 20, 22]).
# Haftalık ortalama sıcaklığı hesaplayın.
# Hafta içi (ilk 5 gün) ve hafta sonu (son 2 gün) ortalama sıcaklıklarını ayrı ayrı hesaplayın.
# En yüksek ve en düşük sıcaklıkları bulun.
# """
#
# temperatures = np.array([22, 24, 19, 21, 23, 20, 22])
#
# weekly_avg_temp = np.mean(temperatures)
# print(f"Haftalık Ortalama Sıcaklık: {weekly_avg_temp}")
#
# weekday_avg_temp = np.mean(temperatures[:5])
# print(f"Hafta İçi Ortalama Sıcaklık: {weekday_avg_temp}")
#
# weekend_avg_temp = np.mean(temperatures[5:])
# print(f"Hafta Sonu Ortalama Sıcaklık: {weekend_avg_temp}")
#
# highest_temp = np.max(temperatures)
# print(f"En Yüksek Sıcaklık: {highest_temp}")
#
# lowest_temp = np.min(temperatures)
# print(f"En Düşük Sıcaklık: {lowest_temp}")