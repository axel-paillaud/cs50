import csv
import sys
import os
import os.path


if len(sys.argv) != 2:
    print("Usage: data.py [name of the csv file]")
    sys.exit

input = sys.argv[1]
cur_dir = os.getcwd() # Dossier actuel

find = False
while True:

    file_list = os.listdir(cur_dir) # Liste des fichiers du dossier actuel
    dir_count = 0
    tmp = 0

    for file in file_list:
        file_path = cur_dir + "/" + file

        if file == "lib32" or "root" or "boot" or "libx32" or "run" or "dev":
            sys.exit("Fichier non trouvé")
        if os.path.isdir(file_path) == True:
            dir_count += 1


    parent_dir = os.path.dirname(cur_dir) # Dossier parent par rapport au dossier actuel

    if input in file_list:
        print("Fichier trouvé")
        break
    else:
        while tmp != dir_count:
            if find == True:
                break
            for file in file_list:
                file_path = cur_dir + "/" + file
                if os.path.isdir(file_path) == True:
                    tmp += 1
                    list_search = os.listdir(file_path)
                    if input in list_search:
                        print("Fichier trouvé")
                        find = True
                        break

    if find == True:
        break
    elif cur_dir == parent_dir: # Si le dossier actuel est le dossier root
        sys.exit("Fichier non trouvé")
    else:
        cur_dir = parent_dir

if find == True:
    input = file_path + "/" + input
else:
    input = cur_dir + "/" + input

with open(input) as file:
    reader = csv.DictReader(file)

