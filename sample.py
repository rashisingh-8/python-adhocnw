#!/usr/bin/env python2

import webbrowser
import commands #to import commands of the operating system of base machine

option='''
Press 1 to check your OS version :
Press 2 to login to your facebook account :
Press 3 to check RAM and CPU in your current machine :
Press 4 to search something in google search engine :
Press 5 to list out all IP and MAC addresses in your current network :
'''

print option
# to take input from user in python2
choice=raw_input()

if int(choice) == 1 :
	print "My OS is RHEL"
elif int(choice) == 2 :
	execfile('web_auto.py')
elif int(choice) == 3 :
	#execfile(<filename>), alternate option
	execfile('ram_cpu.py')
	#ram = commands.getoutput("free -m") #execution of linux command through python
	#final_mem = ram.split()[7] #.split() function to convert a string into a list
	#cpu = commands.getoutput("lscpu | grep -i model | tail -1")
	#print "System RAM :"+final_mem+" MB"
	#print "CPU information :"+cpu
elif int(choice) == 4 :
	data=raw_input("Type something to search on google :")
	webbrowser.open_new_tab('https://www.google.com/search?q='+data)
else :
	print "No valid option given"
	exit()
execfile('sample.py')
