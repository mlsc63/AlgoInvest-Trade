import csv
import time


def open_csv():
    with open('../data/dataset2.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        data = []

        for row in csv_reader:
            if line_count != 0:
                if row[1] != 0.0 and '-' not in row[1]:
                    data.append([row[0], float(row[1]), float(row[2])])
            line_count += 1
        return data


def sacADos_dynamique(capacite, elements):
    matrice = [[0 for x in range(capacite * 100 + 1)] for x in range(len(elements) + 1)]

    for i in range(1, len(elements) + 1):
        for w in range(1, capacite * 100 + 1):
            if int(elements[i - 1][1] * 100) <= w:
                matrice[i][w] = max(elements[i - 1][2] + matrice[i - 1][w - int(elements[i - 1][1] * 100)],
                                    matrice[i - 1][w])
            else:
                matrice[i][w] = matrice[i - 1][w]

    w = capacite * 100
    n = len(elements)
    elements_selection = []

    while w >= 0 and n >= -1:

        print('boucle:', elements[n - 1])
        e = elements[n - 1]

        if (matrice[n][w]*100) == int((matrice[n - 1][w - int(e[1]*100)] + int(e[2]*100))):
            elements_selection.append(e)
            w -= int(e[1]*100)
        n = n - 1

    return matrice[-1][-1], elements_selection


# ele = open_csv()
# print(ele)
# print('Algo dynamique', sacADos_dynamique(500, ele))


ele = [('Montre à gousset', 2.5, 6),
       ('Boule de bowling', 3.2, 10),
       ('Portrait de tata Germaine', 4, 12)]
print('Algo dynamique', sacADos_dynamique(5, ele))

# w = capacite
# n = len(elements)
# elements_selection = []

# while w >= 0 and n >= 0:
#    e = elements[n - 1]
#    if matrice[n][w] == matrice[n - 1][w - e[1]] + e[2]:
#        elements_selection.append(e)
#        w -= e[1]
# return matrice[-1][-1], elements_selection
