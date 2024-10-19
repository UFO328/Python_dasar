#loop dictionary 



data_diri = {
  "nama":"riski",
  "umur":17,
  "gender":"pria"
}

#cara mengambil key dictionary menggunakan method keys() dan for loop 
print("MEMGAMBIL KEY DICTIONARY")
for data in data_diri.keys():
  print(f"\tkey nya adalah : {data}")

#cara mengambil value dictionary menggunakan method values() dan for loop 

print("MENAMBIL VALUE DICTIONARY")

for date in data_diri.values():
  print(f"\tvalue nya adalah : {date}")

#cara mengambil key dan value dictionary menggunakan method items() dan for loop 

print("MENAMBIL KEY DAN VALUE DICTIONARY")
for key,item in data_diri.items():
  print(key,item)

  
