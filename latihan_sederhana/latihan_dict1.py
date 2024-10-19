#latiham nested dictionary 
import datetime
import os 

data_template = {
  "nama":"nama",
  "gender":"gender",
  "umur":0
}
os.system("clear")
"""
fungsi dict.fromkeys adalah untuk mengambil
semua key yang ada pada dictionary di atas
untuk membuat dictionary yang baru
"""
data = dict.fromkeys(data_template.keys())
data["nama"] = input("masukan nama kamu : ")
data["gender"] = input("masukan gender kamu : ")
data["umur"] = input("masukan umur kamu : ")
print(data)