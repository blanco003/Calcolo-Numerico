from numpy import *

def scalini(A):
    
    """
    Riduce una matrice rettangolare A di dimensione m x n in forma a scalini, utilizzando l'algoritmo di eliminazione di gauss con tecnica del pivot
    (se viene trovato un pivot nullo si procede a cercare il primo elemento non nullo al di sotto del pivot e scambiare la riga corrente con quella 
    in cui e' stato trovato il nuovo pivot non nullo).

    INPUT :
        - A : matrice rettangolare di dimensione m x n da ridurre a scalini
    OUTPUT : 
        - A : matrice A ridotta in forma a scalini
    """
    
    righe, colonne = A.shape
    A = A.copy()    # per non sovrascrivere la matrice A in memoria
    
    r = 0  # indice per scorrere le righe
    c = 0  # indice per scorrere le colonne
    
    it = 0  # numero di iterazioni effettuate
    
    
    while(c < colonne) and (r < righe-1):
        
        it += 1
        print("\n-----------------------\nPasso : ",it)
        print(A)
        
        pivot = A[r,c]
        print("pivot corrente : ",pivot)
        
        
        if pivot == 0:
            
            print("pivot corrente nullo, cerchiamo uno nuovo al di sotto")
            pivot_non_nullo_trovato = False
            
            # cerchiamo un elemento non nullo nelle righe al di sotto della colonna del pivot nullo 
            for i in range(r+1,righe):
                
                # al primo elemento non nullo trovato possiamo fermarci e salvare l'indice della riga del nuovo pivot per scambiarlaa
                if A[i,c] != 0:
                    pivot = A[i,c]
                    riga_nuovo_pivot = i
                    pivot_non_nullo_trovato = True
                    break
            
            
            if pivot_non_nullo_trovato:

                # scambiamo la riga corrente con quella del nuovo pivot non nullotrovato
                
                print("nuovo pivot trovato : ",pivot, " in riga ", riga_nuovo_pivot+1)
                print("Scambio la riga ",r+1," con la riga ",riga_nuovo_pivot+1)
                
                temp_row = A[r].copy()  
                A[r] = A[riga_nuovo_pivot] 
                A[riga_nuovo_pivot] = temp_row
                
                print("Matrice aggiornata con righe scambiate :\n",A)
                
                
            else:
                
                # se tutti gli elementi al di sotto del pivot corrente nullo sono già nulli possiamo procedere spostandoci direttamente alla colonna successiva
                
                print("tutti gli elementi al di sotto erano gia nulli, procediamo con la colonna successiva")
                c = c +1
                
                continue  # saltiamo l'aggiornamento degli elementi
        
        
        # aggiorniamo gli elementi sotto al pivot
        for i in range(r + 1, righe):
            
            mik = -A[i, c] / pivot
            print(f"Moltiplicatore m{i+1}{c+1} = {mik}")
            
            for j in range(c, colonne):
                #print("Debug (", i + 1, j + 1, ") : ", A[i, j], "= ", A[i, j], " + ", mik, " * ", A[row, j])
                A[i, j] = A[i, j] + mik * A[r, j]
           
        r += 1
        c += 1
        
    
    print("\nMatrice ridotta a scalini : \n",A)
        
    return A


def rango_1(A):
    
    """
    Calcola il rango della matrice A, considerando che il rango di una matrice è dato dal numero di righe non nulle della matrice A.
    
    INPUT :
        - A : matrice rettangolare di dimensione m x n di cui calcolare il rango.
    OUTPUT : 
        - rango : rango della matrice A
    """
    
    A = scalini(A)  # prima di tutto riduciamo A a scalini
    rango = 0
    
    righe,colonne = A.shape
    
    for i in range(0,righe):
        
        # controlliamo se l'i-esima riga di A non è nulla, ovvero se contiene almeno un elemento diverso da 0
        riga_non_nulla = False
        
        for j in range(0,colonne):
            
            if A[i,j] != 0:
                riga_non_nulla = True
                break
        
        if riga_non_nulla:
            rango += 1
    
    return rango
        

def rango_2(A):
    
    """
    Calcola il rango della matrice A, considerando che il rango di una matrice è dato dal numero di colonne pivotali di A.
    
    INPUT :
        - A : matrice rettangolare di dimensione m x n di cui calcolare il rango.
    OUTPUT : 
        - rango : rango della matrice A.
    """
    
    A = scalini(A)  # prima di tutto riduciamo A a scalini
    rango = 0
    righe,colonne = A.shape
    
    i = 0  # indice per scorrere le righe di A
    j = 0  # indice per scorrere le colonne di A
    
    while (j < colonne) and (i < righe):
        
        if A[i,j] != 0:
            rango += 1
            #print(f"Debug : la colonna {j+1} e' pivotale")
            i += 1
            j += 1
        else : 
            # passiamo alla colonna successiva senza scendere di riga
            j += 1
    
    return rango
        

#esempi

A = array([[1,-1,-2],
           [0,0,-2],
           [2,-2,2],
           [-2,1,-3],
           [1,-2,-3]])

#print("\nMatrice ridotta a scalini : \n", scalini(A))
#print("\nRango di A : ", rango_1(A))
print("\nRango di A : ", rango_2(A))

B = array([ [0, 0, 0, 0, 1],
            [-1,2, 1, 3, 1],
            [1,-2, 1, -1, 1],
            [-1,2, 1, 3, 1],
            [1,-2, -1, -3, 1]])


#print("\nMatrice ridotta a scalini : \n", scalini(B))
#print("\nRango di B : ", rango_1(B))
print("\nRango di B : ", rango_2(B))

C = array([ [ 1,  0,  2, -2,  1],
            [-1,  0, -2,  1, -2],
            [-2, -2,  2, -3, -3]])

print("\nRango di C : ", rango_2(C))



