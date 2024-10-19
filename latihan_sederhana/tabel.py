#membuat tabel perkalian 

def kali(x,y = 10):
  hasil = 1 
  for i in range(x,y + 1):
    print("\n")
    for j in range(x,y + 1):
      hasil = i * j 
      print(f"{i} X {j} = {hasil}")
  return hasil 
kali(1)
