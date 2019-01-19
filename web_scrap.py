#!/usr/bin/python

from googlesearch import search
import urllib2

# Now put a keyword
webdata = search("hello",num=3,stop=2,pause=1)

# generator type is iterable
print type(webdata)	# type is 'generator'

for i in webdata:
	print i
	link = urllib2.urlopen(i)
	print link.read()
