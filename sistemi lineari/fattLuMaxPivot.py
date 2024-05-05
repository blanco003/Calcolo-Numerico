from numpy import * 

def fattlu(A):

    """
    Fattorizzazione LU di una matrice con tecnica del massimo pivot parziale :
        consideriamo come elemento pivotale, quello massimo (in valore assoluto) della colonna considerata,
        se non coincide con l'elemento pivotale corrente scambiamo le 2 righe e preoseguiamo
    
    sintassi: [L,U] = fattlu(A)

    INPUT
        A: matrice da fattorizzare
    OUTPUT
        L: matrice triangolare inferiore speciale
        U: matrice triangolare superiore    
    """
    
    [m,n]=shape(A)
            
    A=copy(A) # altrimenti sovrascriviamo la A nella shell, copia completa di un oggetto anzichè copiare il riferimento
    tol=1e-15
    L=identity(n)  
    
    for k in range(0,n-1):

        print("-------------------------------------------\n","passo : ",k)
        # print(A)

        # scambiamo la riga con quella con il massimo pivot
        max_pivot_index = k
        max_pivot = abs(A[k,k])

        for i in range(k+1,min(n, m)):    # min(n,m) serve nel caso la matrice non sia quadrata, altrimenti è uguale n o m
            if abs(A[i,k]) > max_pivot:
                max_pivot_index = i
                max_pivot = abs(A[i,k])

        print("current pivot : ",A[k,k])
        print("max pivot founderd: ",A[max_pivot_index,k])
    
        # se il max non si trova nella riga corrente scambiamo le 2 righe
        if max_pivot_index > k:
            temp_row = A[k].copy()  
            A[k] = A[max_pivot_index] 
            A[max_pivot_index] = temp_row
            print("scambiata riga ",k," con riga ",max_pivot_index)
            print(A)


        if abs(A[k,k])<tol:
            print("minore principale nullo")
            return None, None
        
        for i in range(k+1,min(n, m)):
            mik=-A[i,k]/A[k,k]
            print("moltiplicatore : m_",i,k,"= ",mik)
            for j in range(k+1,n):
                A[i,j]=A[i,j]+mik*A[k,j]
            L[i,k]=-mik
            
    U = triu(A) # estrae la parte triang. sup. di A
    return L,U             


# esempio
A = array([ [1,-2,3,1],
            [-1,2,1,0],
            [2,-1,-1,-1]])


L,U = fattlu(A)
print("A : \n",A)
print("L : \n",L)
print("U : \n",U)
