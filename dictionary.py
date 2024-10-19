"""
dictionary adalah kumpulan data yang tidak memilki index
tetapi memilki key dan value unik 
jadi ketika kita mau mengakses nilai dict 
kita harus mengaksesnya melalui key nya
didalam dict kita juga bebas memasukan data apa saja mau itu int,float,str,bool,bahkan list sekalipun bisa di masukan kedalam dict 
"""

#cara membuat dictionary 

  
data_dict = {
  "key":"value",
  "nama":"riski",
  "number":12
} #di awali dengan tanda kurung kuawal

#cara mengakses dict
print(data_dict["nama"])
#cara mengakses meggunakan method get 
print(data_dict.get("nama"))

"""
operasi pada dictionary cukup banyak contoh 
method untuk dictionary
keys()-> untuk memgambil semua key dari sebuah dictionary
values-> untuk menambil semua value dari sebuah dictionary
items()-> untuk mengambil key dan kuci dari sebuah dictionary
"""

#cara menggunakan for loop untuk mengamabil kucil dictionary menggunakan method keys()
print("memgambil key dictionary dengan for loop")
for key in data_dict.keys():
  print(key)

#cara menggunakan for loop untuk memgambil nilai dictionary menggunakan method values()
print("memgambil value dictionary dengan for loop")
for value in data_dict.values():
  print("\t",value)
  
  
#menggunakan for loop untuk mengamabil semua key dan value menggunakan method items()
print("memgambil key dan value dictionary dengan for loop")
for value in data_dict.items():
  print("\t",value)
  
#cara mengupdate data dictionary
#dengan cara sederhana 
data_dict["nama"] = "enjoy"
print("\n",data_dict)

#cara mengupdate data dictionary dengan method update 
"""
jika menggunakan method update jika pasangan
key dan value tidak ada maka akan otomatis
ke add sebagai key dan value baru 
"""
data_dict.update({"nama":"ahmed"})
print(data_dict)

#cara menghitung panjang dictionary 
panjang = len(data_dict)
print(panjang)

#cara memgetahui apakah key ada atau tidak di dalam dictionary
cari = "nama" in data_dict
print(cari)
