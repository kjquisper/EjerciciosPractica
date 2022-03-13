from statistics import median 
#se inporta la funcion median, para la media de una lista de numeros


list2=[]#Se crea la lista de valores 
for a in range(3):
    list2.append(int(input("numero: ")))#Se hace uso de la funcion append para agregar los valores desde teclado

media=median(list2)#se hace uso de la funcion "median" del modulo stadistics
print("la media es:",media)#se imprime la media
