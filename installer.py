#!/usr/bin/python3
#Installer for server/client V4 and onwards
import os

#Windows Installer
if (os.name == "nt"):
	os.system("pip install pycryptodome")
	os.system("pip3 install pycryptodome")

#Linux Installer
else:
	os.system("sudo apt-get update")
	os.system("sudo apt-get install python3-pip -y")
	os.system("pip3 install pycryptodome")
