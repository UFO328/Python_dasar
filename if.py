#if statemen berfungsi untuk mengecek sebuah kondisi jika benar blok.kode progran di bawah nya akan di jalan kan 

#contoh if statemen 
#user = input("masukan nama : ")

#if user == "riski":
  #print(f"halo {user}")
  
#contoh if else statemen 

#angka = 10 

#if angka > 10: 
  #print(f"{angka} itu angka besar")#ini akan di eksekusi jika variable angka value nya lebih dari 10 
#else:
  #print(f"{angka} itu angka kecil")#ini akan di eksekusi jika variable valie nya kurang dari 10 atau sama dengan 10
  
#if bercabang 

nilai = int(input("masukan nilai : "))
nilai_un = int(input("masukan nilai um : "))

if nilai >= 90 and nilai_un > 90:
  print("nilai anda 'BAGUS'")#ini akan di eksekusi jika kondisi terpenuhi
#untuk if bercabang keyword nya elif 
elif nilai > 60 and nilai_un > 78:
  print("nilai anda 'CUKUP BAGUS'")#ini akan di  eksekusi jika if di atas nya atau elif di atasnya kondisinya tidak terpenuhi
else:
  print("nilai anda 'SANGAT BURUK'")#ini akan di eksekusi jika seluruh kondisi tidak terpenuhi