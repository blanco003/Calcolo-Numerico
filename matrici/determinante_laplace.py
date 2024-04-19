from numpy import * 

def laplace(A):
    """
    Regola di Laplace per il calcolo del determinante di una matrice quadrata.
    Sviluppo di Laplace lungo la prima riga
    """
    
    [m,n]=shape(A)
    if n==1:
        d=A[0,0]
    else:
        d=0
        for j in range(0,n):
            A1j=delete(A,0,axis=0)
            A1j=delete(A1j,j,axis=1)
            d=d+(-1)**(j)*A[0,j]*laplace(A1j)
    return d