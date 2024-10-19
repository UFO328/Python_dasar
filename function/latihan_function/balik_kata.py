#method untum membalik kata 

def reversed_teks(teks):
  kata_kata = teks.split()
  balik = kata_kata[::-1]
  return " ".join(balik)
hasil = reversed_teks("halo guys apa kabar semua")
print(hasil)