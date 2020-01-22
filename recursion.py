def factorial(n):
    if  n == 0:
        return 1
    else:
        return n*factorial(n-1)
print(factorial(1))

def summation(n):
    if n == 0:
        return 0
    else:
        return n+summation(n-1)
print(summation(5))

def example(n):
    if n == 3:
        return n
    else:
        return 2*example(n+1)


print(example(1))

def reverse_string(input):

    #base case
    if len(input) <= 1:
        return input
    #recursion
    else:
        return reverse_string(input[1:])+input[0]

print(reverse_string("Selam"))


def multiply(x,y):

    #base case
    if x == 0 :
        return 0
    #recursion
    else:
        return (y+multiply(x-1,y))

print(multiply(2,3))


def power(a,b):

    #base case
    if b == 0:
        return 1

    #recursion
    else:
        return (a*power(a,b-1))


print(power(2,3))



def linear_search(list,value):

    index = 0
    found = False

    while index < len(list) and found is not True :

        if list[index] == value :
            found = True
        else:
            index = index + 1
    if found == True:
        return str(index) + '. indexte'
    else:
        return 'Böyle bir sayı bulunamadı'
list=[123,231,4213,2423432,12333,832490,90,19]

print(linear_search(list,90))


def binary_search(list,value):
    if value < 0 or value > len(list):
        return 'Böyle bir sayi yok'
    else:
        index = len(list)//2
        if value == list[index]:

            return (index,value)
        elif value > list[index]:
             list =list[index:]
        elif value < list[index]:
            list= list[:index]

    return binary_search(list,value)

liste = range(1,11)
print(binary_search(liste,12))

