import math as mtk
#membuat perhitungan factorial  menggunakan for loop
# def factorial(n):
#   hasil = 1 
#   for i in range(1,n + 1):
#     hasil *=i 
#   return hasil 
#tes hasil 
user = int(input("masukan angka"))
#print(f"factorial dari {user} : {factorial(user)}")
factorial = mtk.factorial(user)
print(f"factorial dari {user} : {factorial}")
