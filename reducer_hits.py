#!/usr/bin/env python

import sys

old_key = None
c=0

for line in sys.stdin:
	result = line.strip().split('\t')
	#print 'result',result
	##print line ,len(line)
	item0,item1 = result
	#print 'type0',type(item0),'item1',type(item1)
	#if len(item0) == 0 or len(item1) ==0:
	#	continue
	#if item1 != '200':
	#	continue
	
	if old_key and old_key !=item0:
		print "{0}\t{1}".format(old_key,c)
		c=0
	old_key=item0
	c=c+1

if old_key is not None:
	print "{0}\t{1}".format(old_key,c)

	'''
	data =line.strip().split("\t")
	
	if len(data) !=2 :
		continue
	
	store ,sale =data
	#sale =float(sale)
	
	#if old_store and old_store != store:
	#	print "{0}\t{1}".format(old_store,num_sale)
	#	max_sale=0

	res=res+ float(sale)
	#old_store=store
        c=c+1
#if old_store != None:
	print "{0}\t{1}".format(c,res)
	'''
