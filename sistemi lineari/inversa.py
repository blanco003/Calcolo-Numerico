from numpy import *


def inversa(A):
    
    """
    Restituisce l'inversa della matrice quadrata A ricevuta in input. 
    Solleva errore se la matrice A non è quadrata oppure se A non ammette inversa (ovvero se è singolare, det(A) = 0)
    
    Per il calcolo dell'inversa si utilizza la seguente formula :  A^(-1) = 1/det(A) * agg(A)
    
    INPUT:
        - A : matrice quadrata di cui calcolare l'inversa
    OUTPUT:
        - B : matrice inversa di A
    """
    
    m,n = A.shape
    
    if m != n:
        raise("Matrice A non quadrata")
    
    A = A.copy()  # per non modificare la matrice A in memoria
    
    detA = determinante_laplace(A)  # sfruttiamo la funzione det di scipy.linalg per il calcolo del determinante di A
    
    print(f"Determinante di A : {detA}")
    
    
    # se il determinante di A è uguale a 0 la matrice e' singolare e dunque non ammette inversa
    if detA == 0:
        raise("Matrice A singolare")
    
    
    aggA = zeros(shape=(n,n)) # allochiamo la memoria per la matrice dei complementi algebrici
    
    # calcoliamo i coefficienti algebrici di tutte le sottomatrici di A ottenute senza considerare la i-esima riga e j-esima colonna
    for i in range(0,n):
        for j in range(0,n):
            aggA[i,j] =  (-1)**(i+j) * determinante_laplace(delete(delete(A,i,axis=0),j,axis=1))
            
            
    print(f"\nMatrice dei complementi : \n{aggA}")
    
    
    aggA = transpose(aggA)  # aggA è la matrice trasposta della matrice dei complementi algebrici
    
    print(f"\nMatrice dei complementi trasposta: \n{aggA}")
    
    A_1 = (1/detA) * aggA   # costruiamo la matrice inversa
    
    print("\nPer verifica A * A^(-1) = I ? : \n",dot(A,A_1))
    
    return A_1


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
print("\nInversa : \n",inversa(A))