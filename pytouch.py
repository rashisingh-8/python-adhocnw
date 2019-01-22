#!/usr/bin/python2

import os,sys

args = sys.argv[1:]
for i in args:
	if os.path.exists(i):
		print i+" already exists."
	else :
		os.mkdir(i)
