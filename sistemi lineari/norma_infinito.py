from numpy import * 

def norma_infinito(A):
    
    """
    Calcola la norma infinito della matrice rettangolare A, ovvero la somma maggiore dei moduli degli elementi di una riga.
    
    INPUT:
        - A : matrice di cui calcolare la norma infinito
    OUTPUT:
        - norma : norma infinito della matrice A
    """
    
    
    righe, colonne = A.shape
    norma = 0
    
    for i in range(0,righe):
        temp_somma = 0
        for j in range(0,colonne):
            temp_somma += abs(A[i,j])
        
        if temp_somma > norma:
            norma = temp_somma
    
    return norma

A = array([[1,-6,5],
           [2,8,-3]])
print(A)
print("norma infinito : ", norma_infinito(A))

A = array([[1,2],
           [-3,-2],
           [-1,-3]])
print(A)
print("norma infinito : ", norma_infinito(A))
