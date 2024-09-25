from numpy import *

def norma_1(A):
    
    """
    Calcola la norma 1 di una matrice, ovvero la somma maggiore dei moduli degli elementi di una colonna.
    
    INPUT :
        - A : matrice
    OUPUT :
        - norma : la norma 1 della matrice A 
    """
    
    righe,colonne = A.shape
    
    norma = 0
    
    for i in range(0,colonne):
        
        # calcoliamo la somma dei moduli degli elementi della colonna i-esima 
        temp_sum = 0
        for j in range(0,righe):
            temp_sum += abs(A[j,i])

        if temp_sum > norma :
            norma = temp_sum

    return norma

A = array([[1,-6,5],
           [2,8,-3]])
print(A)
print("norma 1 : ", norma_1(A))

A = array([[1,2],
           [-3,-2],
           [-1,-3]])
print(A)
print("norma 1 : ", norma_1(A))