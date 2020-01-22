import math
def jumpSearch(liste,value):

    n = len(liste)
    step = math.sqrt(n)

    prev = 0

    while liste[int(min(step,n)-1)] < value :
        prev = step
        step += math.sqrt(n)

        if prev >= n:
            return -1
    while liste[int(prev)] < value :
        prev += 1
        if prev == min(step,n):
            return -1
    if liste[int(prev)] == value :
        return int(prev)
    return -1

liste=[0,1,2,3,4,5,6,7,8,9,11,23,43,53,213];
a = jumpSearch(liste,43)

print(a)

