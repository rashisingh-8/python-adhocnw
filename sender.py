#!/usr/bin/env python2

import socket

ip = "127.0.0.1"	#receiver's ip and port
port = 9090	#ports > 6000 are usually free

# Calling UDP protocol
#			(ipv4)		(UDP)
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

# sending message to target
while True:
	msg = raw_input("Enter text you want to send : ")
	s.sendto(msg,(ip,port))	#This function automatically binds its 
				#own ip and port and sends it to the 
				#receiver along with the message.
	# this is for receiving acknowledgement from the receiver	
	print s.recvfrom(10)
