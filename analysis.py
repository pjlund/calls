# Script for preprocessing and analysis of PhoneTime.csv
#	PJL 2/3/2015

def main():

	import numpy as np

	# preprocessing
	my_list = csvToList()
	print my_list
# analysis

## call lengths through time

## call lengths by day of week

## call lengths by previous call length

def csvToList():
	import csv
	with open('PhoneTime.csv', 'rb') as f:
		reader = csv.reader(f)
		my_list = list(reader)
	return my_list

main()