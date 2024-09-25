from numpy import * 

def gauss_pivot_parziale(A):

    """
    Algoritmo di gauss con tecnica del massimo pivot parziale di una matrice con tecnica del massimo pivot parziale :
    consideriamo come elemento pivotale, quello massimo (in valore assoluto) della colonna considerata,
    se non coincide con l'elemento pivotale corrente scambiamo le 2 righe e proseguiamo l'eliiminazione.

    INPUT
        A: matrice da fattorizzare
    OUTPUT
        L: matrice triangolare inferiore speciale
        U: matrice triangolare superiore    
    """
    
    [m,n]=shape(A)
            
    A = copy(A) # altrimenti sovrascriviamo la A nella shell, copia completa di un oggetto anzichè copiare il riferimento
    tol = 1e-15
    L = identity(n)  
    
    for k in range(0,n-1):

        print("-------------------------------------------\nPasso : ",k)
        print(A)

        # consideriamo il modulo del pivot corrente e la sua riga per confrontarlo con tutti gli elementi sottostanti
        max_pivot_index = k
        max_pivot = abs(A[k,k])
        
        print(f"Pivot corrente : {max_pivot} , in riga {max_pivot_index+1}")


        # per tutte le righe al di sotto del pivot cerchiamo se esiste un elemento di modulo maggiore del pivot corrente
        for i in range(k+1,n):    
            
            if abs(A[i,k]) > max_pivot:
                # salviamo il pivot e il suo numero di riga
                max_pivot_index = i
                max_pivot = abs(A[i,k])

        print(f"Pivot corrente di modulo massimo trovato : {max_pivot} , in riga {max_pivot_index+1}")
    
    
        # se l'elemento di modulo maggiore non si trova nella riga corrente scambiamo le 2 righe
        
        if max_pivot_index > k:
            
            temp_row = A[k].copy()  
            A[k] = A[max_pivot_index] 
            A[max_pivot_index] = temp_row
            
            print("Scambiamo la  riga ",k+1," con la riga ",max_pivot_index+1)
            print("Matrice aggiornata : \n",A)


        if abs(A[k,k])<tol:
            raise("minore principale nullo")
        
        
        # aggiorniamo i restanti elementi
        for i in range(k+1,n-1):
            
            mik=-A[i,k]/A[k,k]
            print("moltiplicatore : m_",i,k,"= ",mik)
            for j in range(k+1,n-1):
                A[i,j]=A[i,j]+mik*A[k,j]
            L[i,k]=-mik
            
    U = triu(A) # estrae la parte triang. sup. di A
    return L,U             


# esempio
A = array([ [1,-2,3,1],
            [-1,2,1,0],
            [2,-1,-1,-1],
            [-6,-2,5,1]],dtype=float)
L,U = gauss_pivot_parziale(A)

print("A : \n",A)
print("L : \n",L)
print("U : \n",U)

