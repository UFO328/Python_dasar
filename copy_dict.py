"""
jika kita ingin mengcopy data dict kita harus
menggunakan method copy() agar dict ketika di 
ganti di dict yang bukan yang asli data tidak berubah
"""

date_diri = {
  "nama":"riski",
  "umur":17 
}

date = date_diri.copy()#ketiak date mengganti value nya dict date_diri tidak akan berubah valuenya
