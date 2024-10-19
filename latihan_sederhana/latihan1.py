

#latihan 1 
#latihan gabungan angka 

#++++++++++4-----------9++++++++++++++ 
#gabungkan rentang nilai 4 dan 9 

#meminta input user 
user = float(input("masukan angka kurang dari 4 atau lebih dari 9 : "))

hasil = user < 4 or user > 9 
print("apakah sudah benar : ",hasil)

#irisan 
#------------4+++++++++++++9---------- 
#iriskan angka 4 dan 9 

#meminta user input 
user = float(input("masukan angka lebih dari 4 dan  kurang dari 9 : "))

hasil = user > 4 and user < 9 
print("apakah sudah benar : ",hasil)
