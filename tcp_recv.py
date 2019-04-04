#!/usr/bin/python2

import socket

# Step 1. Create socket object
s=socket.socket()

# Step 2. Binding ip and port
s.bind(("",9991))	# leaving ip field empty binds all available ips on your system to given port.

# Step 3. Listen number of consecutive connections
s.listen(50)	# max 50 connections

# Step 4. Receiver must accept connection from client
# data variable --> client's ip+port,client's socket
while True:
	cliskt,cliaddr = s.accept()
	print cliskt
	print cliaddr
	# Step 5. Receive actual data
	print cliskt.recv(100)	# 100 is the buffer size
	cliskt.send("Ok")

s.close()
