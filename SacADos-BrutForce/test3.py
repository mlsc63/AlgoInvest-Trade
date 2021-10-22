import time
name = ['apple', 'google ']
profit = [500, 250, 1500, 1200, 1200, 800]
price = [4, 3, 10, 12, 9, 6]
capacity = 30
# 2^n
numbers_of_possibility = 2 ** len(profit)
print('Le nombbre de combinaisson possible sera de: 2^', len(profit), '=', numbers_of_possibility, 'possiblités')
combinaison = []

gain = 0
for num in range(numbers_of_possibility):
    binary = bin(num)[2:]
    value_backpack = 0
    price_backpack = 0
    # on stock les valeurs dans une liste temporel:
    for index, value in enumerate(binary):
        #print(index, value)
        if value == '1':
            value_backpack = value_backpack + profit[index]
            price_backpack = price_backpack + price[index]
            #print('le sac est de', value_backpack)
    if capacity >= price_backpack and value_backpack > gain:
        gain = value_backpack
        combinaison = binary



print(gain)
print(combinaison)



