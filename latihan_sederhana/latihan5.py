#latihan membuat segita dengan loop 


#menggunakan for loop 

sisi = 10 
# #dummy variablr
angka = 0
print("awal for ")
for i in range(sisi):
   print("*"*angka)
   angka +=1
print("akhir for ")

#menggunakan while loop 

print("awal while")
#variable dummy 
angka = 0 
dum = 0

while True:
  
  print(f"{dum}"*angka)
  angka +=1
  dum += 1
  
  if angka == sisi:
    break
  
print("akhir while")
  