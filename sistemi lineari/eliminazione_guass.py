import numpy as np

def eliminazione_gauss(A,b):

    """
        Eliminazione di Guass per risolvere sistemi lineari 
        
        Dati di input : 
            - A : matrice dei coefficienti (quadrata)
            - b : vettore dei termini noti
        Dati di output : 
            - x : vettore soluzioni
    """
    
    [righe_A,colonne_A] = np.shape(A)
    [righe_b,colonne_b] = np.shape(b)


    if righe_A != colonne_A : 
        print("Errore : Matrice dei coefficienti non quadrata")
        return
    
    if (colonne_b > 1) or (righe_b != righe_A) :
        print("Errore : vettore termini noti di dimensioni non corrette")
        return
    
    

    # creiamo la matrice completa
    matrice_completa = np.concatenate((A,b),axis=1,dtype=float)
    print(f" \n ------------------------------------------------\n[A|b]  :\n\n{matrice_completa}")
    print("\n ------------------------------------------------")

    # inizializziamo il vettore delle soluzioni
    x = np.zeros(righe_b)

    i = 0
    j = i - 1


    # eliminazione di gauss

    while i < righe_A:

        if matrice_completa[i][i] == 0.0:
            print("Errore : Divisione per 0")
            return
        
        for j in range(i+1,righe_b):
            m_ik = matrice_completa[j][i] / matrice_completa[i][i]
            matrice_completa[j] = matrice_completa[j] - (m_ik * matrice_completa[i])
            print(f" \n ------------------------------------------------\n[A{i+1}|b{i+1}]  :\n\n{matrice_completa}")
            print("\n ------------------------------------------------")

        i = i + 1
    


    # algoritmo di sostituzione all'indietro
    x[righe_b-1] = matrice_completa[righe_b-1][righe_b] / matrice_completa[righe_b-1][righe_b-1]    # l'ultima incognita è sempre istantanea da trovare

    for k in range(righe_b-2, -1, -1):
        x[k] = matrice_completa[k][righe_b]

        for j in range(k+1, righe_b):
            x[k] = x[k] / matrice_completa[k][k]
    


    # stampa della soluzione
    
    print("\nSoluzioni del sistema : ")
    for i in range(0,len(x)):
        print(f"x{i} = {x[i]}")
    print("\n")



    
A = np.array([[1,1,3],
              [0,1,3],
              [-1,3,0]])

b = np.array([[1],[3],[5]])
    
eliminazione_gauss(A,b)
