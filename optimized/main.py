import csv


def open_csv():
    with open('../data/dataset1.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0

        for row in csv_reader:
            if line_count != 0:
                if row[1] != 0.0 and '-' not in row[1]:
                    name = row[0]
                    price = row[1]
                    profit = row[2]
            line_count += 1
        return line_count


def sacADos_dynamique(capacite, elements):

    matrice = [[0 for x in range(capacite + 1)] for x in range(len(elements) + 1)]

    for i in range(1, len(elements) + 1):
        for w in range(1, capacite + 1):

            if elements[i-1][1] <= w:

                matrice[i][w] = max(elements[i-1][2] + matrice[i-1][w-elements[i-1][1]], matrice[i-1][w])
            else:
                matrice[i][w] = matrice[i-1][w]
            print(matrice)


    w = capacite
    n = len(elements)
    elements_selection = []

    while w >= 0 and n >= 0:
        e = elements[n-1]
        print(matrice[n][w])
        if matrice[n][w] == matrice[n-1][w-e[1]] + e[2]:
            elements_selection.append(e)
            w -= e[1]

        n -= 1

    return matrice[-1][-1], elements_selection

#ele = open_csv()
#print(ele)
#print('Algo dynamique', sacADos_dynamique(500, ele))


ele = [('Montre à gousset', 2, 6),
       ('Boule de bowling', 3, 10.5),
       ('Portrait de tata Germaine', 4, 12)]
print('Algo dynamique', sacADos_dynamique(5, ele))
