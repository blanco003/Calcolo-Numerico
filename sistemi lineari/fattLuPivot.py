from numpy import * 

def fattlu(A):
    
    """
    Fattorizzazione LU di una matrice con tecnica del pivot :
        se l'elemento pivotale corrente risulta nullo, scambiamo la riga con la prima riga successiva con elemento pivotale non nullo

        lavorando con matrici non singolari (det(A) != 0) , se l'elemento pivotale a_kk = 0 , è possibile dimostrare che esiste certamente
        un elemento non nullo nella colonna k-esima al di sotto di a_kk
    
    sintassi: [L,U] = fattlu(A)

    INPUT
        A: matrice da fattorizzare
    OUTPUT
        L: matrice triangolare inferiore speciale
        U: matrice triangolare superiore    
    """
    
    [m,n]=shape(A)
    
    # TODO : ASSICURATI DET(A) SIA != 0


    A=copy(A) # altrimenti sovrascriviamo la A nella shell, copia completa di un oggetto anzichè copiare il riferimento
    L=identity(n)  
    
    for k in range(0,n-1):

        print("-------------------------------------------\n","passo : ",k)
        # print(A)
        
        print("current pivot : ",A[k,k])

        # se l'elemento pivotale è nullo cerchiamo una riga sottostante in cui l'elemento non è nullo
        if A[k,k]==0: 

            # trovo l'indice di riga in cui l'elemento pivotale non è nullo
            index_pivot_not_null = -1

            for i in range(k+1,min(n,m)):   
                if(A[i,k]!=0):
                    index_pivot_not_null = i
                    print("new pivot not null founded : ",A[index_pivot_not_null,k])
                    
            
            # scambio le 2 righe
            print("----------------------------------\n----------\n",A[k])
            print("----------------------------------\n----------\n",A[index_pivot_not_null])
            temp_row = A[k].copy()  
            A[k] = A[index_pivot_not_null] 
            A[index_pivot_not_null] = temp_row

            print("scambiata riga ",k," con riga ",index_pivot_not_null)
            print(A)
        
        for i in range(k+1,n-1):
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


# esempio
B = array([ [1,-2,3,1],
            [-1,2,1,0],
            [2,-1,-1,-1]])


L,U = fattlu(B)
print("B : \n",B)
print("L : \n",L)
print("U : \n",U)