#!/usr/bin/python2

import socket

# Step 1. Create socket object
s=socket.socket()

# If recv has started listening, we can connect
s.connect(("127.0.0.1",9991))

while True:
	msg = raw_input("Enter your message	:")
	s.send(msg)
	print s.recv(100)

s.close()
