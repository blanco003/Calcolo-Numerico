from numpy import *

def potenze(A,y0,tol=1e-10,kmax=500):
    """
    Metodo delle potenze con tecnica di normalizzazione (norma 2)

    Dati di input :
        - A : matrice quadrata che ammette autovalore dominante
        - y0 : vettore iniziale dell'iterazione
        - tol : precisione richiesta
        - kmax : numero max di iterazioni consentiti
    
    Dati di output :
        - sigma1 : autovalore dominante di A
        - z1 : autovettore corrispondente all'autovalore dominante

    """

    [m,n] = shape(A)
    arresto = False
    k = 0   # contatore iterazioni
    z0 = y0/linalg.norm(y0)   # normalizzazione
    sigma0 = 0

    while not(arresto) and k <= kmax : 
        k = k+1
        t1 = dot(A,z0)   # prodotto
        z1 = t1/linalg.norm(t1)
        sigma1 = sum(t1 * z0)
        Er = abs(sigma1-sigma0) / abs(sigma1)  # errore relativo
        arresto = (Er < tol)
        z0 = z1
        sigma0 = sigma1

    if not (arresto):
        print("successione non convergente")

    return sigma1, z1



A = array([[1, -1], 
           [2, 4]])

y0 = array([1, 1])

autovalore_dominante, autovettore = potenze(A, y0)

print("Autovalore dominante:", autovalore_dominante)
print("Autovettore dominante:", autovettore)