from cs50 import get_float

change = -1
coins = 0
while(change < 0):
    change = get_float("Change owed: ")

int dollars = round(change)

for i in range(change):
    if(change > 0.25):
        i += 0.25
        coins += 1

print(coins)