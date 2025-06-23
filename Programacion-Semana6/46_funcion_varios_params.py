# Definición de funciones
def obtener_resto(num1,num2):
    #return num1 % num2
    return num1 - num2 * num1 // num2 #Sin usar operador %

# Programa principal
a = int(input("primer número: "))
b = int(input("Segundo número: "))

resto = obtener_resto(a,b)

print(f"El resto entre {a} y {b} es {resto}")
