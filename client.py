#!/usr/bin/python3
import socket
from Crypto.Cipher import AES
key = '@@@@@@@@@@@@@@@@'
MAXRECV = 100000

key = input('Key: ')
while len(key) % 16 !=0:
	key = key + '@'
key.encode()

encry = AES.new(key, AES.MODE_CBC, 'This is an IV456')
decry = AES.new(key, AES.MODE_CBC, 'This is an IV456')

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
IP = input('IP: ')
port = input('Port: ')
client_socket.connect((IP, int(port)))

while True:
	data = client_socket.recv(MAXRECV)
	data = decry.decrypt(data)
	data = data.replace(b'@',b'')
	data = data.decode()

	print(data)

	if (data == 'Closing Connection...'):
		exit(0)

	data = input('')
	while len(data) % 16 !=0:
		data = data + '@'
	data = encry.encrypt(data)
	client_socket.send(data)
