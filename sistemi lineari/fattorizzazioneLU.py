from numpy import * 
import scipy
import scipy.linalg

def fattlu(A):

    """
    Fattorizza la matrice quadrata A in forma LU, con L matrice triangolare inferiore speciale ed U matrice triangolare superiore.

    INPUT
        A: matrice da fattorizzare
    OUTPUT
        L: matrice triangolare inferiore speciale
        U: matrice triangolare superiore    
    """
    
    righe, colonne =shape(A)
    
    # controlliamo la matrice sia quadrata
    if righe != colonne:
        print("matrice non quadrata")
        
    A=copy(A) 

    tol=1e-14
    L = identity(colonne)  
    
    for k in range(0,colonne-1):
    
        if abs(A[k,k])<tol:
            print("minore principale nullo")
            return
        
        # aggiorniamo gli elementi
        # lasciando invariati quelli delle prime k righe e quelli delle prime k-1 colonne al di sotto della diagonale principale
        # per comodità senza annullarli, alla fine estrarremo la matrice triangolare superiore di A
        
        for i in range(k+1,colonne): 
            mik=-A[i,k]/A[k,k]  # moltiplicatore di gauss
            
            for j in range(k+1,colonne):
                A[i,j]=A[i,j]+mik*A[k,j]
            L[i,k]=-mik
            
    U = triu(A) # estraiamo la parte triangolare superiore di A
    
    return L,U             


# esempio
A = array([ [2,1,0,-1],
            [-2,-2,1,-1],
            [4,2,-1,-1],
            [0,2,-3,2]])

print("A : \n",A)
L,U = fattlu(A)
print("\nL : \n",L)
print("\nU : \n",U)
print("\nL * U : \n",L.dot(U))
print("\nPer verifica A = A (LU) : ", allclose(A,dot(L,U)))



# scipy realizza la fattlu come : A = P L U , dovremmo riportarla nella nostra forma come P^T A = L U
Ppy,Lpy,Upy = scipy.linalg.lu(A)
print("\n\nP (modulo scipy): \n",Ppy)
print("\nL (modulo scipy): \n",Lpy)
print("\nU (modulo scipy): \n",Upy)
print("\nL * U (modulo scipy): \n",Ppy.dot(Lpy.dot(Upy)))

