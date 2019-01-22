#!/usr/bin/python2

import os,sys


if len(sys.argv) == 1:
	for i in os.listdir("."):
		print i
else :
	for i in os.listdir(sys.argv[1]):
		print i
