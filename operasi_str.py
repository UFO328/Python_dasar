#operasi string atau manipulasi string 

#1.menyambaung string (concatenate)
firts_name = "enjoy"
middle_name = "The"
last_name = "famous"

firts_name = firts_name+" "+middle_name+" "+last_name
print(firts_name)

#2.menghitung panjang string 
loong = len(firts_name)
print("panjang nama "+firts_name+ " = "+str(loong))

#3.operasi string 

#memcari komponen string dalam string 

search = "e"
temukan = search in firts_name#mencari komponen yang ada dalam string 
print("apaka ada huruf e di "+firts_name+" = "+str(temukan))

search = "t"
temukan = search not in firts_name#mencari komponen yang tidak ada dalam stirng 
print("apaka tidak ada huruf t di "+firts_name+" = "+str(temukan))

#mengulang string
print("="*20)
print(99*"wk")

#indexing 

print("index ke-[0] : "+firts_name[0])
print("index ke-[0:5] : "+firts_name[0:5])
print("index ke-[0:6:7] : "+firts_name[0:6:7])

#4.method string 
name = "riski dwi syhahputra "
hitung = name.count("i")#menhitung jumlah i pada nilai variablr name 
print("jumlah i pada "+name+"adalah = "+str(hitung))

