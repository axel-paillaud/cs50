import csv
import sys


if len(sys.argv) != 2:
    print("Usage: data.py [name of the csv file]")
    sys.exit


fdata = open(sys.argv[1], 'r')
reader = csv.DictReader(fdata)
