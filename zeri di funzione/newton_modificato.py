from numpy import *

def newton_modificato(f,f_primo,x0,tol,it_max):
    
    """
    Variante del Metodo di Newton per la ricerca degli zeri di una funzione (Anche noto come metodo delle corde).

    INPUT:
        - f : funzione di cui ricercare lo zero
        - f : derivata prima della funzione di cui ricercare lo zero
        - x0 : stima iniziale
        - tol : precisione richiesta
        - it_max : numero massimo di iterate consentite
    OUTPUT:
        - x1 : approssimazione dello zero di f
        - it : numero di iterate effettuate
   """
   
    arresto = False    # criterio d'arresto basato sull'errore relativo
    it = 0
    
    f_primo_x0 = f_primo(x0)  # valutiamo la derivata della funzione solo nel punto inziale x0
    
    while (not arresto) and (it < it_max):
        it += 1
        
        x1 = x0 - f(x0) / f_primo_x0
        
        arresto = ( ( abs(x0-x1) / abs(x1)  ) < tol ) 
        
        #print(f"Numero iterazione {it}, approssimazione corrente : {x1}")
        
        if (it == it_max):
            print("Limite numero di iterazioni raggiunto")
        
        if (arresto):
            print("Precisione richiesta raggiunta")
        
        x0 = x1
    
    return x1, it



def newton_modificato_successione(f,f_primo,x0,tol,it_max):
    
    """
    Variante del Metodo di Newton per la ricerca degli zeri di una funzione (Anche noto come metodo delle corde),  restituisce la successione 
    degli errori di iterazione in iterazione per mostrare la velocità della riduzione e l'avvicinamento alla precisione richiesta 
    tramite il grafico del confronto tra metodi.

    INPUT:
        - f : funzione di cui ricercare lo zero
        - f : derivata prima della funzione di cui ricercare lo zero
        - x0 : stima iniziale
        - tol : precisione richiesta
        - it_max : numero massimo di iterate consentite
    OUTPUT:
        - xn_eps : successione degli errori
   """
   
    arresto = False    # criterio d'arresto basato sull'errore relativo
    it = 0
    
    f_primo_x0 = f_primo(x0)  # valutiamo la derivata della funzione solo nel punto inziale x0
    
    xn_eps = []
    
    while (not arresto) and (it < it_max):
        it += 1
        
        x1 = x0 - f(x0) / f_primo_x0
        
        arresto = ( ( abs(x0-x1) / abs(x1)  ) < tol ) 
        
        xn_eps.append( abs(x0-x1) / abs(x1)  )
        
        #print(f"Numero iterazione {it}, approssimazione corrente : {x1}")
        
        if (it == it_max):
            print("Newton Modificato (Corde) : Limite numero di iterazioni raggiunto")
        
        if (arresto):
            print("Newton Modificato (Corde) : Precisione richiesta raggiunta in",it,"iterazioni")
        
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

alpha, it = newton_modificato(f,f_primo ,x0, tol, it_max)
print(f"Numero iterazioni eseguite : {it} \nApprossimazione dello zero di f : {alpha}")

"""

