#!/usr/bin/python3
import socket
from Crypto.Cipher import AES
key = "@@@@@@@@@@@@@@@@"
encry = AES.new(key, AES.MODE_CBC, 'This is an IV456')
decry = AES.new(key, AES.MODE_CBC, 'This is an IV456')
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('172.16.12.87', 443))
while True:
	data = client_socket.recv(1024)
	if (data == 'q' or data == 'Q'):
		client_socket.close()
		break
	else:
		try:
			data = data.decode()
		except:
			data = decry.decrypt(data)
			data = data.decode()
			data = data.replace('@','')
		print(data)
		data = input("")
		if (data == 'Q' or data == 'q'):
			client_socket.send(data)
			exit()
		else:
			while len(data) % 16 !=0:
				data = data + '@'
			data = encry.encrypt(data)
			print('sending:')
			print(data)
			client_socket.send(data)
