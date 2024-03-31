from numpy import*

def bisezioni(f,a,b,tol,itmax=100):
    """
    Metodo delle successive bisezioni

    Parametri di input:
        f : funzione di cui ricercare uno zero alpha
    [a,b] : intervallo di lavoro
      tol : precisione richiesta
    itmax : numero massimo di iterate consentite

    Parametri di output:
    alpha : zero di f
  """

    fa = f(a)
    fb = f(b)
  

    if fa*fb > 0:
       print('La funzione non cambia segno agli estremi dell''intervallo')

    it=0

    while b-a > tol and it<itmax:
      it=it+1
      c = (a+b)/2
      fc = f(c)

    if fc==0:
        alpha = c
        return
    elif fa*fc < 0:
        b = c
        fb = fc  # e' possibile eliminare questa assegnazione
    else:
        a = c
        fa = fc

    if b-a>tol:
        print('precisione non raggiunta')
  
    return c

def f1(x):
    return x-cos(x)
