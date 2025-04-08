umbral = 10
sumatoria = 0

# Control de ciclos
while sumatoria < umbral:
    print("Ingrese número: ")
    num = int(input())
    sumatoria += num  # sumatoria = sumatoria + num

print ("/////////////////")

umbral = 10
sumatoria = 0
cont = 0

# Control de ciclos por bandera
while sumatoria < umbral:
    cont += 1  # cont = cont + 1
    print("Ingrese número: ",cont)
    num = int(input())
    sumatoria += num   # sumatoria = sumatoria + num

print("El promedio de valores es",(sumatoria / cont))