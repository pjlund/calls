# Script for preprocessing and analysis of PhoneTime.csv
#	PJL 2/3/2015
import numpy as np
import csv

def main():

	# preprocessing
	my_list = csvToList()
	call_times = getCallTimes(my_list)

	print call_times
# analysis

## distribution of call lengths

## call lengths through time

## call lengths by day of week

## call lengths by previous call length

def csvToList():

	with open('PhoneTime.csv', 'rb') as f:
		reader = csv.reader(f)
		my_list = list(reader)
	return my_list

def getCallTimes(my_list):
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

main()