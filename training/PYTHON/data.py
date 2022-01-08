import csv
import sys


if len(sys.argv) != 2:
    print("Usage: data.py [name of the csv file]")
    sys.exit


with open(sys.argv[1], 'r') as file:
    reader = csv.DictReader(file)
