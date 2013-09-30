'''
Created on Sep 28, 2013

@author: Shakil Ahmad
'''

import csv
import unittest

class sharePrice():
	
	def processRecords(self, input):
		try:			
   			with open(input,'rb') as csvfile:
   				reader = csv.DictReader(csvfile, delimiter=",")
   				keys = []
   				values = []  
   				d={} 			
   				for rec in reader:
   					for k,v in rec.items():
   						keys.append(k.strip())
   						values.append(v.strip())
   				
   				x = zip(keys, values)
   				for k, v in x:
   					try:
   						d.setdefault(k, [  ]).append(v)
   					except KeyError:
   						d[k] = v
   				self.getShareInfo(d)
   				
   		except IOError as e:
	   		print "I/O error({0}): {1}".format(e.errno, e.strerror)
	
	def getShareInfo(self, listCompanies = {}):
		print "\nCompany Name\tHighest Share\tMonth\tYear"
		maxShareIndex = 0
		for k,v in listCompanies.iteritems():
			if k in ('Month', 'Year'):
				continue						
			maxShareIndex = [item for item in range(len(v)) if v[item] == max(v)]
			maxShareIndex = maxShareIndex[-1]						
			print k + "\t" +  max(v) + "\t" + listCompanies['Month'][maxShareIndex] + "\t" + listCompanies['Year'][maxShareIndex]									

'''
To stop running it from main class, Please comment the below 4 lines of code
by adding the hash (#) tag  
'''        	
obj = sharePrice()
print "\n----------------From Main Class---------------\n"
input = raw_input("Please enter the CSV's file name (Path is required if input is in different location from source code):\n") 
obj.processRecords(input.strip())
