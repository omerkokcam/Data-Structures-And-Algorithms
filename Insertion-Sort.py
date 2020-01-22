def insertion(liste):

    for i in range(1, len(liste)):

        value = liste[i]
        position = i

        while position > 0 and liste[position-1] > value :
            liste[position] = liste[position-1]
            position -= 1

            liste[position] = value
    return liste


liste = [3, 2, 13, 4, 6, 5, 7, 8, 1, 20]

insertion(liste)
print(liste)