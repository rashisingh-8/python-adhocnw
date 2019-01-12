#!/usr/bin/env python2

from selenium import webdriver #for web automation
from time import sleep

usr=raw_input("Please enter your username : ")
passwd=raw_input("Please enter your password : ")

driver = webdriver.Firefox() #opens firefox browser
driver.get('https://www.facebook.com/') #to open facebook
print ("Opened facebook") 
sleep(1)

username_box = driver.find_element_by_id('email') 
username_box.send_keys(usr) 
print ("Email Id entered") 
sleep(1)

password_box = driver.find_element_by_id('pass') 
password_box.send_keys(passwd) 
print ("Password entered")

login_box = driver.find_element_by_id('loginbutton') 
login_box.click() 
  
print ("Done") 
input('Press anything to quit\n') 
driver.quit() 
print("Finished")

