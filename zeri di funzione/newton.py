from numpy import*

def newton(f,x0,tol,it_max,stampa=0):
    
    """
    Metodo di Newton per la ricerca degli zeri di una funzione

    Parametri di input:
         f : funzione di cui ricercare uno zero
        x0 : punto iniziale
       tol : precisione richiesta
    it_max : numero massimo di iterate consentite

    Parametri di output:
        x1 : approssimazione dello zero di f
        it : numero di iterate effettuate

   """
    it = 0
    arresto = False

    while not arresto and it <= it_max:
        it = it + 1
        x1 = x0 - f(x0) / f(x0,1)
        arresto = abs(x0-x1)/(1+abs(x1)) < tol    # errore misto
        if stampa : print(x1)
        x0 = x1
    return x1,it
    


def f(x,ord=0):
    if ord==0:
        y=x-cos(x)
    elif ord==1:
        y=1+sin(x)
    else:
        print("secondo argomento non definito")
        y=NaN
    return y