# Convierte la cadena "Python,Java,C++,JavaScript,PHP" en una lista de lenguajes de programación 
# utilizando split(). Luego añade "Ruby" a la lista e imprime los lenguajes por consola.

cadena = "Python, Java, C++, JavaScript, PHP"
lista_lenguajes = cadena.split()
lista_lenguajes.append("Ruby")

print(lista_lenguajes)