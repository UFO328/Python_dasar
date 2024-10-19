"""
nested dict adalah dictionary bersarang 
cara penggunaan nested dictionary
"""

data1 = {
  "nama":"riski",
  "umur":17,
  "gender":"pria"
}
data2 = {
  "nama":"asep",
  "umur":19,
  "gender":"pria"
}
data3 = {
  "nama":"enjoy",
  "umur":20,
  "gender":"pria"
}

#cara menggunakam nested dictionary
dict_satuan = {
  #key:value. valuenya variable dari dict yang ada di atas 
  "MH001":data1,
  "MH002":data2,
  "MH003":data3
}
#cara mengambil data nested dict 
print(f'{"KEY":<5} {"NAMA":<10} {"UMUR":^5} {"GENDER":>6} ')
print("-"*30)

for mahasiswa in dict_satuan:
  KEY = mahasiswa
  NAME = dict_satuan[KEY]["nama"]
  UMUR = dict_satuan[KEY]["umur"]
  GENDER = dict_satuan[KEY]["gender"]
  print(f'{KEY:<5} {NAME:<10} {UMUR:^5} {GENDER:>6}')
  print("-"*30)
  
  