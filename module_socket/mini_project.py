from socket import socket,sys

password = input("masukan password root : ")

class Net:
  def __init__(self):
    if len(sys.argv) != 3:
      print("usege"+sys.argv[0]+"<host_ip> <port>")
      sys.exit 
    else:
      self.HOST = sys.argv[1]
      self.PORT = int(sys.argv[2])
      self.prompt = '<chat>'
  def create(self):
    try:
      #membuat koneksi dengan tcp 
      s = socket.socket(socket.AF_INET,socket.AF_STREAM)
    except:
      print("socket error...")
    else:
      #mengikat ke port 
      s.bind(self.HOST,self.PORT)
      #mendegarkan koneksi
      s.listen(5)#mendegarkan sebanyak 5 kali 
      #menerima koneksi
      koneksi,alamat = s.accept()
    #selamat datang ke client 
    koneksi.send(password)
    stat = 0 
    #stat = 0 tdk terkoneksi
    #stat = 1  terkoneksi
    while 1:
     data = koneksi.recv(100)
     if not data: break 
     if stat == 0:
       if data.strip() == "password":
         stat = 1 
         isi = self.prompt 
         koneksi.send("anda telah login")
       else:
         isi = password
     else:
         if data[:8] == "hostname":
           host = data.split(' ')[1]
           self.prompt = host.strip() + '> '
           isi = self.prompt
         if data.strip() in ["keluar"]:
           koneksi.close
           break
    print(f"data di terima {data}")
    koneksi.send(isi)
    s.close
net = Net()
net.create