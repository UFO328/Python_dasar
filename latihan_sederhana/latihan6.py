#membuat sistem kasir sederhana 

#menampilkan daftar barang 
print("""
______________________________
|No | List barang     | Harga |
|1  | Beras     1 KG  |12000  | 
|2  | Telur     1 KG  |25000  |
|3  | Indomie   1 DUS |45000  |
|___|_________________|_______|
""")

#meminta user memilih barang 
user_choise = int(input("masukan nomor pilihan : "))
#meminta user memasukan jumlah barang yang mau di beli 
user_amount = int(input("masukan jumlah barang yang di inginkan : "))

#inisialisasi harga dan nama baeang 
if user_choise == 1:
  harga = 12000
  nama_barang = "Beras"
elif user_choise == 2: 
  harga = 25000
  nama_barang = "Telur"
elif user_choise == 3:
  harga = 45000
  nama_barang = "Indomie"
else:
  print("PILIH AJA YANG ADA DI MENU COK")
  exit()
#untuk menghitung harga yang akan di tentukan
harga_total = harga*user_amount
print(f"Total belanjaan anda : {harga_total:,.0f},mohon lakukan pembayaran")

#meminta user untuk melakukan pembayaran 
user_paying = int(input("bayar di sini :"))

diskon = 0 #dummy variable 

if harga_total > 50000:
  diskon = 0,1 
  before_price = harga_total*diskon
  after_price = harga_total-before_price
  print("anda mendapatkan diskon sebesar 10%")
elif harga_total > 100000:
  diskon = 0,20 
  before_price = harga_total*diskon
  after_price = harga_total-before_price
  print("anda mendapatkan diskon sebesar 20%") 
elif harga_total >= 150000:
  diskon = 0.3 
  before_price = harga_total*diskon
  after_price = harga_total-before_price
  print("anda mendapatkan diskon sebesar 30%")
else:
  after_price = harga_total
  print("yah kamu ga dapet diskon :(")
  
#untuk menghitung uang kembalina 
hitung = user_paying - after_price

print(10*"=","PERINCIAN BELANJA",10*"=")
print(f"nama barang : {nama_barang}")
print(f"jumlah barang : {user_amount}")
print(f"Total : {after_price}")
print(f"kembalian : {hitung}")