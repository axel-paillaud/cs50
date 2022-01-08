import csv
import sys
import os
import os.path

if len(sys.argv) != 2:
    print("Usage: data.py [name of the csv file]")
    sys.exit

print(os.listdir())
input = sys.argv[1]

with open(input, 'r') as file:
    reader = csv.DictReader(file)
