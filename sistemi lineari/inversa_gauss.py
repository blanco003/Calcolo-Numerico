from numpy import *

def inversa(A):
    
    """
    Restituisce l'inversa della matrice quadrata A ricevuta in input. 
    Solleva errore se la matrice A non è quadrata oppure se non ammette inversa (ovvero se è singolare, det(A) = 0)
    
    Per il calcolo dell'inversa si risolve il seguente sistema lineare : A * X = I
    
    INPUT:
        - A : matrice quadrata di cui calcolare l'inversa
    OUTPUT:
        - B : matrice inversa di A
    """
    
    righe,colonne = A.shape
    
    if righe != colonne:
        raise("Matrice non quadrata")
    
    # controlliamo se la matrice è singolare (det(A)=0), in questo caso per definizione non ammette inversa
    if determinante_laplace(A)==0:
        raise("Matrice singolare")
    
    I = identity(colonne)  # matrice identica
    
    # eseguiamo l'eliminazione di guass sulla matrice completa composta da quella dei coefficienti (A) e la matrice identica (I)
    matrice_completa = eliminazione_gauss_completa(A,I)
    
    # estraiamo dal risultato dell'eliminazione di gauss sulla matrice completa la matrice B
    B = zeros(shape=(colonne,colonne))
    
    for j in range(0,colonne):
        B[:,j] = matrice_completa[:,j+colonne]
        
    # estraiamo dal risultato dell'eliminazione di gauss sulla matrice completa la matrice A
    
    A = zeros(shape=(colonne,colonne))
    
    for j in range(0,colonne):
        A[:,j] = matrice_completa[:,j]
        
        
    print("\nA : \n",A)
    print("\nB : \n",B)
    
    A_1 = zeros(shape=(colonne,colonne))  # allochiamo la memoria per la soluzione, ovvero la matrice inversa di A
    
    # applichiamo la sostituzione all'indietro considerando la matrice A ed una colonna di B alla volta
    b = zeros(shape=(colonne,1))
    
    for j in range(0,colonne):  # per ogni colonna di B
        
        for i in range(0,colonne):  # per ogni riga di B
            b[i] = B[i,j]  
            
        #print(f"\nColonna {j+1} di b : \n {b}")
            
           
        xi = sostituzione_indietro(A,b).flatten() #flatten trasforma il risultato in array 1D
        #print(f"\nColonna {j+1} di A^-1 : \n {xi}")
       
        A_1[:,j] = xi
    
    return A_1


def eliminazione_gauss_completa(A,b):
    
    """
    Effettua l'eliminazione di gauss sulla matrice completa [A|b] composta dalla matrice dei coeffeicienti e quella dei termini noti.

    INPUT :
        - A : matrice rettangolare di dimensione m x n
        - b : matrice dei termini noti
    OUTPUT : 
        - matrice_completa : matrice risultato dell'eliminazione di gauss sulla matrice completa [A|b]
    """

    # creiamo la matrice completa
    matrice_completa = concatenate((A,b),axis=1,dtype=float)
    righe,colonne = matrice_completa.shape
    
    r = 0  # indice per scorrere le righe
    c = 0  # indice per scorrere le colonne
    it = 0  # contatore iterazioni
    
    while(c < colonne) and (r < righe-1):
        
        it += 1
        print("\n-----------------------\nPasso : ",it)
        print("\n",matrice_completa)
        
        pivot = matrice_completa[r,c]
        print("\nPivot corrente : ",pivot)
        
        
        if pivot == 0:
            
            print("pivot corrente nullo, cerchiamo un elemento non nullo nelle righe sottostanti")
            pivot_non_nullo_trovato = False
            
            # cerchiamo un elemento non nullo nelle righe al di sotto
            for i in range(r+1, righe):
                
                # ci fermiamo al primo elemento non nullo che incontriamo
                if matrice_completa[i,c] != 0:
                    pivot = A[i,c]
                    riga_nuovo_pivot = i
                    pivot_non_nullo_trovato = True
                    break
                
           
            if pivot_non_nullo_trovato:

                # scambiamo le righe
                print("Nuovo pivot trovato : ",pivot, " in riga ", riga_nuovo_pivot+1)
                print("Scambio la riga ",r+1," con la riga ",riga_nuovo_pivot+1)
                
                temp_row = matrice_completa[r].copy()  
                matrice_completa[r] = matrice_completa[riga_nuovo_pivot] 
                matrice_completa[riga_nuovo_pivot] = temp_row
                
                print("Matrice completa aggiornata con righe scambiate :\n",matrice_completa)
               
            else:
                
                 # se il pivot continua ad essere 0 (ovvero tutta la colonna e' gia' stata annullata) passiamo alla colonna successiva direttamente
                print("Tutti gli elementi al di sotto erano gia nulli, procediamo con la colonna successiva")
                c = c +1
                continue
        
        
        # aggiorniamo gli elementi della matrice al di sotto del pivot
        for i in range(r + 1, righe):
            
            mik = -matrice_completa[i, c] / pivot
            print(f"Moltiplicatore m{i+1}{c+1} = {mik}")
            
            for j in range(c, colonne):
                matrice_completa[i, j] = matrice_completa[i, j] + mik * matrice_completa[r, j]     
                
        r += 1
        c += 1
        
    print("\nFine eliminazione gauss : \n\n",matrice_completa)
    
    return matrice_completa



def determinante_laplace(A):
    
    """
    Regola di Laplace per il calcolo del determinante di una matrice quadrata.
    Solleva errore se la matrice non è quadrata.
    
    INPUT:
        A : matrice quadrata di cui calcolare il determinante
    OUTPUT:
        d : determinante della matrice A
    """
    
    righe,colonne = A.shape
    
    if righe != colonne:
        raise("La matrice non è quadrata")
    
    
    # Fissata la 1° riga
    
    if colonne == 1:
        d = A[0,0]  # ritorniamo il valore semplice dell'elemento
    else:
        d = 0
        for j in range(0,colonne):
            A1j = delete(delete(A,0,axis=0),j,axis=1)   # A1j è la sottomatrice di A ottenuta scartando la prima riga e la j-esima colonna
            d = d +(-1)**(j)*A[0,j]*determinante_laplace(A1j)   
            
    return d



def sostituzione_indietro(A,b):
    
    """
    Algoritmo di sostituzione all'indietro per la risoluzione dei sistemi lineari triangolari superiori della forma A x = b
    
    INPUT: 
        - A : matrice dei coefficienti triangolare superiore
        - b : vettore dei termini noti
    OUTPUT:
        - x : vettore soluzione del sistema A x =b
    """

    righe,colonne = A.shape
    x = zeros(shape=(colonne,1))  # allochiamo la memoria per il vettore che conterra' la soluzione del sistema
    tol = 1e-15  # tolleranza massima da usare nelle approssimazioni prima di approssimare il valore a 0
    
    for i in range(colonne-1,-1,-1):
        
        if abs(A[i,i])<tol:
            raise ValueError('Matrice singolare')
        
        else:
            somma=0
            for j in range(i+1,colonne):
                somma=somma+A[i,j]*x[j]
            x[i]=(b[i]-somma)/A[i,i]
    return x

    
# esempio

A = array([ [1,-1,0],
            [2,1,-1],
            [0,-2,1]])

A_1 = inversa(A)

print("\nA :\n",A)
print("\nA^(-1) : \n",A_1)
print("\nPer verifica A * A^(-1) = I : ", allclose(dot(A,A_1),identity(3)))   # allclose effettua il controllo di uguaglianza a meno di precisioni molto basse
    
    
    