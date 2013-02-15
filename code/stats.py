#!/usr/bin/python
"""This script can be used to analyze data in the 2012 Presidential Campaign,
available from http://www.fec.gov/disclosurep/PDownload.do"""

import fileinput
import csv

total = 0
minimum = None
maximum = None
records = 0 
donationlist = []
candidates =  dict()
paymentstatuslist = dict()
candidatesdevolutions = dict()
candidatescontributors = dict()
candidatescities = dict()
negativerecords=0
positiverecords=0



for row in csv.reader(fileinput.input()):
	if not fileinput.isfirstline():
		records+=1
		value = float(row[9]) 
		contributorname = row[3]
		candidatename = row[2]
		paymentstatus = row[11]
		contributorcity = row[4]
		# I noticed some negative values that makes no sense to me, in the context of 
		# political contributions, so I decide to count those values 
		if value<=0:
			negativerecords+=1
		else:
			positiverecords+=1
		
		donationlist.append(value)
		# Extra calculations to check
		# without negative contributions!!!!!

		#total received per candidate
		if candidatename in candidates:
			candidates[candidatename].append(value)
		else:
			candidates[candidatename]=[value]

		#devolutions per candidate
		if candidatename in candidatesdevolutions and value<=0:
			candidatesdevolutions[candidatename]+=value
		else:
			candidatesdevolutions[candidatename]=value
		
		#distinct payment statuses
		if paymentstatus in paymentstatuslist:
			paymentstatuslist[paymentstatus]+=1
		else:
			paymentstatuslist[paymentstatus]=1
		
		# unique contributors (greedy, just by names)
		if candidatename in candidatescontributors:
			candidatescontributors[candidatename].add(contributorname)
		else:
			candidatescontributors[candidatename]=set(contributorname)
		
		if candidatename in candidatescities:
			citiespercandidate = candidatescities[candidatename]
			if contributorcity in citiespercandidate:
				citiespercandidate[contributorcity]+=1
			else:
				citiespercandidate[contributorcity]=1
		else:
			candidatescities[candidatename] = dict({contributorcity:1})


	###
	# TODO: calculate other statistics here
	# You may need to store numbers in an array to access them together
	##/
	# print paymentstatuslist.keys()
print
print "--------------------------"
print "Number of records in file %s" % records
print "Positive contributions %s - Percentage: %3.2f" % (positiverecords, (positiverecords*100.00/records))
print "Negative/zero contributions %s - Percentage %3.2f" % (negativerecords, (negativerecords*100.00/records))
print "--------------------------"
print

donationlist = sorted(donationlist)
minimum = min(donationlist)
maximum = max(donationlist)
total = sum(donationlist)
records = len(donationlist)


mean=total/records
median=0.0
if records % 2 == 0:
	median = donationlist[records/2]+donationlist[records/2-1]/2
else:
	median = donationlist[records/2]

# testing standard deviation
# donationlist = [2,4,4,4,5,5,7,9]
# records = len(donationlist)
# mean = sum(donationlist)/len(donationlist)
# #result  = 2

std = (sum([(value- mean)**2.0 for value in donationlist])/records)**0.5

##### Print out the stats
print "           Records: %15d" % records 
print "             Total: %15.5f" % total
print "           Minimum: %15.5f" % minimum
print "           Maximum: %15.5f" % maximum
print "              Mean: %15.5f" % mean
print "           Median: %15.5f" % median
# square root can be calculated with N**0.5
print "Standard Deviation: %15.5f" % std

print "--------------------------"
print
##### Comma separated list of unique candidate names
print "Candidates: %s" % sorted(candidates.keys()) 

print "--------------------------"
print
def minmax_normalize(value):
	#"""Takes a donation amount and returns a normalized value between 0-1. The
	#	normilzation should use the min and max amounts from the full dataset"""
	###
	# TODO: replace line below with the actual calculations
	norm = (value-minimum)/(maximum-minimum)
  ###
	return norm

def z_normalize(value):
	znorm = (value - mean)/std	
	return znorm

##### Normalize some sample values
print "Min-max normalized values: %r" % map(minmax_normalize, [2500, 50, 250, 35, 8, 100, 19])

print "z normalized values: %r" % map(z_normalize, [2500, 50, 250, 35, 8, 100,     19])

# ordering data... i need to learn an elegant way to do this with python :(
citiespercandidate = dict()
for candidate in candidatescities.keys():
	orderlist = sorted(candidatescities[candidate], key=candidatescities[candidate].get)
	citiespercandidate[candidate] = [orderlist[-1],candidatescities[candidate][orderlist[-1]],orderlist[0],candidatescities[candidate][orderlist[0]]]

print '\nContributors per city (top/bottom)'
for key in citiespercandidate.keys():
	print "  %30s  cities: %s" % (key,str(citiespercandidate[key]))

print '\nTotal of unique contributors (per name)'
for key in candidatescontributors.keys():
	print "  %30s  U.Cont.: %d" % (key,len(candidatescontributors[key]))

print '\nContributions per candidate'
for key in candidates.keys():
	print "  %30s  contribution avg.: %10.2f   max: %10.2f" % (key,sum(candidates[key])/len(candidates[key]),max(candidates[key]))

