from numpy import*

def bisezioni(f,a,b,tol,it_max):
    
    """
    Metodo delle successive bisezioni per la ricerca degli zeri di una funzione.

    INPUT:
        - f : funzione di cui ricercare uno zero alpha
        - a : estremo sinistro dell'intervallo da considerare
        - b : estremo destro dell'intervallo da considerare
        - tol : precisione richiesta
        - it_max : numero massimo di iterate consentite
    OUTPUT:
        - alpha : approssimazione dello zero di f
        - it : numero di iterate effettuate
  """

    # valutiamo la funzione agli estremi dell'intervallo
    fa = f(a)
    fb = f(b)
  
    if fa*fb > 0:
       print('La funzione non cambia segno agli estremi dell''intervallo dunque non ammette zero')

    it = 0  # contatore iterate
    arresto = False  # criterio d'arresto basato sull'ampiezza dell'intervallo 
    
    while (not arresto) and (it < it_max):
      
        it=it+1
      
        c = (a+b)/2
        fc = f(c)  
        
        #print(f"Numero iterazione {it}, approssimazione corrente : {fc}") 

        if fc==0:  # abbiamo trovato lo zero di f
            alpha = c
            return alpha
    
        elif fa*fc < 0:
            # l'intervallo viene dimezzato ad [a_n; c_n]
            b = c
            fb = fc 
        else:
            # l'intervallo viene dimezzato ad [c_n; b_n]
            a = c
            fa = fc

        if it == it_max:
            print("Limite numero di iterazioni raggiunto")
            
        arresto = (b-a < tol)

        if  arresto:  
            print('Precisione richiesta raggiunta')
  
    return c, it


def bisezioni_successione(f,a,b,tol,it_max):
    
    """
    Metodo delle successive bisezioni per la ricerca degli zeri di una funzione, restituisce la successione degli errori di iterazione in iterazione
    per mostrare la velocità della riduzione e l'avvicinamento alla precisione richiesta tramite il grafico del confronto tra metodi.

    INPUT:
        - f : funzione di cui ricercare uno zero alpha
        - a : estremo sinistro dell'intervallo da considerare
        - b : estremo destro dell'intervallo da considerare
        - tol : precisione richiesta
        - it_max : numero massimo di iterate consentite
    OUTPUT:
        - xn_eps : successione degli errori
  """

    # valutiamo la funzione agli estremi dell'intervallo
    fa = f(a)
    fb = f(b)
  
    if fa*fb > 0:
       print('La funzione non cambia segno agli estremi dell''intervallo dunque non ammette zero')

    it = 0  # contatore iterate
    arresto = False  # criterio d'arresto basato sull'errore relativo
    
    xn_eps = []
    
    while (not arresto) and (it < it_max):
      
        it=it+1
      
        c = (a+b)/2
        fc = f(c) 
         
        #print(f"Numero iterazione {it}, approssimazione corrente : {fc}") 

        if fa*fc < 0:
            # l'intervallo viene dimezzato ad [a_n; c_n]
            b = c
            fb = fc 
        else:
            # l'intervallo viene dimezzato ad [c_n; b_n]
            a = c
            fa = fc

        if it == it_max:
            print("Bisezioni : Limite numero di iterazioni raggiunto")
            
        xn_eps.append(b-a)
            
        arresto = (b - a < tol)
        
        if  arresto:  
            print("Bisezioni : Precisione richiesta raggiunta in",it,"iterazioni")
  
    return xn_eps




"""
# ESEMPIO 

def f(x):
    return x**2 -2

x0 = 2
a = 0
b = 2
tol = 1e-8  # Precisione richiesta
it_max = 100  # Numero massimo di iterazioni

alpha, it = bisezioni(f, a, b, tol, it_max)
print(f"Numero iterazioni eseguite : {it} \nApprossimazione dello zero di f : {alpha}")
"""