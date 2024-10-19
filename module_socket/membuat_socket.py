"""
create socket
kostanta keluarga(family)protocol
AF_UNIX -> untuk domain unix 
AF_INET -> untuk protocol ipv4
AF_INET6 -> untuk protocol ipv6 
AF_STREAM -> untuk stream socket(tcp)
AF_DGRAM -> untuk datagram socket(udp)
"""
#cara penggunana 
#import module socket 
import socket
#cara penggunan AF_INET dan AF_STREAM
sock = socket.socket(AF_INET,AF_STREAM)

#cara menghubungkan socket.connect berfungsi untuk menghubungkan socket ke server
#menggunakan method connect 
#harus di kirim sebagai tuple
sock.connect(('localhot','port'))
#contoh lain 
sock.connect(('192.168.1.1',8080))
#connect berfungsi agar kita bisa terhubung ke layanan server 
#setelah itu kita mengikat socket atau binding
sock = socket.bind(('localhot','port'))
#contoh lain 
sock = socket.bind(("192.168.1.1",8080))
#berfungsi untuk mengukat socket ke port 

#setelah itu gunakan method listen untuk mengitrusikan port untuk listen pada port yang sudah di bind atau diikat

sock.listen(5)#mendegarkan koneksi dengan maksimum minimal 5 antrian 

#menerima koneksi(accepting)
sock.accept()#menerima koneksi
#berfungsi untuk menerima request client 

#menerima data koneksi(sending)
sock.send('ini pesan dari server')

#menerima data koneksi dari server menggunakan method recv(bufsize)
sock.recv(1024)#menerima data sebesar 1024 byte

#menutup koneksi menggunakan method close()
sock.close()