from numpy import*

def secanti(f,x0,x1,tol,it_max):
    
    """
    Metodo delle secanti per la ricerca degli zeri di una funzione.

    INPUT:
        - f : funzione di cui ricercare uno zero
        - x0,x1 : punti iniziali
        - tol : precisione richiesta
        - it_max : numero massimo di iterate consentite
    OUTPUT:
        - x2 : approssimazione dello zero di f
        - it : numero di iterate effettuate

   """
   
    it = 0  # contatore iterazioni
    arresto = False   # criterio d'arresto basato sull'errore relativo

    while (not arresto) and (it < it_max):
        
        it = it + 1
        x2 = x1 - ( f(x1) * ( (x1 - x0) / (f(x1) - f(x0))  ) ) 
        
        #print(f"Numero iterazione {it}, approssimazione corrente : {x2}")
        
        arresto = ( abs(x2-x1)/(abs(x2)) < tol )
        
        x0 = x1
        x1 = x2
    
        if (it == it_max):
            print("Limite numero di iterazioni raggiunto")
        
        if (arresto):
            print("Precisione richiesta raggiunta")
              
    return x2,it
    



def secanti_successione(f,x0,x1,tol,it_max):
    
    """
    Metodo delle secanti per la ricerca degli zeri di una funzione, restituisce la successione degli errori di iterazione in iterazione
    per mostrare la velocità della riduzione e l'avvicinamento alla precisione richiesta tramite il grafico del confronto tra metodi.

    INPUT:
        - f : funzione di cui ricercare uno zero
        - x0,x1 : punti iniziali
        - tol : precisione richiesta
        - it_max : numero massimo di iterate consentite
    OUTPUT:
        - xn_eps : successione degli errori

   """
   
    it = 0  # contatore iterazioni
    arresto = False   # criterio d'arresto basato sull'errore relativo
    
    xn_eps = []

    while (not arresto) and (it < it_max):
        
        it = it + 1
        x2 = x1 - ( f(x1) * ( (x1 - x0) / (f(x1) - f(x0))  ) ) 
        
        
        
        #print(f"Numero iterazione {it}, approssimazione corrente : {x2}")
        
        arresto = ( abs(x2-x1)/(abs(x2)) < tol )
        xn_eps.append(abs(x2-x1)/(abs(x2)))
        x0 = x1
        x1 = x2
    
        if (it == it_max):
            print("Secanti : Limite numero di iterazioni raggiunto")
        
        if (arresto):
            print("Secanti : Precisione richiesta raggiunta in",it,"iterazioni")
              
    return xn_eps


"""

# ESEMPIO

def f(x):
    return x**2 -2

x0 = 2
x1 = 3
tol = 1e-8  # Precisione richiesta
it_max = 100  # Numero massimo di iterazioni

alpha, it = secanti(f, x0, x1, tol, it_max)
print(f"Numero iterazioni eseguite : {it} \nApprossimazione dello zero di f : {alpha}")

"""