#!/usr/bin/python

# Format of each line is:
# date\ttime\tstore name\titem description\tcost\tmethod of payment
#
# We want elements 2 (store name) and 4 (cost)
# We need to write them out to standard output, separated by a tab

import sys
import re


for line in sys.stdin:
    	#print line ,type(line)
	
	#data = line.strip()
	#print data
	
	result=map(''.join, re.findall(r'\"(.*?)\"|\[(.*?)\]|(\S+)',line))
	#print 'length',len(result)
	if len(result) >7:
		continue
	ip,rfc,userid,timezone,protocol,statuscode,byteobject = result
	
	
	#print "{0}\t{1}\t{2}\t{3}\t{4}\t{5}\t{6}".format(ip,rfc,userid,timezone,protocol,statuscode,byteobject)
	
	#trip= protocol.strip().split(" ")
	if len(ip) == 0 or len(statuscode) == 0 or ip == None or statuscode == '':
		continue

	print "{0}\t{1}".format(ip,statuscode)
	#result = re.search(line)
	#print result.groups()
    	
	

	'''
    	if len(data) == 6:
        	#cost=int(cost)
        date, time, store, item, cost, payment = data
        #cost=int(cost)
        print "{0}\t{1}".format(store, cost)
    	'''
