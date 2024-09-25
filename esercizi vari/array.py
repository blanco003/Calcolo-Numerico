import numpy as np

# trova il minimo e massimo di un array
def min_max(array):
    min = array[0]
    max = array[0]
    for i in range (len(array)):
        if array[i] > max:
            max = array[i]
        if array[i] < min:
            min = array[i]
    print("max : ",max)
    print("min : ",min)


# ricerca binaria (l'array deve essere gia ordinato)
def binary_search(array, element): 
    left = 0
    right = len(array) - 1
    while left <= right:
        mid = int((left + right)/2)
        if array[mid] == element:
            print("element found at index : ", mid)
            return
        elif array[mid] < element:
            left = mid + 1
        else:
            right = mid - 1
    print("element not found")


