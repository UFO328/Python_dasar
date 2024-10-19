#macam macam operasi aritmatika
a = 10
b = 3
#operasi tambah (+) 
hasil = a + b 
print(f"{a} + {b} = {hasil}")

#operasi kurang (-)
hasil = b - a 
print(f"{b} - {a} = {hasil}")

#operasi kali (*)
hasil = a * b 
print(f"{b} * {a} = {hasil}")


#operasi bagi (/)
hasil = a / b 
print(f"{a} / {b} = {hasil}")

#operasi eksponen / pangkat (**)
hasil = a**b
print(f"{b}**{a} = {hasil}")

#operasi modulus / sisa bagi(%)
hasil = a % b 
print(f"{b}%{a} = {hasil}")

#operasi floor division (//)
hasil = a // b
print(f"{b} // {a} = {hasil}")

"""
prioritas operator aritmatika 
    1.() angka yang di dalam kurung akan di hitung duluan 
    2.eksponen
    3.perkalian dan kawan kawan /,%,//
    4.tambah dan kurang 
"""


a = 5
b = 2 
hitung = (a**2-2**3)
print(hitung)