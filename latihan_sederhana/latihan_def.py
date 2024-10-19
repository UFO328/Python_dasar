#latihan functiom dengan argumen

#membuat function aritmatika 

def tambah(num1,num2):
  result = num1 + num2
  return result
def kali(num1,num2):
  result = num1 * num2
  return result
def kurang(num1,num2):
  result = num1 - num2
  return result
def bagi(num1,num2):
  if num2 != 0:
   result = num1 / num2
   return result
  else:
    result = "jangan di bagi nol bang"
    return result

#function factorial 
def factorial(n):
  if n >0:
    faktor = 1
    for i in range(1,n+1):
      faktor *= i
  return faktor

user_input = int(input("masukan angka : "))
user_input2 = int(input("masukan angka : "))
result = bagi(user_input,user_input2)
print(f"{result}")