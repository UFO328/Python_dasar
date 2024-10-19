#latihan menggunakan if,elif dan else stateman

#program sederhana menentukan nilai murid 

nilai_uts = float(input("masukan nilai : "))
nilai_un = float(input("masukan nilai : "))

#pengecekkan logika dengan if,elif dan else stateman.
if nilai_uts > 90 and nilai_un > 90:
  print("nilai agregat anda 'A'")
elif nilai_uts >= 80 and nilai_un >= 85:
  print("nilai agregat anda 'B'")
elif nilai_uts > 70 and nilai_un > 75 :
  print("nilai agregat anda 'C'")
elif nilai_uts >= 60 and nilai_un > 65 :
  print("nilai agregat anda 'D'")
else:
  print("nilai agregat anda 'SANGAT BURUK'")