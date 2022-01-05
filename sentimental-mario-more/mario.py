from cs50 import get_int

n = 999
while(n < 1 or n > 8):
    n = get_int("Height: ")

space = n - 1
for i in range(n):
    for j in range(i + 1):
        for k in range(space):
            print(" ", end="")
        print("#", end="")
    space -= 1
    print()
