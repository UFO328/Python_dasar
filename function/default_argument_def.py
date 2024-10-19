#function dengan default value 
"""
function dengan default value adalah
ketika function di buat lalu didalam 
function tersebut di isi parameter
lalu parameter nya di kasih nilai 
saat deklarasi nya 
lalu,jika ingin memberi default value 
harus di beri di parameter akhir 
"""

#def function(parameter=valuenya)

#contoh function tanpa default value
# def function(nama):
#   print(f"halo {nama}")
# function()#pemanggilan error karna tidak di beri argument 

#contoh function dengan default value
def halo(nama="kamu"):
  print(f"halo {nama}")

halo()#output akan menjadi "halo kamu"
halo("riski")#output akan "halo riski"

#contoh dengan default value yang baca 
def angka(num1=1,num2=2,num3=3,num4=4):
  return num1+num2+num3+num4

#mengambil beberapa parameter 
print(angka(num2=5,num4=7))#output akan "16"