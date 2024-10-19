#menghitung luas dan keliling persegi 
import os 
#membuat function header 
def header():
  '''function header'''
  print(f"{'keliling dan persegi':^40}")
  print(f"{'ketik 1 untuk menghitung luas dan ketik 2 untuk menghitung keliling':^20}")
  print(f"{'-'*40}")

#function untuk input
def user_input():
  '''function for user input'''
  panjang = int(input("masukan angka : "))
  lebar = int(input("masukan lebar : "))
  return panjang,lebar

#function untuk menghitung luas persegi panjang
def luas(panjang,lebar):
  '''function perhitungan untuk keliling'''
  return panjang*lebar

#function untuk menghitung keliling persegi panjang
def keliling(panjang,lebar):
  return 2*(panjang+lebar)

#function untuk display hasil 
def display(pesan,hasil):
  '''function untuk display hasil'''
  print(f"{pesan} : {hasil}")

#membuat program berjalan 
while True:
  #memanggil fungsi header
  header()
  pilih = input("masukan angka pilihan : ")
  if pilih == "1":
    panjang,lebar = user_input()
    hasil = luas(panjang,lebar)
    display("hasil perhitungan luas adalah",hasil)
  elif pilih == "2":
    panjang,lebar = user_input()
    hasil = keliling(panjang,lebar)
    display("hasil perhitungan keliling adalah",hasil)
  user = input("lanjut atau tidak 'y/n' : ")
  if user == "n":
    break