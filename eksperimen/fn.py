#membuat method aritmatika 

#method untuk operasi pertambahan 
def pertambahan(number1,number2):
  '''perhitungan number1 + number2'''
  return number1 + number2 

#method untuk operasi perkalian 
def perkalian(number1,number2):
  '''perhitungan number1 X number2 '''
  return number1 * number2

#method untuk pengurangan
def pengurangan(number1,number2):
  '''perhitungan number1 - number2'''
  return number1 - number2 

#method untuk pembagian 
def pembagian(number1,number2):
  '''perhitungan number1 / number2 '''
  if number2 % 2 != 0:
    return number1 / number2 

#method untuk faktorial 
def faktorial(number1):
  if number1 > 0:
    hitung = 1 
    for i in range(1,number1 + 1):
      hitung *=i 
    return hitung 
  else:
    hitung = "Value must be greater than zero"
  return hitung

#method untuk konversi celcius ke fahrenheit 
def celcius(fahrenheit):
  celcius = (fahrenheit * 9/5)+32
  return celcius

#method untuk konversi fahrenheit ke celcius
def fahrenheit(celcius):
  pass