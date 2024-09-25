from numpy import *

def potenze(A, y0, tol, it_max):
    
    """
    Metodo delle potenze classico senza tecnica di normalizzazione

    INPUT:
        - A : matrice quadrata che ammette autovalore dominante
        - y0 : vettore iniziale dell'iterazione
        - tol : precisione richiesta
        - it_max : numero max di iterazioni consentiti
    
    OUTPUT:
        - sigma1 : autovalore dominante di A
        - z1 : autovettore corrispondente all'autovalore dominante
        - it : numero di iterazioni eseguite
    """
    
    arresto = False
    it = 0  # contatore iterazioni
    
    z0 = y0  
    sigma0 = 0

    while (not arresto) and (it < it_max): 
        
        it += 1
        
        z1 = dot(A, z0)  # prodotto matrice-vettore
        sigma1 = dot(z1, z0) / dot(z0, z0)  
        
        Er = abs(sigma1 - sigma0) / abs(sigma1)  # errore relativo
        arresto = Er < tol
        
        if arresto:
            print("Precisione raggiunta")
        elif it == it_max :
            print("Limite numero iterazioni raggiunto")
        
        z0 = z1
        sigma0 = sigma1
        
        

    
        

    return sigma1, z1, it


A = array([[13, 2 , 0], 
           [2,  1,  3],
           [0,  3, 22]])

y0 = array([1, 1,1])
tol = 1e-6
it_max = 100

autovalore_dominante, autovettore, it = potenze(A, y0, tol, it_max)

print("Autovalore dominante:", autovalore_dominante)
print("Autovettore dominante:", autovettore)
print("Numero iterazioni:", it)