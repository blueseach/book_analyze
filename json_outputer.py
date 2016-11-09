# -*- coding: utf-8 -*-
"""
Created on Tue Nov  1 11:44:31 2016

@author: Administrator
"""

# coding:utf-8
import json
class JsonOutputer(object):
	def __init__(self):
		# init a list to contain list of dicts 
		self.data = []

	def collect_data(self, data):
		if data is None:
			return
		self.data.append(data)

	def output_json(self,name):
		with open(name,'w') as fout:
			json.dump(self.data, fout)
   
	def output_txt(self,name):  
           print(self.data)            
           f = open(name,'w+')  
           f.write(self.data)  
           f.close()  