def binarySearch(liste,value):

    first_index = 0
    last_index = len(liste) - 1

    found = False


    while first_index <= last_index and not found:

        middle_index = (first_index + last_index) // 2

        if liste[middle_index] == value:
            found = True
        else:
            #sol taraf
            if value < liste[middle_index]:
                last_index = middle_index - 1
            else:
                first_index = middle_index + 1
    return found



liste = [3,6,11,18,21,34]
a = binarySearch(liste,11)
print(a)
b = binarySearch(liste,33)
print(b)