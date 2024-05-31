from numpy import *

def norma1(A):
    [m,n] = A.shape
    
    max = 0

    for i in range(n):
        sum = 0
        for j in range(m):
            sum += abs(A[j,i])

        if sum > max :
            max = sum

    return max

A = array([[1,-6,5],
           [2,8,-3]])
print(A)
print("norma 1 : ", norma1(A))

A = array([[1,2],
           [-3,-2],
           [-1,-3]])
print(A)
print("norma 1 : ", norma1(A))