#operasi pada list 

data_angka =[1,1,3,5,5,5,7,6,5,7,9,9,9,7,7,7,2,2]
#menghitung item yang sering keluar di list 
hitung1 = data_angka.count(2)
hitung2 = data_angka.count(5)
print(f"angka 2 berapa kali keluar = {hitung1}")
print(f"angka 5 berapa kali keluar = {hitung2}")
#memcari posisi item (index)
#contoh data.index(item)
data = ["budi","aat","bujang","udang"]
print(f"data = {data}")
scr_index = data.index("bujang")
print(f"data ada di index = {scr_index}")

#cara mengururtkan item list 
print(f"data sebelum di sort : \n{data_angka}")
data_angka.sort()
print(f"data sesudah di sort : \n{data_angka}")

