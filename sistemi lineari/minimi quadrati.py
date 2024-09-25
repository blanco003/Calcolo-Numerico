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
        #print("pivot corrente : ",pivot)
        
        
        if pivot == 0:
            
            #print("pivot corrente nullo, cerchiamo uno nuovo al di sotto")
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
                
                #print("nuovo pivot trovato : ",pivot, " in riga ", riga_nuovo_pivot+1)
                #print("Scambio la riga ",r+1," con la riga ",riga_nuovo_pivot+1)
                
                temp_row = A[r].copy()  
                A[r] = A[riga_nuovo_pivot] 
                A[riga_nuovo_pivot] = temp_row
                
                #print("Matrice aggiornata con righe scambiate :\n",A)
                
                
            else:
                
                # se tutti gli elementi al di sotto del pivot corrente nullo sono già nulli possiamo procedere spostandoci direttamente alla colonna successiva
                
                #print("tutti gli elementi al di sotto erano gia nulli, procediamo con la colonna successiva")
                c = c +1
                
                continue  # saltiamo l'aggiornamento degli elementi
        
        
        # aggiorniamo gli elementi sotto al pivot
        for i in range(r + 1, righe):
            
            mik = -A[i, c] / pivot
            #print(f"Moltiplicatore m{i+1}{c+1} = {mik}")
            
            for j in range(c, colonne):
                #print("Debug (", i + 1, j + 1, ") : ", A[i, j], "= ", A[i, j], " + ", mik, " * ", A[row, j])
                A[i, j] = A[i, j] + mik * A[r, j]
           
        r += 1
        c += 1
        
    
    print("\nMatrice ridotta a scalini : \n",A)
        
    return A


def rango(A):

    """
    Calcola il rango di A, considerando che il rango di una matrice è uguale al numero di righe non nulle.
    
    INPUT:
        - A : matrice di cui calcolare il rango
    OUTPUT:
        - rango : rango della matrice A
    """
    
    print("Riduciamo prima di tutto A in forma a scalini")
    A = scalini(A)  
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



def risolvi_sistema(A,b):

    """
    Risolve il sistema lineare A x = b
    
    INPUT:
        - A : matrice dei coefficienti
        - b : vettore dei termini noti
    OUTPUT:
        - x : soluzione del sistema lineare A x = b
    """
    
    A,b = eliminazione_gauss(A,b)
    x = sostituzione_indietro(A,b)

    return x
    
    
    
def eliminazione_gauss(A, b):

    """
    Effettua l'eliminazione di gauss sulla matrice A e ripete le operazioni sul vettore colonna dei termini noti b.

    INPUT :
        - A : matrice rettangolare di dimensione m x n
        - b : vettore colonna dei termini noti 
    OUTPUT : 
        - A : matrice triangolare superiore
        - b : vettore dei termini noti
    """

    righe,colonne  = A.shape

    A = A.copy()
    b = b.copy()

    r = 0  # indice per scorrere le righe
    c = 0 # indice per scorrere le colonne
    it = 0 # contatore iterazioni effettuate
    
    tolleranza=1e-16
    
    while (c < colonne) and (r < righe - 1):

        it += 1
        print("\n-----------------------\nPasso : ", it)
        print("\n", A)
        print("\n", b)
        
        pivot = A[r, c]
        #print("\npivot corrente : ", pivot)
        
        if abs(pivot) < tolleranza:  # Se il pivot è minore della tolleranza, consideralo nullo
            #print(f"pivot corrente nullo (|pivot| < {tolleranza}), cerchiamo uno nuovo al di sotto")
            pivot_non_nullo_trovato = False
            
            # Cerchiamo un elemento non nullo nelle righe al di sotto
            for i in range(r + 1, righe):
                if abs(A[i, c]) >= tolleranza:  # Solo pivot con modulo maggiore della tolleranza
                    pivot = A[i, c]
                    riga_nuovo_pivot = i
                    pivot_non_nullo_trovato = True
                    break
                
            if pivot_non_nullo_trovato:
                # Scambiamo le righe
                #print("nuovo pivot trovato : ", pivot, " in riga ", riga_nuovo_pivot + 1)
                #print("Scambio la riga ", row + 1, " con la riga ", riga_nuovo_pivot + 1)
                A[[r, riga_nuovo_pivot]] = A[[riga_nuovo_pivot, r]]  # Scambio diretto con NumPy
                b[[r, riga_nuovo_pivot]] = b[[riga_nuovo_pivot, r]]  # Scambio nel vettore b
            else:
                #print(f"tutti gli elementi al di sotto erano già nulli (|valore| < {tolleranza}), procediamo con la colonna successiva")
                c += 1
                continue
        
        # Aggiorniamo gli elementi della matrice A al di sotto del pivot
        for i in range(r + 1, righe):
            mik = -A[i, c] / pivot
            #print(f"Moltiplicatore m{i + 1}{col + 1} = {mik}")
            
            for j in range(c, colonne):
                A[i, j] = A[i, j] + mik * A[r, j]
                # Applica la tolleranza
                if abs(A[i, j]) < tolleranza:
                    A[i, j] = 0.0  # Approssimiamo a 0 se il valore è minore della tolleranza
            
            # Aggiorniamo il vettore b
            b[i] = b[i] + mik * b[r]
            if abs(b[i]) < tolleranza:
                b[i] = 0.0  # Approssimiamo a 0 se il valore è minore della tolleranza
                
        r += 1
        c += 1
        
    print("\nFine eliminazione gauss : \n\n", A, "\n\n", b, "\n")
    
    return A, b

    
