#continue,pass,break 

#pass -> fungsinya untuk dummy,atau tidak akan di jalan kan oleh program 

# angka = 0
# 
# while angka < 5:
#   angka += 1 
#   if angka == 2:
#     pass #tidak akan di jalan kan oleh program
#   
#   print(f"{angka}")

#continue
#continue -> berfungsi untuk melanjutkan ke step berikutnya 

angka = 7
while angka > 1:
  angka -= 1 
  if angka == 3:
    continue#ini tidak akan melanjutkan kode yang ada dibawah tapi akan lanjut ke ste berikutnya 
    print("heyyo whatup")
print(f"ini angka {angka}")

#break 
#break -> untuk menghetikan loop 

# angka = 0  
# while True :
#   angka += 1 
#   print(f"{angka}")
#   if angka == 20:
#     break
# print("end loop")
  
