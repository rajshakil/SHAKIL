'''
Created on Sep 28, 2013

@author: Shakil Ahmad
'''

import unittest
from Shakil_8 import *

obj = sharePrice()
class sharePriceUnitTest(unittest.TestCase):	
	def testProcessRecords(self):
		print "\n----------------From Unit Test---------------\n"
		input = raw_input("Please enter the CSV's file name (Path is required if input is in different location from source code):\n") 
		obj.processRecords(input.strip())		
	
	# You can test it by providing the companies information here in a dictionary format as well
	def testShareInfo(self):
		companiesDetails = {'Month': ['Jun', 'Sep'], 'Company N': [ '50', '500'], 'Year': [ '2000', '2013'], 'Company D': [ '85.2', '33']}		
		obj.getShareInfo(companiesDetails)
    
if __name__ == '__main__':
    unittest.main()
