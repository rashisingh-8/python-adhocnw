#!/usr/bin/python
import cgi	#To receive data from web-server
import cgitb	# For tracing errors
cgitb.enable()

print "Content-type:text/html"	#this is http proto header (OSI)
print ""

# Extracting n1 and n2 from web page
web = cgi.FieldStorage()
a = web.getvalue("n1")
b = web.getvalue("n2")

print int(a)+int(b)

# print "<pre>"
# print commands.getoutput(c)
# print "</pre>"
