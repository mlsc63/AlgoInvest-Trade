import csv


def open_csv():
    with open('../data/dataset1.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        name = []
        price = []
        profit = []
        for row in csv_reader:
            if line_count != 0:
                name.append(row[0])
                price.append(int(row[1]))
                profit.append(int(row[2]))
            line_count += 1
        return name, price, profit


open_csv()


def brute_force(profit, price, capacity):
    numbers_of_possibility = 2 ** len(profit)
    print('Le nombre de combinaison possible sera de: 2^', len(profit), '=', numbers_of_possibility, 'possibilités')
    combination = []

    gain = 0
    # on fait une boucle dans laquelle on va générer la suite binaire par rapport à un nombre
    for num in range(numbers_of_possibility):
        binary = bin(num)[2:]
        value_backpack = 0
        price_backpack = 0
        # on stock les valeurs dans une liste temporaire:
        for index, value in enumerate(binary):
            if value == '1':
                value_backpack = value_backpack + profit[index]
                price_backpack = price_backpack + price[index]
        if capacity >= price_backpack and value_backpack > gain:
            gain = value_backpack
            combination = binary
    return gain, combination


name, price, profit = open_csv()
gain, combinaison = brute_force(profit, price, 500)
print("Voici les actions les plus rentables pour 500€")
total_price = 0
for index, value in enumerate(combinaison):
    if value == '1':
        total_price = total_price + price[index]
        print('Name:', name[index], ' prix', price[index], 'profit', profit[index], '%')
print('On dépensera au total:', total_price, '€')
