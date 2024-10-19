#casting berfungsi untuk merubah tipe data


print(10*"=","INT",10*"=")
#contoh casting data int ke tipe data lain 
data_int = 10#akan di casting menjadi tipe data lain

#merubah variablw data_int yang bertipe data int menjadi tipe data float 
data_float = float(data_int)

#merubah variablw data_int yang bertipe data int menjadi tipe data str/string 
data_str = str(data_int)

#merubah variablw data_int yang bertipe data int menjadi tipe data boolean 
data_bool = bool(data_int)#nilai akan True atau False, True jika data yang di casting nilai nya lebih dari 0,  dan False jika data yang di casting nilai nya sama dengan 0 


print("ini",data_int,"bertipe data",type(data_int))
print("ini",data_float,"bertipe data",type(data_float))
print("ini",data_str,"bertipe data",type(data_str))
print("ini",data_bool,"bertipe data",type(data_bool))

print(10*"=","FLOAT",10*"=")
#merubah tipe data float ke tipe data lain

data_float = 4.5 #akan di casting menjafi tipe data lain 

data_int = int(data_float)#angkanya akan di bulatkan 
data_str = str(data_float)
data_bool = bool(data_float)
print("ini",data_int,"bertipe data",type(data_int))
print("ini",data_float,"bertipe data",type(data_float))
print("ini",data_str,"bertipe data",type(data_str))
print("ini",data_bool,"bertipe data",type(data_bool))

print(10*"=","STR",10*"=")
#merubah tipe data string ke tipe data lain

data_str = "5" #akan di casting menjadi tipe data lain 

data_int = int(data_str)#string tidak boleh tipe data float jika ingin di casting menjadi int dan str tidak boleh huruf atau charakter
data_float = float(data_str)
data_bool = bool(data_str)
print("ini",data_str,"bertipe data",type(data_str))
print("ini",data_float,"bertipe data",type(data_float))
print("ini",data_int,"bertipe data",type(data_int))
print("ini",data_bool,"bertipe data",type(data_bool))