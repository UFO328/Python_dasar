#membuat program bilangan prima 

def prima(angka):
  if angka > 1:
    for i in range(2,angka):
      if (angka % i) == 0:
         return False
    return True
  else:
    return False
#tes program 
angka = int(input("masukan angka : "))
if prima(angka):
  print(f"angka {angka} bilangan prima")
else:
  print(f"angka {angka} bukan prima")
  