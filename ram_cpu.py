#!/usr/bin/env python2
import commands

ram = commands.getoutput("free -m") #execution of linux command through python
	
final_mem = ram.split()[7] #.split() function to convert a string into a list
	
cpu = commands.getoutput("lscpu | grep -i model | tail -1")
	
print "System RAM :"+final_mem+" MB"
	
print "CPU information :"+cpu
