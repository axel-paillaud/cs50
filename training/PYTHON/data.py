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

    file_list = os.listdir(cur_dir)         # Liste des fichiers du dossier actuel
    dir_count = 0
    tmp = 0

    for file in file_list:
        file_path = cur_dir + "/" + file

        if file == "root":                  # Pour éviter d'aller chercher dans le dossier "root" et d'avoir un message d'erreur "acces denied"
            sys.exit("Fichier non trouvé")
        if os.path.isdir(file_path) == True:
            dir_count += 1


    parent_dir = os.path.dirname(cur_dir)   # Dossier parent par rapport au dossier actuel

    if input in file_list:
        print("Fichier trouvé")
        break
    else:
        while tmp != dir_count:             # Tant qu'on a pas fait tout les dossiers de la liste
            if find == True:
                break
            for file in file_list:
                file_path = cur_dir + "/" + file

                if os.path.isdir(file_path) == True:
                    tmp += 1
                    list_search = os.listdir(file_path)     #Liste des fichiers/dossiers dans le dossier dans lequel on cherche

                    if input in list_search:
                        print("Fichier trouvé")
                        find = True
                        break

    if find == True:
        break
    elif cur_dir == parent_dir:     # Si le dossier actuel est le dossier root
        sys.exit("Fichier non trouvé")
    else:
        cur_dir = parent_dir

if find == True:                    # Si on a trouvé le fichier dans les sous-dossiers, alors find == True, et il faut suivre le path suivant :
    input = file_path + "/" + input
else:                               # Sinon, le fichier trouvé était dans le dossier actuel, et il faut prendre le path suivant :
    input = cur_dir + "/" + input

data = []

with open(input) as file:
    reader = csv.DictReader(file)
    next(reader)
    for row in reader:
        data.append(row)

print(data)
