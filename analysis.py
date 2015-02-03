# Script for preprocessing and analysis of PhoneTime.csv
#	PJL 2/3/2015
import numpy as np
import csv
import datetime

def main():

	# preprocessing
	my_list = csvToList()
	call_times = getCallTimes(my_list)
	dates = getDates(my_list)
	print dates
# analysis

## distribution of call lengths

## call lengths through time

## call lengths by day of week

## call lengths by previous call length

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
	return call_times

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

main()