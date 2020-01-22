def linearSearchWithUnorderedList(liste,value):
    index = 0
    found = False


    while index < len(liste) and not found:
        if liste[index] == value:
            found = True
        else:
            index += 1
    return (found, index)

liste = [5, 7, 2, 3, 15, 8, 100, 12]
a = linearSearchWithUnorderedList(liste, 8)
print(a)
