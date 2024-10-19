#tipe data list 

#list adalah kumpulan data 
#kita bisa memasuki berbagai jenis tipe data 
#seperti float,int,str,dan boolean 

#cara membuat list 

#a = ["riski",1,1.2,True]
#print(a)
#memgakses list dengan for loop

# for i in a :
#   print(i)

data = ["riski","dwi","syahputra"]

#opeeasi manipulasi list

#menambahkan item sesuai urutan index 
#contoh -> data.insert(index,obj)
#menggunakan insert untuk menambahkan item list 
print(10*"=","insert","="*10)
data.insert(1,"enjoy")#akan menambahkan item list sesuai dengan index yang ditentukan
print(data)
print(10*"=")

print(10*"=","append","="*10)
#contoh menggunakan append 
#contoh -> data.append("item")
#append akan otomatis menambahkan item di akhir list 
data.append("budi ")
print(data)

#cara mengambil data list menggunakan index 
print(f"mengambil dara list ke-[0] : {data[0]}")
print(f"mengambil dara list ke-[-1] : {data[-1]}")#jika memulai dari index -1 maka dara yang di ambil adalah data yang paling terakhir

#cara menghitung panjang list 
print(10*"=","menghitung panjang list")
panjang = len(data)
print(f"panjang data list nya adalah : {panjang}")

#cara menghapus item di dalam list
#dengan menggunakan command del 
#contoh -> del data[index]

del data[2]#menghapus menggunakan del harus sesuai index
print(data)

#cara menghapus item berdasarkan nama item atau nama obj 
#menggunakan remove
#contoh -> data.remove("item")
data.remove("enjoy")
print(data)

#menghapus item terakhir 
#contoh -> data.pop()
data.pop()
print(data)

#mengubah item list 
data[0] = "acong"
print(data)