def sostituzione_indietro(A, b):

    """
    Algoritmo di sostituzione all'indietro per la risoluzione dei sistemi triangolari superiori della forma A x = b.
    
    INPUT: 
        - A : matrice dei coefficienti triangolare superiore
        - b : vettore dei termini noti
    OUTPUT:
        - x : vettore soluzione del sistema A x = b
    """

    righe, colonne = A.shape
    x = zeros(shape=(colonne, 1))  # Allocazione della memoria per il vettore soluzione
    
    tolleranza = 1e-16
    
    for i in range(colonne-1, -1, -1):
        somma = 0
        for j in range(i+1, colonne):
            somma += A[i, j] * x[j]
        
        # Calcola il valore di x[i]
        x[i] = (b[i] - somma) / A[i, i]
        
        # Applica la tolleranza: se x[i] è minore di tolleranza, approssimiamo a zero
        if abs(x[i]) < tolleranza:
            x[i] = 0.0
    
    return x

            

def minimi_quadrati(A,b):

    """
    Risolve il problema dei minimi quadrati associato al sistema lineare nel caso in cui è possibile eseguire la via breve,
    ovvero quando il problema ammette soluzione unica (il rango della matrice A è massimo).
        
    INPUT : 
        - A : matrice dei coefficienti
        - b : vettore dei termini noti
    OUTPUT :
        - x : soluzione del problema dei minimi quadrati
    """
    
    # prima di tutto controlliamo se rango della matrice dei coefficienti A è massimo, in tal caso il problema ammette soluzione unica x
    righe_A, colonne_A = A.shape
    
    print("Calcoliamo il rango di A : ")
    rango_A = rango(A)
    
    if colonne_A == rango_A:
        
        print(f"Il rango di A e'  {rango_A} , dunque e' massimo e possiamo procedere con la via breve")
        
        A_T = transpose(A)
        A_T_A = dot(A_T,A)
        A_T_b = dot(A_T,b)
    
        print("Soluzione : \n",risolvi_sistema(A_T_A,A_T_b))
    
    else :
        print("Il rango di A non e' massimo dunque la soluzione non e' unica, devi procedere con la strada classica")
        
    
    
# ESEMPIO

A = array([[-1 , 0 , -2],
           [ 2 , 1 ,  2],
           [-1 , 0 , -2],
           [ 2 , 1 ,  1],
           [ 3 , 1 ,  3],],dtype=float)

b = array([1, 1, 1, 1, 1],dtype=float)

minimi_quadrati(A,b)
