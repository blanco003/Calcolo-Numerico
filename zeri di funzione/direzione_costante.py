from numpy import *

def direzione_costante(f,f_primo,x0,m,tol,it_max):
    
    """
    Metodo della direzione costante per la ricerca degli zeri di una funzione.

    INPUT:
        - f : funzione di cui ricercare lo zero
        - f : derivata prima della funzione di cui ricercare lo zero
        - x0 : stima iniziale
        - m : parametro rapprensentate l'inverso del coefficiente angolare (1/m)
        - tol : precisione richiesta
        - it_max : numero massimo di iterate consentite
    OUTPUT:
        - x1 : approssimazione dello zero di f
        - it : numero di iterate effettuate
   """
   
    arresto = False    # criterio d'arresto basato sull'errore relativo
    it = 0
    
    # controlliamo il parametro m sia stato inserito correttamente affichè si abbia convergenza globale con il metodo della direzione costante
    # (assumendo x0 sia una stima abbastanza buona dello zero di f)
    if not (0 < m * f_primo(x0) <= 1):
        raise("Successione non convergente")
        
        
    while (not arresto) and (it < it_max):
        
        it += 1
        
        x1 = x0 - m * f(x0)
        
        arresto = ( ( abs(x0-x1) / abs(x1)  ) < tol ) 
        
        #print(f"Numero iterazione {it}, approssimazione corrente : {x1}")
        
        if (it == it_max):
            print("Limite numero di iterazioni raggiunto")
        
        if (arresto):
            print("Precisione richiesta raggiunta")
        
        x0 = x1
    
    return x1, it


def f(x):
    return x**2 -2

def f_primo(x):
    return 2*x


x0 = 2
tol = 1e-8  # Precisione richiesta
it_max = 100  # Numero massimo di iterazioni
m = 1 / (2 * abs(x0)) # scelta del parametro m

alpha, it = direzione_costante(f,f_primo ,x0, m, tol, it_max)
print(f"Numero iterazioni eseguite : {it} \nApprossimazione dello zero di f : {alpha}")