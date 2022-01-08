import csv
import sys
import os
import os.path


if len(sys.argv) != 2:
    print("Usage: data.py [name of the csv file]")
    sys.exit

input = sys.argv[1]

cur_dir = os.getcwd()
print(cur_dir)

file_list = os.listdir(cur_dir)
print(file_list)

parent_dir = os.path.dirname(cur_dir)
print(parent_dir)

with open(input) as file:
    reader = csv.DictReader(file)

