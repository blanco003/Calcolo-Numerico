from numpy import * 

def determinante_laplace(A):
    
    """
    Regola di Laplace per il calcolo del determinante di una matrice quadrata.
    Solleva errore se la matrice non è quadrata.
    
    INPUT:
        A : matrice quadrata di cui calcolare il determinante
    OUTPUT:
        d : determinante della matrice A
    """
    
    m,n = shape(A)
    
    if m != n:
        raise("La matrice non è quadrata")
    
    
    # Fissata la 1° riga
    
    if n==1:
        d = A[0,0]  # ritorniamo il valore semplice dell'elemento
    else:
        d = 0
        for j in range(0,n):
            A1j = delete(delete(A,0,axis=0),j,axis=1)   # A1j è la sottomatrice di A ottenuta scartando la prima riga e la j-esima colonna
            d = d +(-1)**(j)*A[0,j]*determinante_laplace(A1j)   
            
    return d

# esempio
A = array([ [1,0,-2], [-1,0,1], [1,1,-3]])
print("A : \n",A)
print("\nDeterminante di A : ",determinante_laplace(A))
