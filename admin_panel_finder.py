#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from urllib2 import Request, urlopen, URLError, HTTPError

def Space(j):
	i = 0
	while i<=j:
		print " ",
		i+=1


def findAdmin():
	f = open("link.txt","r");
	link = raw_input("Site Adresini Giriniz \n(ex : ornek.com or www.ornek.com ): ")
	print "\n\nTespit Edilen Linkler : \n"
	while True:
		sub_link = f.readline()
		if not sub_link:
			break
		req_link = "http://"+link+"/"+sub_link
		req = Request(req_link)
		try:
			response = urlopen(req)
		except HTTPError as e:
			continue
		except URLError as e:
			continue
		else:
			print "OK => ",req_link

def Credit():
	
Space(9); print "|<<<<<<<<<<<<<<<<|>>>>>>>>>>>>>>>>>>|"
Space(9); print "|   +++ Admin Panel Finder v| +++   |"
Space(9); print "|       Coded by TurKLoJeN          |"
Space(9); print "|    	  Turkish Pentester          |"
Space(9); print "|<<<<<<<<<<<<<<<<|>>>>>>>>>>>>>>>>>>|"
    
Credit()
findAdmin()
