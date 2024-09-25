from numpy import *

def sostituzione_indietro(A,b):
    
    """
    Algoritmo di sostituzione all'indietro per la risoluzione dei sistemi triangolari superiori della forma A x = b.
    
    INPUT: 
        - A : matrice dei coefficienti triangolare superiore
        - b : vettore dei termini noti
    OUTPUT:
        - x : vettore soluzione del sistema A x = b
    """

    righe, colonne = A.shape  
    
    # righe = numero di equazioni, colonne = numero di incognite
    
    x = zeros(shape=(colonne,1))# preallochiamo la memoria per un vettore rappresentantela soluzione del sistema
    
    tol = 1e-15  # tolleranza massima prima di approssimare il valore a 0
    
    for i in range(colonne-1,-1,-1):
        
        if abs(A[i,i]) < tol:
            raise ValueError('Matrice singolare')
        else:
            somma=0
            for j in range(i+1,colonne):
                somma=somma+A[i,j]*x[j]
            x[i]=(b[i]-somma)/A[i,i]
    return x
   
   
# esempio

A = array([[1,  -1, -2, -2, -3],
           [0,  -1, -7, -4 , -7],
           [0,  0,  6, 5 , 6],
           [0,  0,  0,  14/3 , 5],
           [0,0,0,0, 55/14]])

b = array([1,3,-2,1/3,-43/14])

print("\nMatrice dei coefficienti : \n",A)
print("\nVettore dei termini noti : \n",b)
print("\nSoluzione del sistema A x = b  : \n",sostituzione_indietro(A,b))