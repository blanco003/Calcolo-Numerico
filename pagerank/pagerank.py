import numpy as np

def pagerank(A, m=0.15):
    """ 
    Calcola il Pagerank di un web 
    INPUT: 
        A : Matrice di adiacenza
        m : parametro di compensazione della matrice di Google
    OUTPUT:
        x : vettore dei Pagerank
    """
    A = np.double(np.copy(A))
    [r, n] = A.shape
    
    for j in range(0, n):
        # Controllo la presenza di colonne nulle
        if np.sum(A[:, j]) == 0:
            A[:, j] = np.ones(shape=(n,))  # A[:, j] : j-esima colonna di A
            
        A[:, j] = A[:, j] / np.sum(A[:, j])
        
    E = np.ones(shape=(n, n))  # Matrice quadrata di dimensione n con elementi uguali a 1
    
    G = (1 - m) * A + m / n * E  # Compensazione della matrice di Google

    # Vettore iniziale della successione generata dal metodo delle potenze
    x0 = np.ones(shape=(n,)) / n

    _, x = potenze(G, x0)  # Metodo delle potenze implementato a parte
    
    return x

def potenze(A, y0, tol=1e-10, kmax=500):
    """
    Metodo delle potenze classico senza tecnica di normalizzazione

    Dati di input :
        - A : matrice quadrata che ammette autovalore dominante
        - y0 : vettore iniziale dell'iterazione
        - tol : precisione richiesta
        - kmax : numero max di iterazioni consentiti
    
    Dati di output :
        - sigma1 : autovalore dominante di A
        - z1 : autovettore corrispondente all'autovalore dominante
    """
    [m, n] = A.shape
    arresto = False
    k = 0  # contatore iterazioni
    z0 = y0
    sigma0 = 0

    while not arresto and k <= kmax: 
        k = k + 1
        z1 = np.dot(A, z0)  # prodotto matrice-vettore
        sigma1 = np.dot(z1, z0) / np.dot(z0, z0)  # stima dell'autovalore dominante
        
        Er = np.abs(sigma1 - sigma0) / np.abs(sigma1)  # errore relativo
        arresto = Er < tol
        
        z0 = z1
        sigma0 = sigma1

    if not arresto:
        print("Successione non convergente")

    return sigma1, z1


A = np.array([[0, 0, 1, 1], [1, 0, 0, 0], [1, 1, 0, 1], [1, 1, 0, 0]])
print("Matrice di adiacenza:")
print(A)
print("\nPagerank calcolato:")
print(pagerank(A, 0))
