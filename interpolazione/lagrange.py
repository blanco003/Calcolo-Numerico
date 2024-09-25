import numpy as np
import matplotlib.pyplot as plt

# effettuare prima pip install matplotlib

def lagrange(x, y, xx):
    
    """
    Costruisce il polinomio interpolante di Lagrange definito dai nodi x e dalle ordinate y, e lo valuta nei punti xx
    
    INPUT: 
        - x: vettore dei nodi
        - y: vettore delle ordinate
        - xx: vettore di punti (ascisse) in cui valutare il polinomio
    OUTPUT:
        - p: vettore contenente le valutazioni del polinomio che interpola i dati x,y nei punti del vettore xx
    """
    
    n = len(x)   
    p = 0  
    
    for k in range(n):
        Lk = 1
        
        for i in range(n):
            
            if i != k:
                Lk = Lk * (xx - x[i]) / (x[k] - x[i])  # k-esimo polinomio cardinale di Lagrange
                
        p = p + Lk * y[k]
        
    return p


def interpola(f, a, b, n):
    
    """
    Costruisce e disegna il polinomio che interpola una funzione f(x) in n nodi uniformemente distribuiti nell'intervallo [a,b]  
    
    INPUT: 
        - f : funzione da approssimare mediante un polinomio interpolante di Lagrange
        - a : estremo sinistro dell'intervallo in cui approssimare la funzione f
        - b : estremo destro dell'intervallo in cui approssimare la funzione f
        - n : numero di punti in cui interpolare la funzione con il polinomio
    """
    
    # linspace genera un array di punti equidistanti nell'intervallo [a,b], dividendo l'intervallo in n parti uguali

    x = np.linspace(a, b, n)  # vettore dei nodi 
    y = f(x)   # vettore delle ascisse

    xx = np.linspace(a, b, 100)   # dividiamo il grafico in 100 punti in cui verra valutata la funzione
    # ho scelto 100 per rendere il grafico abbastanza dettagliato e non segmentato

    # valutiamo i punti nella funzione desisderata
    fxx = f(xx)
    pxx = lagrange(x, y, xx)  

    # plot crea negli assi il grafico della funzione / i punti, prendendo in input il vettore delle ascisse, 
    # il vettore delle ordinate, ed eventuali stili di formattazione

    plt.plot(x, y, "o", label="punti di interpolazione")
    plt.plot(xx, fxx, label="f(x)")
    plt.plot(xx, pxx, label="p(x)")

    # mostra nella schermata la leggenda
    plt.legend()  

    # titolo del grafico
    plt.title(f"Approssimazione di f(x) con pn(x) con {n} punti di interpolazione")

    # manda in output a video la finestra contenente il grafico costruito
    plt.show()


# esempio 1
def f(x):
    return  np.exp(-x) * np.sin(2*x)

# esempio 2
def runge(x):
    return 1 / (1 + x**2)


# esempio 1
interpola(f, 0 , np.pi/2 , 5)
interpola(f, 0 , np.pi/2 , 15)
interpola(f, 0 , np.pi/2 , 35)

# esempio 2
interpola(runge, -5, 5,9)
interpola(runge, -5, 5,15)
interpola(runge, -5, 5,35)
