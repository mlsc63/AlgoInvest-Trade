import csv
import time


def open_csv(root):
    with open(root) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        data = []

        for row in csv_reader:
            if line_count != 0:
                if row[1] != '0.0' and '-' not in row[1] and row[2] != '0.0':
                    taux = round((float(row[1]) * float(row[2])), 2) * 100
                    my_liste = (row[0], float(row[1]), taux, float(row[2]))
                    data.append(my_liste)
            line_count += 1
        return data


def sacADos_dynamique(capacite, elements):
    matrice = [[0 for x in range(capacite * 100 + 1)] for x in range(len(elements) + 1)]

    for i in range(1, len(elements) + 1):
        for w in range(1, capacite * 100 + 1):
            if int(elements[i - 1][1] * 100) <= w:

                matrice[i][w] = round(max(elements[i - 1][2] + matrice[i - 1][w - int(elements[i - 1][1] * 100)],
                                          int(matrice[i - 1][w])), 2)
            else:
                matrice[i][w] = round(matrice[i - 1][w], 2)
    w = capacite * 100
    n = len(elements)
    elements_selection = []

    while w >= 0 and n >= 0:
        e = elements[n - 1]
        if matrice[n][w] == round(matrice[n - 1][w - int(e[1] * 100)] + e[2], 2):
            elements_selection.append(e)
            w -= int(e[1] * 100)
        n -= 1
    return elements_selection


def start(root):
    start = time.time()

    ele = open_csv(root)
    elements = sacADos_dynamique(500, ele)
    euro = 0
    benefice = 0

    for i in elements:
        print('Name: ', i[0], ' Price: ', i[1], ' Profit ', round((i[3] * i[1]) / 100, 2), '€')
        euro += round(i[1], 2)
        benefice += (i[3] * i[1]) / 100
    print('La somme totale dépensée est de:', round(euro, 2), '€ et le bénéfice est de:', round(benefice, 2), '€.')
    end = time.time()
    elapsed = end - start

    print(f'Temps d\'exécution : ', elapsed, ' secondes.')


while True:
    file = input('Veuillez choisir un fichier: 1=dataset.csv, 2=dataset1_Python+P7.csv, 3=dataset2_Python+P7.csv')
    if file == '1':
        root = '../data/dataset.csv'
        start(root)
    elif file == '2':
        root = '../data/dataset1_Python+P7.csv'
        start(root)
    elif file == '3':
        root = '../data/dataset2_Python+P7.csv'
        start(root)
    else:
        print('Valeur non correct')
