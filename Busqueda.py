import random
import time

def busqueda_lineal(l,valor):
    for i in range(len(l)):
        if l[i]==valor:
            return 1
        else: return -1

def busqueda_binaria(l,valor,inicio=None,final=None):
    if inicio is None:
        inicio=0
    if final is None:
        final=len(l)-1
    
    if final<inicio:
        return -1
    
    medio=(inicio+final)//2

    if l[medio]==valor:
        return medio
    elif valor<medio:
        return busqueda_binaria(l,valor,inicio,medio-1)
    else:
        return busqueda_binaria(l,valor,medio+1,final)

if __name__=="__main__":
    tamaño=10000
    sorted_list =set()

    while len(sorted_list)<tamaño:
        sorted_list.add(random.randint(-3*tamaño,3*tamaño))
    sorted_list=sorted(list(sorted_list))

    inicio1=time.time()
    for valor in sorted_list:
        busqueda_lineal(sorted_list,valor)
    final1=time.time()
    print("Tiempo en Busqueda Lineal: ",(final1-inicio1),"s") 

    inicio1=time.time()
    for valor in sorted_list:
        busqueda_binaria(sorted_list,valor)
    final1=time.time()
    print("Tiempo en Busqueda Binaria: ",(final1-inicio1),"s") 