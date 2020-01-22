def mergeSort(liste):

    if len(liste)>1 :
        mid = len(liste)//2

        left_half = liste[:mid]
        right_half = liste[mid:]


        mergeSort(left_half)
        mergeSort(right_half)
        i = 0
        j = 0
        k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                liste[k] = left_half[i]
                i += 1
            else:
                liste[k] = right_half[j]
                j += 1
            k += 1

        while  i < len(left_half) :
            liste[k] = left_half[i]
            i+=1
            k+=1
        while j < len(right_half):
            liste[k] = right_half[j]
            j += 1
            k += 1
    return liste



liste = [3,2,12,34,23,44,23,42]
mergeSort(liste)
print(liste)