
# Si scriva una funzione python che abbia 
# INPUT : 
    # A : matrice (rettangolare)
# OUPUT : 
    # v : media aritmetica degli elementi della matrice A
    # i,j : coordinate  di un elemento della matrice di A che più si avvicina alla media v
    
    
# Esempio :

# A : 
# 0 0 -1 0
# 3 3 -2 2
# 3 1 -1 -1 

# media = 7/12 (0.58)
# (i,j) ) (3,2)

from numpy import *

def f(A):
    righe, colonne = A.shape
    count = 0
    sum = 0
    
    # calcoliamo la media degli elementi della matrice
    
    for i in range (0,righe):
        for j in range (0,colonne):
            count = count + 1
            sum = sum + A[i,j]
            
    media = sum / count
    
    # troviamo le cordinate dell'elemento che si avvicina di piu alla media degli elementi della matrice
    r = 0
    c = 0
    for i in range (0,righe):
        for j in range (0,colonne):
            if ( abs(A[i,j]-media) < abs(A[r,c]-media)):
                r,c = i,j
    return media,r+1,c+1  # +1 perchè partono da 0 


A = array([[0,0,-1,0],[3,3,-2,2],[3,1,-1,-1]])
media,r,c = f(A)
print("\nMatrice in input \n\n", A)
print("\nMedia : ",media)
print("\nCordinate elemento che si avvicina di piu' alla media : (",r,",",c,")\n")