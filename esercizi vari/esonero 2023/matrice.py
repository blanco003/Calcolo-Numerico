import numpy as np

def funzione(A):
    x = 0
    rows, columns = A.shape
    for i in range (0,rows):
        riga = A[i,:]
        for j in range (0,columns):
            colonna = A[:,j]
            if np.array_equal(riga,colonna):
                x = 1
                return x
    return x

test1 = np.array([[-2,-1,2],[3,2,3],[2,3,0]])
x = funzione(test1)
print(test1)
print(x)

test2 = np.array([[-2,-1,2],[1,4,5],[6,7,8]])
x = funzione(test2)
print(test2)
print(x)
