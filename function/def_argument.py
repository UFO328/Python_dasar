#function dengan argumen

#contoh function dengan argumen
#def nama_function(parameter_atau_variable):
  #blok kode program 

#cara pembuatan 
def name(nama):#variable yang di dalam kurung nama nya parameter 
  print(f"hello {nama} {type(nama)}")

"""
jika sebuah function atau method,jika method
atau function tersebut memiliki parameter, 
di saat kita memanggil function harus dengan 
argumen atau real value 
"""
#contoh -> nama_function(argumen)
name("riski")
name(10)
"""
jika function memiliki 2 atau lebih parameter 
mengirim argumen nya harus sesuai jumlah 
parameter yang ada pada function
"""
#contoh function yang lebih dari satu parameter

def hello(nama,umur,gender):#untuk pemisah nya menggunkan koma(,)
    print(f"halo {nama}")
    print(f"umur kamu {umur}")
    print(f"gender kamu {gender}")
#contoh pemanggilan nya hello(argumen1,argumen2,argumen3) pemisah nya koma 
hello("riski",17,"pria")

#cara mengirim argumen berupa data list 
def lists(date_list):
  date_people = date_list.copy()
  for dates in date_people:
    print(f"halo wahai {dates}")
    
data_siswa = ["riski","otong","petong"]
lists(data_siswa)