"""3.Escribe un programa que muestre en pantalla los numeros multiplos de 7 del 1 al 100"""

for n in range(1,101,1):#ciclo for de 1 a 100 
    if n%7==0:#Condicional if con argumento n mod 7==0 para los multiplos de 7 
        print(n)#Imprime el valor que cumple el if
    else:#otro camino
        pass#se continua el programa

 