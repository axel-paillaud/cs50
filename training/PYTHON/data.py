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
while find == False:

    file_list = os.listdir(cur_dir) # Liste des fichiers du dossier actuel
    print(file_list)
    dir_count = 0
    tmp = 0

    for file in file_list:
        if os.path.isdir(cur_dir + "/" + file) == True:
            dir_count += 1

    print(dir_count)

    parent_dir = os.path.dirname(cur_dir) # Dossier parent par rapport au dossier actuel

    if input in file_list:
        print("Fichier trouvé")
        break
    else:
        while tmp != dir_count:
            for file in file_list:
                file_path = cur_dir + "/" + file
                if os.path.isdir(file_path) == True:
                    tmp += 1
                    list_search = os.listdir(file_path)
                    if input in list_search:
                        print("Fichier trouvé")
                        find = True
                        break
                    

    if cur_dir == parent_dir: # Si le dossier actuel est le dossier root
        sys.exit("Fichier non trouvé")
    else:
        cur_dir = parent_dir

input = file_path + "/" + input

with open(input) as file:
    reader = csv.DictReader(file)

