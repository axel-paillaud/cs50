from cs50 import get_string

people = {
    "Axel": "06.68.37.98.67",
    "Leila": "06.49.19.32.77"
}

name = get_string("Name: ")
if name in people:
    print(f"Numbers: {people[name]}")