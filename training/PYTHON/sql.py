import csv

from CS50 import SQL

db = SQL("sqlite:///data.db")

name = input("Name: ")

db.execute(")