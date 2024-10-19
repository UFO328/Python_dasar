#kwargs parameter 

def date(**kwargs):
    """
    Fungsi ini menerima parameter dalam bentuk keyword arguments (kwargs),
    yang berarti argumen dikirim sebagai pasangan key-value dan disimpan
    dalam bentuk dictionary.
    
    Keyword arguments ini bisa digunakan saat kita tidak tahu secara
    pasti berapa banyak argumen yang akan diterima oleh fungsi, 
    tetapi ingin mengirimnya dengan cara yang eksplisit (key-value).
    """

    # Akses nilai dari kwargs menggunakan key-nya (nama, umur, tinggi)
    nama = kwargs["nama"]  # Mengambil nilai dari key "nama"
    umur = kwargs["umur"]  # Mengambil nilai dari key "umur"
    tinggi = kwargs["tinggi"]  # Mengambil nilai dari key "tinggi"

    # Menampilkan data yang diambil dari kwargs
    print(f"nama kamu {nama}")  # Display nama
    print(f"umur kamu {umur}")  # Display umur
    print(f"tinggi kamu {tinggi}")  # Display tinggi

# Memanggil fungsi dengan keyword arguments
date(nama="riski", umur=17, tinggi=185)  # nama, umur, dan tinggi dikirim sebagai kwargs

#contoh studi kasus dengan *args dan kwargs

def hitung(*num,**operation):
  operation["operasi"]
  output = 0
  if operation["operasi"] == "tambah":
    for angka in num:
      output += angka
      
  elif operation["operasi"] == "kali":
    output = 1
    for angka in num:
      output *= angka
      
  else:
    print("operasi ga ada")
  return output

tambah = hitung(8,8,7,operasi="tambah")
kali = hitung(2,1,7,operasi="kali")

print(f"ini hasil jumlah : {tambah}")
print(f"ini hasil kali : {kali}")