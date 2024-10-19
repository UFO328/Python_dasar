"""
args/argumens berfungsi supaya kita bisa membuat
sebuah parameter bisa lebih dinamis 
"""

#contoh studi kasus 
# def date_list(data_list):
#   date = data_list.copy()
#   for data in date:
#     print(data)
# 
# date_list(["riski",17,2007])

"""
contoh studi kasus di atas kode nya,masih
bisa di sederhanakan lagi mengunakan args 
parameter
"""

#contoh deklarasi function dengan argas parameter
#sebelum parameter di deklarasi harus ada tanda bintang(*) agar menandakan parameter adalah args parameter

# def name_function(*args):
#   pass 

def halo(*date):
  name = date[0]#mengaksesnya sama seperti list 
  umur = date[1]
  tinggi = date[2]
  print("\nMENGAKSES MENGGUNAKAN INDEKS")
  print(f"nama kamu {name}")
  print(f"umur kamu '{umur}'")
  print(f"tinggi kamu '{tinggi}'")
  #atau menggunakan iterasi dengan for loop
  print("\nMENGGUNAKAN FOR LOOP")
  for data in date:
    print(data)

halo("riski",17,185)