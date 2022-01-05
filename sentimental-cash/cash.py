from cs50 import get_float

change = -1
coins = 0
while(change < 0):
    change = get_float("Change owed: ")

if(change >= 0.25):
    n = change / 0.25
    n = int(n)
    for i in range(n):
        coins+= 1
        change -= 0.25
change = round(change, 2)

if(change >= 0.10):
    n = change / 0.10
    n = round(n)
    for i in range(n):
        coins += 1
        change -= 0.10
change = round(change, 2)

if(change >= 0.05):
    n = change / 0.05
    n = round(n)
    for i in range(n):
        coins += 1
        change -= 0.05
change = round(change, 2)

if(change >= 0.01):
    n = change / 0.01
    n = round(n)
    for i in range(n):
        coins += 1
        change -= 0.01

print(coins)