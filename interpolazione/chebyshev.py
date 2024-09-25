import numpy as np
import matplotlib.pyplot as plt

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


def nodi_chebyshev(a, b, n):
    
    """
    Restituisce i nodi di Chebyshev nell'intervallo [a,b]
    
    INPUT:
        - a: estremo sinistro dell'intervallo
        - b: estremo destro dell'intervallo
        - n: numero di nodi
    OUTPUT:
        - x: vettore dei nodi di Chebyshev
    """

    i = np.array(range(n+1))  # vettore degli indici dei nodi

    # calcoliamo i nodi di Chebyshev rappresentati le ascisse di nodi equispaziati sulla semicirconferenza di raggio uno, [-1,1]
    x_cheb = -np.cos(i * np.pi / n)  

    # e riscaliamoli nell'intervallo [a,b]
    x = 0.5 * (a + b) + 0.5 * (b - a) * x_cheb

    return x




def interpola_chebyshev(f, a, b, n):
    """
    Costruisce e disegna il polinomio che interpola una funzione f(x) usando nodi di Chebyshev in [a,b]  
    """
    
    # calcoliamo i nodi di Chebyshev
    x = nodi_chebyshev(a, b, n)  

    # valutiamo la funzione nei nodi calcolati
    y = f(x)  
    xx = np.linspace(a, b, 100)
    fxx = f(xx)
    
    # definiamo il polinio interpolante
    pxx = lagrange(x, y, xx)  

    # plot crea negli assi il grafico della funzione / i punti, prendendo in input il vettore delle ascisse, 
    # il vettore delle ordinate, ed eventuali stili di formattazione
    
    # mostriamo a schermo i grafici della funzione e dei polinomi interpolanti

    plt.plot(x, y, "o", label="nodi di interpolazione (Chebyshev)")
    plt.plot(xx, fxx, label="f(x)")
    plt.plot(xx, pxx, label="p(x)")
    plt.legend()
    plt.title(f"Approssimazione di f(x) con pn(x) con {n} nodi di Chebyshev")
    plt.show()



# esempio 2
def runge(x):
    return 1 / (1 + x**2)


#interpola_chebyshev(runge, -5, 5,5)
interpola_chebyshev(runge, -5, 5, 15)
