#menghitung huruf vokal 
def huruf_vokal(teks):
  vokal = "aeiouAEIOU" 
  jumlah_vokal = 0
  for abjat in teks:
    if abjat in vokal:
      jumlah_vokal += 1 
  return jumlah_vokal

user_input = input("masukan teks : ")
count = huruf_vokal(user_input)
print(count)