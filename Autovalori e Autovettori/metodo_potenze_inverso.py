from numpy import *

def potenze_inverse(A, x0, tol, it_max):

    """
    Metodo per il calcolo dell'autovalore di minimo modulo della matrice quadrata A.

    INPUT:
        - A : matrice quadrata che ammette autovalore dominante
        - y0 : vettore iniziale dell'iterazione
        - tol : precisione richiesta
        - it_max : numero max di iterazioni consentiti
    
    OUTPUT:
        - sigma1 : autovalore di minimo modulo di A
        - z1 : autovettore corrispondente all'autovalore di minimo modulo di A
        - it : numero di iterazioni eseguite
    """

    v0 = 0  # Inizializzazione dell'autovalore precedente
    it = 0  # contatore iterazioni
    arresto = False # criterio d'arresto basato sull'errore relativo

    while (not arresto) and (it < it_max):
        it += 1
        yk = x0 / linalg.norm(x0)  # Normalizza il vettore iniziale
        xk = linalg.solve(A,yk) # Risolve il sistema A * xk = yk
        vk = dot(transpose(yk),xk) # Calcola l'autovalore approssimato

        if abs(vk-v0) / abs(vk) < tol :
            arresto = True
            print("Precisione richiesta raggiunta")

        if it == it_max:
            print("Limite iterazioni raggiunto")
        
        v0 = vk  # aggiorniamo l'autovalore per la prossima iterazione
        x0 = xk  # aggiorniamo l'autovettore per la prossima iterazione

    return 1/vk ,  xk / linalg.norm(xk, 2), it  # l'autovalore di minimo modulo è dato dall'inverso dell'ultima iterazione

    
A = array([[13, 2, 0],
           [2, 1 ,3],
           [0, 3 , 22]])

y0 = array([1,1,1])

tol = 1e-15
it_max = 200

autovalore_minimo, autovettore, it = potenze_inverse(A,y0,tol,it_max)

print("Autovalore di minimo modulo:", autovalore_minimo)
print("Autovettore associato:", autovettore)
print("Numero iterazioni:", it)

