cant_numeros = 5

for cont in range(1,cant_numeros+1):
    print("Ingrese número", cont)
    num = int(input())

print("/////////////////")

# Variable de tipo acumuladora para tener la sumatoria de valores ingresados por el usuario
cant_numeros = 5
sumatoria = 0

for cont in range(1,cant_numeros+1):
    print("Ingrese número", cont)
    num = int(input())
    sumatoria = sumatoria + num
    print()

print("La sumatoria de los valores es", sumatoria)
print("El valor promedio es",(sumatoria/cant_numeros))