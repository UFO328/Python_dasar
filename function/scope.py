#global scope dan static scope
"""
global scope dan static scope adalah
sebuah variable yang menentukan dimana dia 
bisa di akses dan data nya di ubah 
"""

#contoh variabale dengan global scope 
name = "ucup"#ini adalah global scope
"""
variabale global scope bisa di akses di 
manapun dan kapan pun 
"""
#cara mengakses global scope menggunakan method 
"""
dan bagaimana cara kita agar si variabale
global scope bisa di rubah data nya 
di dalam method
"""
def say_halo(ubah):
  global name#memberi tau program bahwa variabale name adalah global scope
  name = ubah
  print(f"halo {name}")

say_halo("yanto")

"""
sedang kan static scope atau variabale static 
hanya bisa di akses di dalam funtion saja
"""
#contoh static scope
def halo():
  names = "halo guys"#static scope
  print(names)

halo()
#print(names)#ini tidak bisa 