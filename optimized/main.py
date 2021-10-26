import csv
import time


def open_csv():
    with open('../data/dataset2.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        data = []

        for row in csv_reader:
            if line_count != 0:
                if row[1] != '0.0' and '-' not in row[1]:
                    my_liste = (row[0], float(row[1]), float(row[2]))
                    data.append(my_liste)

                    #data.extend([row[0], float(row[1]), float(row[2])])
            line_count += 1
        return data


def sacADos_dynamique(capacite, elements):
    matrice = [[0 for x in range(capacite * 100 + 1)] for x in range(len(elements) + 1)]

    for i in range(1, len(elements) + 1):
        for w in range(1, capacite * 100 + 1):
            if int(elements[i - 1][1] * 100) <= w:

                matrice[i][w] = round(max(elements[i - 1][2] + matrice[i - 1][w - int(elements[i - 1][1] * 100)],
                                    int(matrice[i - 1][w])), 2)

                #print('matrice:', matrice[i][w], '== max(', elements[i - 1][2] + matrice[i - 1][w - int(elements[i - 1][1] * 100)],
                                    #int(matrice[i - 1][w]))


            else:
                matrice[i][w] = matrice[i - 1][w]

    #print(matrice)


    w = capacite * 100
    n = len(elements)
    elements_selection = []
    #print('w', w)

    while w >= 0 and n >= 0:
        e = elements[n-1]
        #print('e2', e[2])
        #print(matrice[n][w], '==', matrice[n-1][w-int(e[1]*100)] + e[2], 'e[2]:', e[2])
        if matrice[n][w] == round(matrice[n-1][w-int(e[1]*100)] + e[2], 2):
            elements_selection.append(e)
            w -= int(e[1]*100)
            #print('w', w)
        n -= 1

    return matrice[-1][-1], elements_selection


ele = open_csv()
#print(ele)
print('Algo dynamique', sacADos_dynamique(500, ele))

elem1 =[('Share-MOEX', 40.6, 16.69),
        ('Share-GBGY', 27.08, 34.09),
        ('Share-FJTI', 33.5, 20.81),
        ('Share-LGDP', 15.26, 3.4),
        ('Share-GEBJ', 5.87, 37.95)]

ele = [('Montre à gousset', 2.5, 6.2),
       ('Boule de bowling', 3.2, 10.5),
       ('Portrait de tata Germaine', 4, 12.5)]
#print('Algo dynamique', sacADos_dynamique(7, ele))
#print('Algo dynamique', sacADos_dynamique(50, elem1))


