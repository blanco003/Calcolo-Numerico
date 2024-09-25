from numpy import *

def is_triangolare_superiore(A):
    
    righe,colonne = A.shape
    
    for i in range(0,righe):
        for j in range(0,i):
            if A[i,j] != 0:
                return False
    
    return True



def is_triangolare_inferiore(A):
    
    righe,colonne = A.shape
    
    for i in range(0,righe):
        for j in range(i+1,colonne):
            if A[i,j] != 0:
                return False
            
    
    return True



A = array( [ [1,1,0],
             [0,0,2],
             [0,0,3]])

print(is_triangolare_superiore(A))

B = array( [ [1,0,0],
             [-1,-2,0],
             [2,-4,3]])

print(is_triangolare_inferiore(B))