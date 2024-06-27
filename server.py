import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('192.2.6.108',12345))
s.listen()

conn, addr = s.accept()
data = conn.recv(1024)
conn.sendall("Hola, soy compu 12".encode())
print(data)