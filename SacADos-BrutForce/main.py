import csv
import time


def open_csv():
    with open('../data/dataset.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        name = []
        price = []
        profit = []
        for row in csv_reader:
            if line_count != 0:
                name.append(row[0])
                price.append(int(row[1]))
                pro = round((float(row[1]) * float(row[2]) / 100), 2)
                profit.append(pro)
            line_count += 1
        return name, price, profit





def brute_force(profit, price, capacity):
    print(capacity)
    numbers_of_possibility = 2 ** len(profit)
    print('Le nombre de combinaison possible sera de: 2^', len(profit), '=', numbers_of_possibility, 'possibilités')
    combination = []
    gain = 0

    for num in range(numbers_of_possibility):
        binary = bin(num)[2:].zfill(len(profit))
        tempo_price = 0
        tempo_profit = 0
        for i in range(len(binary)):
            if binary[i] == '1':
                tempo_price += price[i]
                tempo_profit += profit[i]

        if tempo_profit > gain and tempo_price <= capacity:
            gain = tempo_profit
            combination = binary

    return gain, combination


start = time.time()
name, price, profit = open_csv()
gain, combinaison = brute_force(profit, price, 500)
print("Voici les actions les plus rentables pour 500€")
total_price = 0
total_profit = 0
for index, value in enumerate(combinaison):
    if value == '1':
        total_profit = total_profit + profit[index]
        total_price = total_price + price[index]
        print('Name:', name[index], ' prix', price[index], 'profit', profit[index], '€')
print('On dépensera au total:', total_price, '€, et on aura un profit de:', round(total_profit, 2), '€')
end = time.time()
elapsed = end - start
print(f'Temps d\'exécution : ', elapsed, ' secondes.')
