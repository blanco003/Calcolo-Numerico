from numpy import*

def newton(f,f_primo,x0,tol,it_max):
    
    """
    Metodo di Newton per la ricerca degli zeri di una funzione.

    INPUT:
        - f : funzione di cui ricercare lo zero
        - f_primo : derivata della funzione di cui ricercare lo zero
        - x0 : stima iniziale
        - tol : precisione richiesta
        - it_max : numero massimo di iterate consentite
    OUTPUT:
        - x1 : approssimazione dello zero di f
        - it : numero di iterate effettuate

   """
   
    it = 0  # contatore iterazioni
    arresto = False  # criterio d'arresto basato sull'errore misto

    while (not arresto) and (it < it_max):
        
        it = it + 1
        x1 = x0 - f(x0) / f_primo(x0)
        
        arresto = ( abs(x0-x1) / (1+abs(x1)) < tol ) 
        
        # print(f"Numero iterazione {it}, approssimazione corrente : {x1}")
        
        if (it == it_max):
            print("Limite numero di iterazioni raggiunto")
        
        if (arresto):
            print("Precisione richiesta raggiunta")
        
        x0 = x1
        
    return x1,it

def newton_successione(f,f_primo,x0,tol,it_max):
    
    """
    Metodo di Newton per la ricerca degli zeri di una funzione, restituisce la successione degli errori di iterazione in iterazione
    per mostrare la velocità della riduzione e l'avvicinamento alla precisione richiesta tramite il grafico del confronto tra metodi.

    INPUT:
        - f : funzione di cui ricercare uno zero
        - x0 : stima iniziale
        - tol : precisione richiesta
        - it_max : numero massimo di iterate consentite
    OUTPUT:
        - xn_eps : successione degli errori

   """
   
    it = 0  # contatore iterazioni
    arresto = False  # criterio d'arresto basato sull'errore relativo
    

    xn_eps = []
    
    while (not arresto) and (it < it_max):
        
        it = it + 1
        x1 = x0 - f(x0) / f_primo(x0)
        
        xn_eps.append(( abs(x0-x1) / abs(x1)  ) )
        
        arresto = ( ( abs(x0-x1) / abs(x1)  ) < tol ) 
        
        #print(f"Numero iterazione {it}, approssimazione corrente : {x1}")
        
        if (it == it_max):
            print("Newton : Limite numero di iterazioni raggiunto")
        
        if (arresto):
            print("Newton : Precisione richiesta raggiunta in",it,"iterazioni")
        
        x0 = x1
        
    return xn_eps


"""

# ESEMPIO

def f(x):
    return x**2 -2

def f_primo(x):
    return 2*x

x0 = 2
tol = 1e-8  # Precisione richiesta
it_max = 100  # Numero massimo di iterazioni

alpha, it = newton(f,f_primo ,x0, tol, it_max)
print(f"Numero iterazioni eseguite : {it} \nApprossimazione dello zero di f : {alpha}")

"""