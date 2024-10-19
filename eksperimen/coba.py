import fn

#kallulator sederhana 

# num1 = int(input("masukan angka : "))
# operasi = input("masukan operasi : '+,X,-,/' : ")
# num2 = int(input("masukan angka : "))
# 
# if operasi == "+":
#   hasil = fn.pertambahan(num1,num2)
#   print(f"hasil {num1} + {num2} = {hasil}")
# elif operasi == "X" or operasi == "*":
#   hasil = fn.perkalian(num1,num2)
#   #print(f"hasil {num1 "X" num2 " = " hasil}")
#   print(f"hasil {num1} X {num2} = {hasil}")
# elif operasi == "-":
#   hasil = fn.pengurangan(num1,num2)
#   #print(f"hasil {num1 "-" num2 " = " hasil}")
#   print(f"hasil {num1} - {num2} = {hasil}")
# elif operasi == "/":
#   hasil = fn.pembagian(num1,num2)
#   #print(f"hasil {num1 "/" num2 " = " hasil}")
#   if num2 != 0:
#     print(f"hasil {num1} / {num2} = {hasil}")
#   else:
#     print("jangan di bagi nol bang")

#kallulator faktorial 
while True:
  faktorial = int(input("masukan angka : "))
  hitung = fn.faktorial(faktorial)
  print(hitung)