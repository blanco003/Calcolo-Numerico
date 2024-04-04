# metodo iterativo
def frazione_continua_iterative(x):
    val = x[len(x)-1]
    for i in range(len(x) - 2, -1, -1): # dal penultimo elemento di x e si ferma al primo (-1 è escluso quindi 0) e ad ogni passo decrementa di 1
        val = x[i] + 1 / val
    return val

# metodo ricorsivo
def frazione_continua_recursive(x):
    return get_next_fraction_val(x, 0)

def get_next_fraction_val(x, index):
    if index == len(x) - 1:
        return x[index]
    else:
        return x[index] + 1 / get_next_fraction_val(x, index + 1)



print (frazione_continua_iterative([3,4,12,4]))
print (frazione_continua_recursive([3,4,12,4]))
