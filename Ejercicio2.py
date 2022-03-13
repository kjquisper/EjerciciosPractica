"""2.Escribe un programa que apartir de una tupla cualquiera, obtenga un lista con todos los 
elementos de la tupla"""

t1=(1,2,3,'uno','dos','tres')#declaro una tupla cualquiera

list1=[]#declaro un variable tipo lista

for n in t1:#bucle for de la tupla 
    list1.append(n)#agrego los elementos de la tupla a la lista list1

print(f"La Lista de los elementos de la tupla: {list1}")