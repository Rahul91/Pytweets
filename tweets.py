#!/usr/bin/python2.7

"""Twitter Project"""

__version__ = '1.1.1'

import urllib2
from bs4 import BeautifulSoup

username = raw_input("Enter your twitter_handle/username : ") 
link = "https://twitter.com/" + username

def mytweets():
	
	"""
	Function to print all the tweets/re-tweets you have done so far.

	"""

	url = urllib2.urlopen(link)
	soup = BeautifulSoup(url)
	var = soup2.find('title')
	print var.text

	var2 = soup.find_all('p', {"class" : "ProfileTweet-text js-tweet-text u-dir"})
	for items in var2:
		print items.text
		print " "
	raw_input("Press Enter to exit :)")


if __name__ == "__main__":
	mytweets()
