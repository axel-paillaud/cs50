pizzas = {
"cheese": 9,
"pepperoni": 10,
"vegetable": 11,
"buffalo chicken": 12
}

pizzas["bacon"] = 14

for pie, price in pizzas.items():
    print(" Une pizza {} coûte €{}".format(pie, price))