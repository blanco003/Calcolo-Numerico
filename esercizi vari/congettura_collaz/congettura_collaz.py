import numpy as np

def congettura_collaz(x0):
    successione = [x0]
    xi = x0
    count = 0
    while xi != 1:
        count = count + 1
        if np.mod(xi,2) == 0:
            xi = int(xi/2)
        else : 
            xi = (3 * xi) +1
        successione.append(xi)
    return successione,count

xn,count = congettura_collaz(6)
print("numero di passi : ",count)
print("successione generata : ",xn)
    
