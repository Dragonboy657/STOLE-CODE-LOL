#message of the day server
import socket
import random

message = "penis"

HOST = ''
PORT = 17

print("MOTD server v0.1")

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(5)

while True:
	conn, addr = s.accept()
	print("Connection recieved from: ", addr)
	conn.send((message).encode())
	conn.close()
