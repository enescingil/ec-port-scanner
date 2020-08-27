#!/bin/python3
#Author: enestos

import pyfiglet
import sys
import socket
from datetime import datetime

if len(sys.argv) == 2:
	target=socket.gethostbyname(sys.argv[1])
else:
	print("Usage: python scanner.py <ip>")
	print("Add more arguments")
	sys.exit()

#Banner
banner = pyfiglet.figlet_format("EC SCANNER")
print(banner)
print("Target scanning: "+target)
print("Time started: "+str(datetime.now()))

try:
	for port in range(50,100):
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		socket.setdefaulttimeout(1)
		result = s.connect_ex((target, port))
		print("Scanning port: ".format(port))
		if result == 0:
			print("Port {} is open".format(port))
		s.close()

except KeyboardInterrupt:
	print("\nExiting program.")
	sys.exit()

except socket.gaierror:
	print("Hostname could not be resolved.")
	sys.exit()

except socket.error:
	print("EVERTHING IS BURNING AAAAAAA")
	sys.exit()
