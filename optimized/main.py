import csv


def open_csv():
    with open('../data/dataset1_Python+P7.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        data = []


        for row in csv_reader:
            if line_count != 0:
                if row[1] != '0.0' and '-' not in row[1] and row[2] != '0.0':
                    taux = round((float(row[1]) * float(row[2])), 2) *100
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
    print(len(elements_selection))
    return matrice[-1][-1], elements_selection


ele = open_csv()
test1, test2 = sacADos_dynamique(500, ele) 
euro = 0
benefice = 0
for i in test2:
    print('Name: ', i[0], ' Pice: ', i[1], ' Profit ', i[3])
    euro += round(i[1], 2)
    benefice += i[3]
print(euro)
print(benefice)
