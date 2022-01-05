import cs50

x = cs50.get_int("x: ")
y = cs50.get_int("y: ")

if x < y:
    print("x est inférieur à y")
elif x > y:
    print("x est supérieur à y")
else:
    print("x est égal à y")