#!/usr/bin/python2.7

"""Twitter Project"""

__version__ =  '1.1.1'

from setuptools import find_packages, setup

setup(name = 'Pytweets',
	package = ['Pytweets'],
	version = '0.3',
	descripiton = 'A test module:Pytweets',
	Summary = 'A test module:dPytweets',
	long_description = 'A module for printing all the tweets/re-tweets you/anyone have/has done till date.',
	platforms = ["Linux"],
	author = "Rahul Mishra",
	author_email = "priyrahulmishra@gmail.com",
	url= "https://github.com/Rahul91/pytweet",
	download_url = "https://github.com/Rahul91/pytweet/tarball/0.1",
	license = "MIT",
	keywords = ['twitter', 'Tweets', 'testing'],
	packages = find_packages()
	)