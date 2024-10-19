
#menjumlah bilangan ganjil 
def ganjil(angka):
#  hasil = 0
#   for i in range(1,angka+1):
#     if i % 2 == 0:
#       hasil += i 
  return sum(range(1,angka + 1,2))
#   return hasil

print(ganjil(99))