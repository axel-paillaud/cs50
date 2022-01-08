import csv
import sys


if len(sys.argv) != 2:
    print("Usage: data.py [name of the csv file]")
    sys.exit

input = sys.argv[1]

with open(input) as file:
    reader = DictReader(file)

