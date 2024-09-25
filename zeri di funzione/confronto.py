import numpy as np
import matplotlib.pyplot as plt

from bisezioni import bisezioni_successione
from newton import newton_successione
from secanti import secanti_successione
from newton_modificato import newton_modificato_successione


def confronto_metodi(f, f_primo, a, b, x0, x1, tol, it_max):
    
    """
    Confronta i metodi di ricerca dello zero di una funzione (bisezioni, Newton, Newton Modificato (Corde e Secanti)), 
    in base alla loro velocità nel raggiungere la precisione richiesta, creando un grafico avente sull'asse delle ascisse il numero
    di iterazioni effettuare per arrivare alla precisione richiesta e sull'asse delle ordinate l'errore relativo generato in base 
    all'approssimazione dell'iterazione corrispondente.

    INPUT:
        - f : funzione di cui ricercare lo zero
        - f_primo : derivata della funzione (per semplicità ed evitare di calcolarla)
        - a, b : estremi dell'intervallo per il metodo delle bisezioni
        - x0, x1 : stime iniziali per i metodi di Newton 
        - tol : precisione richiesta
        - it_max : numero massimo di iterazioni consentite
    """

    # eseguiamo i diversi metodi di ricerca dello zero con circa gli stessi parametri di input
    errori_bis = bisezioni_successione(f, a, b, tol, it_max)
    errori_newton = newton_successione(f, f_primo, x0, tol, it_max)
    errori_secanti= secanti_successione(f, x0, x1, tol, it_max)
    errori_corde = newton_modificato_successione(f, f_primo ,x0, tol, it_max)
    
    
    # creiamo il grafico
    plt.figure(figsize=(10, 6))

    # plot crea negli assi cartesiano il grafico della funzione, prendendo in input il vettore delle ascisse, 
    # il vettore delle ordinate, ed eventuali stili di formattazione

    # Consideriamo come ascisse il numero di iterate e quindi la dimensione del vettore risultante dalle approssimazioni del metodo
    # e come ordinate la precisione ottenutta all'iterata corrispodente

    plt.plot(range(0,len(errori_bis)), errori_bis, label='Bisezioni', marker='o')
    plt.plot(range(0,len(errori_newton)), errori_newton, label='Newton', marker='s')
    plt.plot(range(0,len(errori_secanti)), errori_secanti, label='Secanti', marker='^')
    plt.plot(range(0,len(errori_corde)), errori_corde, label='Corde', marker='p')

    
    plt.yscale('log')  # scala logaritmica per mostrare la grandezza degli errori
    plt.xlabel('Numero di Iterazioni')
    plt.ylabel('Precisione raggiunta')
    plt.title('Confronto Metodi')
    plt.legend()
    plt.grid(True)
    plt.show()


# esempio

def f(x):
    return x**2 -2

def f_primo(x):
    return 2*x


a = 0  
b = 2  
x0 = 2 
x1 = 3  
tol = 1e-9  
it_max = 50 


confronto_metodi(f, f_primo, a, b, x0, x1, tol, it_max)

"""

OSSERVAZIONI : 

- BISEZIONI : 

Il metodo delle successive bisezioni è un metodo, seppur necessità di più iterazioni, che converge sempre allo zero alpha di f.
Il numero di valutazioni di funzione per ogni iterazione è 1, quindi il costo computazionale non è troppo elavato.
La velocità di convergenza dipende dall'ampiezza dell'intervallo [a,b] scelto, tanto più grande tante più iterazioni saranno richieste.


- NEWTON : 

Il metodo di Newton risulta essere come notiamo dal grafico molto più veloce a convergere allo zero di alpha rispetto al 
metodo delle successive bisezioni (dalla teoria sappiamo che ha convergenza quadratrica)
Il numero di valutazioni di funzione per ogni iterazioni è 2, dunque anche se più veloce risulta più costoso rispetto 
al metodo delle successive bisezioni.
Osserviamo inoltre che il numero di iterazioni dipende anche notevolmente dalla stima iniziale x0 dello zero alpha di f.


- NEWTON MODIFICATO (CORDE) : 

Variante del metodo di Newton, nella quale al posto di calcolare ogni volta la derivata prima (e quindi avere 2 valutazioni di 
funzione per iterata come Newton) viene calcolata la derivata prima solo nel punto inziale x0. 
Anche se risulta meno veloce (convergenza linerare) a convergere alla zero alpha di f tuttavia ha un costo computazionale minore.


- SECANTI :

Un'altra variante del metodo di Newton, nella quale viene approssiamata la funzione derivata prima 
f'(x_n) con [ f(x_n)-f(x_n-1) ] / x_n - x_n-1  (quindi si hanno 2 valutazioni di funzione per iterata )
Osserviamo che man mano l'intervallo si restringe i punti trovati tendono ai punti trovati col metodo di Newton, questo perché 
la secante tenderà a coincidere con la derivata. 
Risulta essere quindi quasi veloce (convergenza superlineare) a convergere allo zero alpha di f come il metodo di Newton, 
avendo tuttavia un costo computazionale  minore.

"""

