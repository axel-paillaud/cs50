from cs50 import get_int

n = 999
while(n < 1 or n > 8):
    n = get_int("Height: ")


for i in range(n):
    for j in range(i + 1):
        for k in range(n - (i + 1)):
            print(" ", end="")
        print("#", end="")
    print()
