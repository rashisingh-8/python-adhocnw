#!/usr/bin/python

from googlesearch import search
from bs4 import BeautifulSoup
import requests
from time import sleep

# Now put a keyword to search in google
webdata = search("hello",num=3,stop=2,pause=1)
# this is the list of urls that we've already determined is safe and legal to scrape from.

# generator type is iterable
print type(webdata)
# type is 'generator'

for url in webdata:
	page_response = requests.get(url)
	# here, we fetch the content from the url, using the requests library
	page_content = BeautifulSoup(page_response.content, "html.parser")
	#we use the html parser to parse the url content and store it in a variable.
	complete_page = ""
	for data in page_content.find_all('p') :
		complete_page = complete_page+data.text
	print complete_page
	sleep(3)
