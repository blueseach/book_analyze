# -*- coding: utf-8 -*-
"""
Created on Tue Nov  1 09:30:14 2016

"""

import urllib.request



class Downloader(object):


  
	def download(self,url):
     #安全原因，这里把cookie拿掉了
		HEADERS = {"User-Agent":'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.113 Safari/537.36',"cookie":''}
		req = urllib.request.Request(url=url,  headers=HEADERS)
		response = urllib.request.urlopen(req)

		if response.getcode()!= 200:
			print("Request failed! with stats_code %s!",response.getcode)
			return None

		return response
		  
  
  