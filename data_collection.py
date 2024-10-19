"""
data collection di pythom ada banyak 
contoh nya list,tuple,set 
list[] menggunakan kurung siku
tuple()menggunakan kurung biasa
set{}menggunakan kurung kurawal

tuple data nya bisa di akses namun tidak bisa
di ubah ubah dan tidak bisa menggunakan operasi append

set dia tidak memiliki index jadi dia tidak 
bisa menggunakan operasi indexing namun bisa 
menggunakan operasi yang lain seperti add untuk menambahkan item atau remove untuk menghapus item 
"""

data_tuples = (1,5,4,7,)
#data_tuples.append(9)#tidak bisa menggunakan operasi append
print(data_tuples)

data_set = {9,8,7,7,6,5}
data_set.add(10)
print(data_set)