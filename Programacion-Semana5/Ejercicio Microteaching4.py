# Genera una lista con los números impares del 1 al 20 utilizando range(). Luego, crea otra lista 
# que contenga sólo los números de la primera lista que son divisibles por 3.


lista = list(range(1,21,2))

print (lista)

nueva_lista = []
for i in range(len(lista)):
    if lista[i] % 3 ==0:
        nueva_lista.append(lista[i])
print(nueva_lista)
