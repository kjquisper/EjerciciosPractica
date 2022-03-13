"""1.Escribe en un programa que utilice un bucle para crear una lista con los numeros del 1 al 10 y luego   
la muestre por pantalla."""

list=[]#Declarar variable lista
for n in range(1,11,1):#Define el rango de 0 a 10
    list.append(n)#Se usa la funcion append(adjuntar) para agregar valores a la lista

print(f"La lista creada: {list}")#Se imprime la lista

#end

