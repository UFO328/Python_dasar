"""
lambda funtion berguna jika kode yanv akan 
kita buat tidak terlalu panjang 
"""

#contoh lambda function
# variable = lambda parameter:ekspresion

#cara mengunakan lambda function untuk filter list 

#lambda function untuk sort list 
data_nama = ["dudung","cepot","bubun","aji"]
data_nama.sort(key=lambda name:len(name))
print(data_nama)

#lambda function untuk filter list 
data_angka = [1,2,3,4,5,6,7,8,9,10]
data = list(filter(lambda x : x<7,data_angka))
print(data)

#mengfilter data angka yang genap 
data_genap = list(filter(lambda i : i % 2 == 0,data_angka))
print(f"angka genap {data_genap}")

#mengfilter data angka yang ganjil
data_ganjil = list(filter(lambda i : i % 2 == 1,data_angka))
print(f"angka ganjil {data_ganjil}")