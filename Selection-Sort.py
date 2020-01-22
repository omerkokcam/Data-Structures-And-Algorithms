def selection(liste):

    for i in range (len(liste)-1,0,-1):
        positionOfMax = 0
        for location in range(1, i+1):
            if liste[location] > liste[positionOfMax]:
                positionOfMax = location

        liste[positionOfMax], liste[i] = liste[i],liste[positionOfMax]

    return liste




liste = [3, 2, 13, 4, 6, 5, 7, 8, 1, -1, 20]
selection(liste)

print(liste)