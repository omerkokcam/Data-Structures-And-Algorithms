def bubbleSort(liste):
    n = len(liste)-1

    for i in range(0,n):
        for j in range (n-i) :
            if liste[j]>liste[j+1] :
                (liste[j],liste[j+1]) = (liste[j+1],liste[j]) #python is the best :)
                # or you can do this method
                # temp = liste[j]
                # liste[j] = liste[j+1]
                # liste[j+1] = temp


liste = [15,2,90,4,6,3,5,17,11,23,1,7]

bubbleSort(liste)
print(liste)