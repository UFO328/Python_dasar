#latihan list 
#membuat lits data diri 

data_diri = []

while True:
  #meminta user memberikan data diri 
   user_name = input("masukan nama : ")
   user_age = input("masukan umur anda : ")
   user_gender = input("masukan gender anda : ")

   if user_gender == "PRIA":
     print("whastup bro\n")
   elif user_gender == "WANITA":
     print("HEI NONA\n")
   else:
     print("gender tidak terdeteksi\n")

   data_list = [user_name,user_age,user_gender]
   data_diri.append(data_list)
   
   for data in data_diri:
     print(10*"=","DATA","="*10)
     print(f"halo nama kamu : {data[0]}")
     print(f"umur kamu : {data[1]}")
     print(f"gender kamu : {data[2]}\n")