from cs50 import get_string

s = get_string("Est-ce que vous acceptez ?\n")

if s.lower() in  ["y", "yes"]:
    print("Validé")
elif s == "N" or s == "n":
    print("Annulé")