# Si scriva una funzione Python che abbia
# INPUT : 
    # A : matrice (rettangolare)
# OUPUT : 
    # norma : norma infinito della matrice A (somma massima dei moduli degli elementi di una riga della matrice)
    
from numpy import *

def norma_infinito(A):
    righe, colonne = A.shape
    somma_max = 0
    
    for i in range(0,righe):
        temp_somma = 0
        for j in range(0,colonne):
            temp_somma += abs(A[i,j])
            
        if temp_somma > somma_max:
            somma_max = temp_somma
    
    return somma_max
            
            
A = array([[1,-6,5], [2,8,3]])
print(A)
print(norma_infinito(A))

B = array([[1,2], [-3,-2], [-1,-3]])
print(B)
print(norma_infinito(B))
        