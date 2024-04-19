from numpy import * 
from scipy import *

def triang_sup(A,b):
    """
    Algoritmo di sostituzione all'indietro
    per la risoluzione dei sistemi lineari
    triangolari superiori
    
    --------------------------------------

    INPUT
    --------------------------------------
    A: matrice dei coefficienti triangolare superiore
    
    b: vettore dei termini noti
    
    OUTPUT
    --------------------------------------
    x: vettore soluzione del sistema Ax=b
    """

    [m,n]=shape(A)# oppure n=len(b)
    x=zeros(shape=(n,1))# preallochiamo la memoria per x
    tol=1e-15
    
    for i in range(n-1,-1,-1):
        if abs(A[i,i])<tol:
            raise ValueError('Matrice singolare')
        else:
            somma=0
            for j in range(i+1,n):
                somma=somma+A[i,j]*x[j]
            x[i]=(b[i]-somma)/A[i,i]
    return x
   