from cs50 import get_int

n = 999
while(n < 1 or n > 8):
    n = get_int("Height: ")

space = n - 1
hash = False
for i in range(n):
    for j in range(i + 1):
        for k in range(space):
            if hash == False:
                print(" ", end="")
        print("#", end="")
        hash = True
    for l in range(1):
        print("..", end="")
    hash = False
    space -= 1
    print()
