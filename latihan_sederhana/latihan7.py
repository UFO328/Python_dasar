#mejumlahkan bilangan ganjil dari range 1 sampai 100

a = 1
b = 99
hasil = 0 
for i in range(a,b+1):
  if i % 2 == 0:
    hasil += i 
    print(f"angka  -> {hasil}")
  