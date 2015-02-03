# Script for preprocessing and analysis of PhoneTime.csv
# Preprocessing: collect dates and call times
# Analysis: 
#	Call length distribution
#	Call length over time
#	Call length by day of week
#	Call length by previous call length
#
#	PJL 2/3/2015

# TODO:
# Add option to combine phone calls within days

import csv
import datetime
import numpy as np
import matplotlib.pyplot as plt
import math
import pylab


def main():

	# preprocessing
	my_list = csvToList()
	call_times = getCallTimes(my_list)
	dates = getDates(my_list)
	
	# ... may want additional step to collect calls on same day
	print "Calls have not been combined within days"
	print "There are " + str(countDuplicateDays(dates)) + " days out of " + str(countDays(dates)) + " with multiple calls"

	# analysis

	## distribution of call lengths
	callTimesHist(call_times)

	## call lengths through time
	callTimesThroughTime(dates,call_times)

	## call lengths by day of week

	## call lengths by previous call length

	## make figures visible
	plt.show()

def csvToList():
	# read csv into list

	with open('PhoneTime.csv', 'rb') as f:
		reader = csv.reader(f)
		my_list = list(reader)
	return my_list

def getCallTimes(my_list):
	# return list of call times in minutes, one for each phone call

	call_times = []
	for i in range(len(my_list)):
		if i == 0:
			continue # skip header of csv
		else:
			h = float(my_list[i][1])
			m = float(my_list[i][2])
			s = float(my_list[i][3])
			call_times.append(h*60.0 + m + s/60.0)
	return np.array(call_times, float)

def getDates(my_list):
	# return list of date objects, one for each phone call
	# see https://docs.python.org/2/library/datetime.html

	dates = []
	for i in range(len(my_list)):
		if i == 0:
			continue # skip header of csv
		else:
			date_MDY = my_list[i][0].split("/")
			month = int(date_MDY[0])
			day = int(date_MDY[1])
			year = int(date_MDY[2])
			
			dates.append(datetime.date(year, month, day))

	return dates

def getOrdinals(dates):
	# get ordinals for each date

	ordinals = []
	for d in dates:
		ordinals.append(d.toordinal())
	return ordinals

def countDays(dates):
	# Count number of unique days

	ordinals = getOrdinals(dates)
	return len(set(ordinals))

def countDuplicateDays(dates):
	# Count number of days with multiple calls
	
	ordinals = getOrdinals(dates)
	ordinals.sort()

	duplicates = 0
	for i in range(1,len(ordinals)):
		if i > 1:
			if ordinals[i] == ordinals[i-1] and ordinals[i] != ordinals[i-2]:
				duplicates += 1
		elif i == 1:
			if ordinals[i] == ordinals[i-1]:
				duplicates += 1

	return duplicates

def callTimesHist(call_times):
	# Plot histogram of call times in 10 minute bins

	M = call_times.max()
	rangeMin = 0
	rangeMax = 100*math.ceil(M/100)
	bins = math.ceil((rangeMax-rangeMin)/10.0)

	fig = plt.figure()
	ax = fig.add_subplot(111)
	ax.set_title('Histogram of Call Times')
	ax.set_xlabel('Call Time (min)')
	ax.set_ylabel('Count')

	ax.hist(call_times,bins=bins,range=(rangeMin,rangeMax))
	
def callTimesThroughTime(dates,call_times):
	# Plot call times over time
	ordinals = getOrdinals(dates)

	assert len(ordinals) == len(call_times)

	fig = plt.figure()
	ax = fig.add_subplot(111)
	ax.set_title("History of Call Times")
	ax.set_xlabel("Time (Date Ordinal)")
	ax.set_ylabel("Call Time (min)")

	ax.plot(ordinals,call_times,'ko')



main()