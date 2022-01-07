import csv

titles = []

with open("favorites.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        if not row["title"] in titles:
            titles.append(row["title"])