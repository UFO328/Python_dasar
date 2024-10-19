#membuat segitiga menggunakn while loop 

# angka = input("mau berapa sisi segitiga nya : ")
# dum = 0
# while True:
#   dum += 1 
#   print("*"*dum)
#   
#   if dum == int(angka):
#     break
#   

#menggunakn for loop untuk buat segitiga 
print(f'{"MEGGUNAKAN FOR LOP":^50}')
user = int(input("masukan panjang segitiga : "))

dum = 0 

for i in range(1,user + 1):
  dum += 1 
  print("*"*dum)