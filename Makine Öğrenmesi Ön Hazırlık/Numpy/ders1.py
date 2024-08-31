"""
numpy -> numerical python
numpy array python listelere göre daha dinamik/kullanışlıdır
daha hızlı çalışmaktadır
normal python ile type olarak kıyasla

Yaptırılacak Örnekler:
1) Sınıf Notlarını Analiz Etme : Ortalama, medyan, varyans, standart sapma gibi temel istatistiksel değerleri hesaplayın.
Notları sıralayın ve en yüksek ile en düşük notu bulun.

2)
Numpy kütüphanesini kavratmak için sadece Numpy ile gerçekleştirilebilecek daha spesifik üç proje önerisi:

Seviye 1: Numpy ile Dizi Manipülasyonu
Proje: "Sıcaklık Verileri Analizi"

Açıklama: Öğrenciler, bir haftalık sıcaklık verilerini içeren bir Numpy array’i kullanarak çeşitli analizler yapacaklar.
Hedef: Numpy ile dizi oluşturma, dilimleme ve temel istatistiksel fonksiyonları kullanma.
Adımlar:
Bir haftalık (7 gün) sıcaklık verilerini temsil eden bir Numpy array’i oluşturun (örneğin, [22, 24, 19, 21, 23, 20, 22]).
Haftalık ortalama sıcaklığı hesaplayın (np.mean).
Hafta içi (ilk 5 gün) ve hafta sonu (son 2 gün) ortalama sıcaklıklarını ayrı ayrı hesaplayın.
En yüksek ve en düşük sıcaklıkları bulun (np.max, np.min).

Destekleyici colab notebook linki:
https://colab.research.google.com/drive/1BWwyDZS_rNiFZuezrc6Vg-Psr4gulNf7?usp=sharing#scrollTo=w66c2p9Z6JwY
"""

# Numpy Kütüphanesini İçe Aktarma
import numpy as np

# 1. Numpy ile Dizi (Array) Oluşturma
# ------------------------------------
python_list = [1, 2, 3, 4]
print(type(python_list))
# 1D Dizi Oluşturma
array_1d = np.array([1, 2, 3, 4, 5])
print("1D Array:", array_1d)
print(type(array_1d))

# 2D Dizi Oluşturma
array_2d = np.array([[1, 2, 3], [4, 5, 6]])
print("2D Array:\n", array_2d)

# Dizinin boyutunu öğrenme
boyut = np.ndim(array_2d)
print(boyut)

# Boş Dizi Oluşturma
empty_array = np.empty((2, 3))
print("Empty Array:\n", empty_array)

# Sıfırlarla Dolu Dizi Oluşturma
zeros_array = np.zeros((3, 3))
print("Zeros Array:\n", zeros_array)

# Birlerle Dolu Dizi Oluşturma
ones_array = np.ones((3, 3))
print("Ones Array:\n", ones_array)

# Rastgele Sayılarla Dolu Dizi Oluşturma
random_array = np.random.rand(3, 3)
print("Random Array:\n", random_array)

# Aralıklarla Dizi Oluşturma
range_array = np.arange(0, 10, 2)  # 0'dan 10'a kadar 2'şer artan dizi
print("Range Array:", range_array)

# Belirli Aralıkta Sabit Sayıda Değerler İçeren Dizi Oluşturma
linspace_array = np.linspace(0, 1, 5)  # 0'dan 1'e kadar 5 eşit aralıklı değer
print("Linspace Array:", linspace_array)


# 2. Numpy ile Temel Dizi Operasyonları
# --------------------------------------

# Dizi Boyutları (Shape) ve Tipini (dtype) Öğrenme
print("Array Shape:", array_2d.shape)
print("Array Data Type:", array_2d.dtype)

# Dizi Elemanlarına Erişim ve Dilimleme
print("Element at Index 0 in 1D Array:", array_1d[0])
print("Element at Row 0, Column 1 in 2D Array:", array_2d[0, 1])
print("Slice of 1D Array [1:4]:", array_1d[1:4])

# Dizi Yeniden Şekillendirme (Reshape)
reshaped_array = array_1d.reshape((5, 1))
print("Reshaped Array:\n", reshaped_array)

# Dizi Birleştirme (Concatenation)
concatenated_array = np.concatenate((array_1d, range_array))
print("Concatenated Array:", concatenated_array)

# Dizi Boyutlarını Değiştirme (Flattening)
flattened_array = array_2d.flatten()
print("Flattened Array:", flattened_array)


# 3. Numpy ile Matematiksel İşlemler
# -----------------------------------

# Toplama ve Çıkarma
array_sum = np.add(array_2d, 5)  # Her elemana 5 ekleme
print("Array after Addition:\n", array_sum)

array_diff = np.subtract(array_2d, 2)  # Her elemandan 2 çıkarma
print("Array after Subtraction:\n", array_diff)

# Çarpma ve Bölme
array_mult = np.multiply(array_2d, 2)  # Her elemanı 2 ile çarpma
print("Array after Multiplication:\n", array_mult)

array_div = np.divide(array_2d, 2)  # Her elemanı 2'ye bölme
print("Array after Division:\n", array_div)

# Matris Çarpımı (Matrix Multiplication)
matrix_mult = np.dot(array_2d, array_2d.T)  # Matris çarpımı (dot product)
print("Matrix Multiplication Result:\n", matrix_mult)

# Toplama (Sum), Ortalamayı (Mean) ve Standart Sapma (Standard Deviation) Hesaplama
array_sum = np.sum(array_2d)  # Tüm elemanların toplamı
print("Sum of all elements:", array_sum)

array_mean = np.mean(array_2d)  # Ortalamayı hesaplama
print("Mean of all elements:", array_mean)

array_std = np.std(array_2d)  # Standart sapmayı hesaplama
print("Standard Deviation of all elements:", array_std)
#Transpose -> satirlar sutunlara, sutunlar satiralara donusur.
# Örnek bir matris oluşturma
A = np.array([[1, 2, 3],
              [4, 5, 6]])

print("Orijinal Matris A:")
print(A)

# Matrisin transpozunu alma
A_transpose = A.T

print("\nMatris A'nın Transpozu A^T:")
print(A_transpose)
# Transpozunu Alma
transposed_array = array_2d.T
print("Transposed Array:\n", transposed_array)

# Maksimum ve Minimum Değerleri Bulma
max_value = np.max(array_2d)
min_value = np.min(array_2d)
print("Max Value:", max_value)
print("Min Value:", min_value)

# Argmax ve Argmin ile Maksimum ve Minimum Değerlerin İndekslerini Bulma
max_index = np.argmax(array_2d)
min_index = np.argmin(array_2d)
print("Index of Max Value:", max_index)
print("Index of Min Value:", min_index)


# 4. Numpy ile İleri Seviye İşlemler
# -----------------------------------

# Boolean Indexing
bool_array = array_2d > 4  # 4'ten büyük olan elemanlar True olacak
print("Boolean Array (Elements > 4):\n", bool_array)
print("Elements greater than 4:\n", array_2d[bool_array])

# Rastgele Sayılarla Dolu Bir Dizi Oluşturup Normalizasyon (Normalization) Yapma
random_array = np.random.rand(3, 3) * 100
normalized_array = (random_array - np.min(random_array)) / (np.max(random_array) - np.min(random_array))
print("Normalized Array:\n", normalized_array)

# Dizi Elemanlarını Sıralama (Sorting)
sorted_array = np.sort(random_array, axis=0)  # Sütunlara göre sıralama
print("Sorted Array:\n", sorted_array)
