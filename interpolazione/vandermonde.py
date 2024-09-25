from numpy import *
def matrice_vandermonde(x):

    """
    Restituisce la matrice di Vandermonde dato vettore di input x.

    INPUT:
        - x : vettore di input
    OUTPUT:
        - V : matrice di Vandermonde
    """

    n = len(x)

    V = zeros((n, n))  # inizializziamo una matrice vuota (soli 0) che sarà la matrice di Vandermonde

    for i in range(0,n):
        for j in range(0,n):
            V[i, j] = x[i] ** (n - j - 1)  

    return V


def polinomio_interpolante(x, y):

    """
    Calcola i coefficienti del polinomio interpolante dato il vettore delle ascisse x ed il vettore delle ordinate y,
    rappresentanti i punti (x,y) da interpolare.

    INPUT:
        - x : vettore delle ascisse
        - y : vettore delle ordinate

    OUPUT:
        - a : vettore dei coefficienti del polinomio interpolante
    """

    V = matrice_vandermonde(x)
    
    # per determinare i coefficienti del polinomio interpolante abbiamo bisogno di risolvere il sistema lineare V a = y

    a = risolvi_sistema(V,y)
    
    return a



def risolvi_sistema(A,b):
    
    """
    Risolve il sistema lineare della forma A x = b , di m equazioni in n incognite.
    L'algoritmo applica inizialmente l'eliminazione di gauss alle matrici A ed al vettore colonna b, successivamente applica l'algoritmo 
    di sostituzione all'indietro per ricavare il vettore delle incognite x.
    
    INPUT: 
        - A : matrice rettangolare di dimensione m x n
        - b : vettore colonna dei termini noti
    OUTPUT :
        - x : soluzione del sistema lineare A x = b
    """
    
    A,b = eliminazione_gauss(A,b)
    x = sostituzione_indietro(A,b)

    return x


def eliminazione_gauss(A,b):
    
    """
    Effettua l'eliminazione di gauss sulla matrice A e ripete le operazioni sul vettore colonna dei termini noti b.

    INPUT :
        - A : matrice rettangolare di dimensione m x n
        - b : vettore colonna dei termini noti 
    OUTPUT : 
        - A : matrice triangolare superiore
        - b : vettore dei termini noti
    """
    
    [m,n] = A.shape
    A = A.copy()
    b = b.copy()
    row = 0
    col = 0
    it = 0 
    
    while(col<n) and (row<m-1):
        
        it += 1
        print("\n-----------------------\nPasso : ",it)
        print("\n",A)
        print("\n",b)
        
        pivot = A[row,col]
        print("\npivot corrente : ",pivot)
        
        if pivot == 0:
            
            print("pivot corrente nullo, cerchiamo uno nuovo al di sotto")
            pivot_non_nullo_trovato = False
            
            # cerchiamo un elemento non nullo nelle righe al di sotto
            for i in range(row+1,m):
                if A[i,col] != 0:
                    pivot = A[i,col]
                    riga_nuovo_pivot = i
                    pivot_non_nullo_trovato = True
                    break
                
           
            if pivot_non_nullo_trovato:

                # scambiamo le righe
                print("nuovo pivot trovato : ",pivot, " in riga ", riga_nuovo_pivot+1)
                print("Scambio la riga ",row+1," con la riga ",riga_nuovo_pivot+1)
                temp_row = A[row].copy()  
                A[row] = A[riga_nuovo_pivot] 
                A[riga_nuovo_pivot] = temp_row
                print("Matrice A aggiornata con righe scambiate :\n",A)
                
                # effettuiamo il medesimo scambio sul vettore dei termini noti
                temp_elem = b[row]
                b[row] = b[riga_nuovo_pivot]
                b[riga_nuovo_pivot] = temp_elem
                print("Vettore b aggiornato con righe scambiate :\n",b)
                
                
            else:
                
                 # se il pivot continua ad essere 0 (ovvero tutta la colonna e' gia' stata annullata) passiamo alla colonna successiva direttamente
                print("tutti gli elementi al di sotto erano gia nulli, procediamo con la colonna successiva")
                col = col +1
                continue
        
        # aggiorniamo gli elementi della matrice A al di sotto del pivot
        for i in range(row + 1, m):
            mik = -A[i, col] / pivot
            print(f"Moltiplicatore m{i+1}{col+1} = {mik}")
            
            for j in range(col, n):
                #print("Debug (", i + 1, j + 1, ") : ", A[i, j], "= ", A[i, j], " + ", mik, " * ", A[row, j])
                A[i, j] = A[i, j] + mik * A[row, j]
           
            # Aggiorniamo il vettore b
            b[i] = b[i] + mik * b[row]
            #print(f"Debut b[{i + 1}] = {b[i]}")
                
                
        row += 1
        col += 1
        
    print("\nFine eliminazione gauss : \n\n",A,"\n\n",b,"\n")
    
    return A,b

    
def sostituzione_indietro(A,b):
    
    """
    Algoritmo di sostituzione all'indietro per la risoluzione dei sistemi lineari triangolari superiori.

    INPUT:
        - A: matrice dei coefficienti triangolare superiore
        - b: vettore dei termini noti
    OUTPUT:
        - x: vettore soluzione del sistema A x = b
    """

    [m,n]=shape(A)
    x = zeros(shape=(n,1))  # allochiamo la memoria per il nuovo vettore che conterra' la soluzione del sistema
 
    for i in range(n-1,-1,-1):
        somma=0
        for j in range(i+1,n):
            somma=somma+A[i,j]*x[j]
        x[i]=(b[i]-somma)/A[i,i]
    return x


# esempio

x = array([1, 2, 3])
y = array([1, 4, 9]) 

a = polinomio_interpolante(x, y)
print("\nCoefficienti del polinomio interpolante : \n", a)
