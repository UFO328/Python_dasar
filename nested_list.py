"""
nested list adalah list di dalam list atau list
bersarang 
"""
#contoh nested list 
list_1 = [1,2,3]
list_2 = [4,5,6]
list_3 = [7,8,9]

nested_lits = [list_1,list_2,list_3]
print(f"\n{nested_lits}")

#contoh penggunana nested_lits

nama = ["otong",25,"laki-laki"]
gender = ["ujang",23,"laki-laki"]
umur = ["otong",25,"laki-laki"]

print("CONTOG PENGGUNAAN NESTED LIST ")
list_satuan = [nama,gender,umur]
for peserta in list_satuan:
  print(f"nama \t: {peserta[0]}")
  print(f"umur \t: {peserta[1]}")
  print(f"gender \t: {peserta[2]}\n")