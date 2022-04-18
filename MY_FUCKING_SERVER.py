#message of the day server
import socket
import random

message = "Wow I don't know if this will work because I stole it all."

HOST = ''
PORT = 69

print("MOTD server v0.1")

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(5)

while True:
	conn, addr = s.accept()
	print("Connection recieved from: ", addr)
	conn.send((message).encode())
	conn.close()
