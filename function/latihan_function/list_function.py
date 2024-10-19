#function dengan dict 

def data_dict(name,user):
  date = name.copy()
  for data in date:
    gate = data["nama"]
    if gate == user:
      print(f"nama anda {data["nama"]}")
    else:
      print("nama tidak ada")
dates ={
  "nama":"wahyu"
}
user_input = input("masukan nama : ")
data_dict(dates,user_input)