#mengakses list denga loop

#memgakses list dengan for loop 
print("\nMENGAKSES LIST DENGAN FOR LOOP")
data = [1,6,7,9,0,9,7]

for angka in data:
  print(f"data angka : {angka}")

print("\nMENGAKSES LIST DENGAN WHILE LOOP")
#mengakses list dengan while 
data_name =["tatang","adung","bujang"]
panjang_data = len(data_name)
print(panjang_data)
i = 0
while i < panjang_data :
  print(f"nama kamu : {data_name[i]}")
  i += 1
  
print("\nMENGAKSES LIST DENGAN FOR LOOP compherison")
#mengakses lisy dengan for loop compherison
[print(i) for i in data_name]

#menggunakam enumerate

for index,name in enumerate(data_name):
  print(f"nama : {name},index ke : {index}")
  
