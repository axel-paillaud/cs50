import csv

with open("favorites.csv", "r") as file:
    reader = csv.reader(file)
    next(reader) # Ici on passe la première ligne, qui correspond à Time, name, title etc
    for row in reader:
        print(row[1])