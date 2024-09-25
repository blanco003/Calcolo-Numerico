"""
Possiamo osservare che scegliendo un numero elevato di nodi di interpolazione equidistanti, 
accadde il fenomeno di Runge, ovvero il polinomio di interpolazione di Lagrange presenta forti oscillazioni 
specialmente ai bordi dell'intervallo, producendo un'interpolazione imprecisa per funzioni non regolari.

Tale fenomeno può essere evitato considerando non più nodi equidistanti ma scegliendo come nodi di interpolazione
i cosidetti nodi di Chebyshev-Gauss-Lobatto, x_i = (a+b)/2 + (b-a)/2 * x^_i  , dove x^_i = - cos(pi/n)  , i = 0,..,n

E' possibile dimostare che se f è una funzione continua e derivabile in [a,b], allora il polinomio interpolante associato alla
distribuzione dei nodi di Chebyshev converge ad f per n->infinito per ogni x in [a,b]. Questo non era detto per i nodi equidistanti,
in quanto un aumento del numero di nodi di interpolazione non implicava necessariamento un miglioramento dell'approssimazione di f.

I  nodi di  Chebyshev-Gauss-Lobatto, scelti in modo arbitrario in modo da rapprensentare le ascisse di nodi equispaziati 
sulla semicirconferenza di raggio uno, appartengono all' intervallo [a, b] e si addensano vicino agli estremi dell' intervallo, 
proprio dove l'interpolazione con nodi equidistanti risultava oscillante.
"""

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



def confronta_interpolazioni(f, a, b, n):

    """
    Confronta graficamente l'interpolazione di una funzione f(x) usando nodi equispaziati
    e nodi di Chebyshev nell'intervallo [a, b] con n nodi.
    
    INPUT:
        - f: funzione da interpolare
        - a: estremo sinistro dell'intervallo [a, b]
        - b: estremo destro dell'intervallo [a, b]
        - n: numero di nodi
    """

    # linspace genera un array di punti equidistanti nell'intervallo [a,b], dividendo l'intervallo in n parti uguali
    x_equidistanti_lagrange = np.linspace(a, b, n)
    y_equidistanti_lagrange = f(x_equidistanti_lagrange)
    
    # calcoliamo i nodi di chebyshev
    x_cheb = nodi_chebyshev(a, b, n)
    y_cheb = f(x_cheb)
    
    # valutiamo la funzione nei punti prestabiliti
    xx = np.linspace(a, b, 1000)
    fxx = f(xx)
    
    # interpolazione con nodi equispaziati
    pxx_equi = lagrange(x_equidistanti_lagrange, y_equidistanti_lagrange, xx)
    
    # interpolazione con nodi di Chebyshev
    pxx_cheb = lagrange(x_cheb, y_cheb, xx)
    

    plt.figure(figsize=(10, 6))

    # plot crea negli assi il grafico della funzione / i punti, prendendo in input il vettore delle ascisse, 
    # il vettore delle ordinate, ed eventuali stili di formattazione
    
    # mostriamo a schermo i grafici della funzione e dei polinomi interpolanti
    plt.plot(xx, fxx, label="f(x)", color="black", linewidth=2)
    plt.plot(xx, pxx_equi, label="Interpolazione Lagrange (nodi equispaziati)", linestyle='--', color="red")
    plt.plot(xx, pxx_cheb, label="Interpolazione Lagrange (nodi di Chebyshev)", linestyle='--', color="blue")
    
    # mostriamo a schermo i punti di interpolazione di entrambi i polinomi
    plt.plot(x_equidistanti_lagrange, y_equidistanti_lagrange, 'ro', label="Nodi equispaziati")
    plt.plot(x_cheb, y_cheb, 'bo', label="Nodi di Chebyshev")
    
    plt.legend()
    plt.title(f"Confronto tra interpolazione con {n} nodi equispaziati e nodi di Chebyshev")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.grid(True)
    plt.show()


# esempio

def runge(x):
    return 1 / (1 + x**2)

confronta_interpolazioni(runge, -5, 5, 15)
