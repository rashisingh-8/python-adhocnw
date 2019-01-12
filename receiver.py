#!/usr/bin/env python2

import socket

ip = "127.0.0.1"
port = 9090 #ports > 6000 are usually free

# Calling UDP protocol
#			(ipv4)		(UDP)
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)	#if an argument is not given, TCP socket is created by default

# ============================ above code is common for sender and receiver ==================

# binding ip and port
s.bind((ip,port))	#tuple as argument because it is immutable and we do not need to change

# receiving data from sender in format (message,(ip,port))
while True:
	recv = s.recvfrom(100)			#100 is the buffer size in character
	print "Data received : ", recv[0]
	s.sendto("Ok, Got it", recv[1])		#recv[1] contains the ip and port of the sender
