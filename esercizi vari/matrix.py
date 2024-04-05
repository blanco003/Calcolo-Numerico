import numpy as np

# stampa la matrice
def print_matrix(m):
    r, c = m.shape
    for i in range (0, r):
        for j in range(0, c): 
            print(m[i][j], end=' ')
        print()


# effettua il prodotto tra una matrice e uno scalare
def scalar_product(m,x):
    r, c = m.shape
    for i in range (0, r):
        for j in range(0, c): 
            m[i,j] = m[i,j] + x

# effettua la somma di 2 matrici : le matrici devono avere le stesse dimensioni
def sum_matrix(m1,m2):
    row_m1, col_m1 = m1.shape
    row_m2, col_m2 = m2.shape
    if row_m1 != row_m2 or col_m1 != col_m2:
        print("cant sum , matrices have different sizes")
        return
    m3 = np.zeros(shape=(row_m1, col_m1))  # sum matrix initialization
    for i in range (0, row_m1):
        for j in range(0, col_m1): 
            m3[i,j] = m1[i,j] + m2[i,j]
    return m3

# trasposta di una matrice : matrice ottenuta scambiandone le righe con le colonne
def trasponse_matrix(m):
    r, c = m.shape
    t = np.zeros(shape=(c,r),dtype=int)
    for i in range (0,r):
        for j in range (0,c):
            t[j,i] = m[i,j]
    return t


""" Si scriva una funzione che abbia in input un vettore (array o lista) x le cui componenti siano interi compresi tra 0 e 9, e in
     output un ' array (o matrice) A di due colonne cosi definita:
    - la prima colonna di A riporta le cifre distinte del vettore x
    - il generico elemento della seconda colonna di A riporta il numero di volte in cui la cifra corrispondente nella prima colonna compare nel
    vettore x
"""

# matrice simmetrica : restituisce true se la matrice è simmetrica, false altrimenti
def simmetric(m):
    rows, columns = m.shape
    for i in range (0,rows):
        for j in range (0,columns):
            if m[i][j] != m[j][i]:
                return False
    return True

""" 
test1 = np.array([[2,-1,5],[-1,5,7],[5,7,-1]]) # simmetric : True
test2 = np.array([[1,-1,3],[0,5,4],[1,2,3]]) # simmetric : False
test3 = np.array([[3,2,1],[2,4,0],[1,0,5]]) # simmetric : True
print("test 1 : ", simmetric(test1))
print("test 2 : ", simmetric(test2))
print("test 3 : ", simmetric(test3))
"""