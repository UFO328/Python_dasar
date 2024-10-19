def celcius_to_fahrenheit(celcius):
  fahrenheit= (9/5)*celcius+32 
  return fahrenheit 

user = float(input("masukan suhu dalam celcius : "))

convert = celcius_to_fahrenheit(user)

print(f"suhu dalam fahrenheit : {convert}")
