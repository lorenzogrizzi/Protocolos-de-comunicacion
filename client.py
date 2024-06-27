import socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(('192.168.182.204', 12345))
s.send("Hola dios".encode())
response = s.recv(1024).decode()
print(response)