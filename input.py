#input berfingsi menerima inputan data atau
#masukan data dari uset 

#contoh input user bertipe data string 
name = input("masukan nama : ")#walaupun user menginput angka,data tetap berupa string 

#contoh input user bertipe data float dan int 

number = int(input("masukan angka : "))
pecahan = float(input("masukan bilangan angaka : "))
print(number,"bertipe data",type(number))
print(pecahan,"bertipe data",type(pecahan))

#contoh input user bertipe boolean 
#harus di casting 3 kali 
boolean = bool(int(input("masukan boolean : ")))
print(boolean,"bertipe data",type(boolean))