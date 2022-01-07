dict = {"Axel":"0671007241", "Leila":"0649193277", "Maman":"0628372454"}

print(dict["Axel"])

list = list(dict.values())

print(list[0:2])

list[0] = int(list[0])

list[1] = int(list[1])

sum = list[0] + list[1]

print(list)

print(sum)

