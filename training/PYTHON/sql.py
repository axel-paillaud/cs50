import csv

from cs50 import SQL

db = SQL("sqlite:///data.db")

name = input("Name: ")

rows = db.execute("SELECT firstname FROM data WHERE firstname = '?'", name)
print(rows)