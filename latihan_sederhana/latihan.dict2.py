#latihan dict 2 
import os 
import string 
import random

#data template 
data_diri = {
  "nama":"nama",
  "status":"status",
  "umur":0,
  "gender":"gender"
}

data_satuan = {}

while True:
  
  print("\n")
  print("DATEBASE MASYARAKAT")
  #untuk mengambil semua key data_diri ke data_copy
  data_copy = dict.fromkeys(data_diri.keys())
  data_copy["nama"] = input("masukan nama : ")
  data_copy["status"] = input("masukan status anda : ")
  data_copy["umur"] = int(input("masukan umur anda : "))
  data_copy["gender"] = input("masukan gender anda : ")
  key = "".join((random.choice(string.ascii_uppercase) for i in range(3)))
  
  data_satuan[key] = data_copy
  
  print(f'{"KEY":<3} {"NAMA":<6} {"STATUS":>6} {"UMUR":^6} {"GENDER":>10}')
  for dates in data_satuan:
    KEY = dates 
    NAMA = data_satuan[KEY]["nama"]
    STATUS = data_satuan[KEY]["status"]
    UMUR = data_satuan[KEY]["umur"]
    GENDER = data_satuan[KEY]["gender"]
  print(f'{KEY:<3} {NAMA:<10} {STATUS:<6} {UMUR:^6} {GENDER:>10}')
  
  