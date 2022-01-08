import csv
import sys
import os
import os.path


if len(sys.argv) != 2:
    print("Usage: data.py [name of the csv file]")
    sys.exit

input = sys.argv[1]
print(input)

cur_dir = os.getcwd()
file_list = os.listdir(cur_dir)


with open(input) as file:
    reader = csv.DictReader(file)

