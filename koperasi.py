#operator komperasi 
"""
      contoh operator komperasi 
      1.lebih dari (>)
      2.kurang dari (<)
      3.lebih dari sama dengan (>=)
      4.kurang dari sama dengan (<=)
      5.sama dengan sama dengan (==)
      6.tidak sama dengan (!=)
      7.object identity is dan is not
berfungsi untuk membandingkan dua buah 
data.
Hasil dari perbandingan akan menjadi boolean
atau menjadi True atau False 
"""
#lebih dari (>)
a = 5
b = 3 
hasil = a > b 
print(f"apakah {a} lebih besar dari {b} = {hasil}")

"""
Note : 
object identity berfungsi untuk membandingkan
object atau alamat memori dari sebuah data
jadi object identity tidak bisa di gunakan
untuk membandingkan tipe data literal
hanya bisa di gunakan di obejct atau variable 

obejct atau variable yang memiliki value yang sama akan di tempatkan di alamat memori yang sama juga 
"""
#contoh penggunan obejct identity is 
x = 5 
y = 6
hasil = x is y 
print(f"apakah {x} dan {y} memiliki alamat yang sama = {hasil}")

#contoh penggunan is not 
hasil = x is not y 
print(f"apakah {x} dan {y} memiliki alamat yang beda = {hasil}")

"""
jika is akan True jika memori alamat nya sama dan akan False jika alamat memorinya berbeda

tetapi is not akan True jika alamat memori nya berbeda dan akan False jika alamat memorinya sama 

"""