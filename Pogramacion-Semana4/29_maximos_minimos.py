
cant_numeros = 4

for cont in range(cant_numeros):
    print("Ingrese número",(cont+1))
    num = int(input())

print("////////////////////")

# Cuál fue el maximo registrado?
cant_numeros = 4
max_numero = float('-inf')

for cont in range(cant_numeros):
    print("Ingrese número",(cont+1))
    num = int(input())
    if num > max_numero:
        max_numero = num

print("El máximo es", max_numero)        

print("////////////////////")

# Calcular un valor minimo
cant_numeros = 4
min_numero = float('+inf')

for cont in range(cant_numeros):
    print("Ingrese número",(cont+1))
    num = int(input())
    if num < min_numero:
        min_numero = num

print("El minimo es", min_numero) 

print("////////////////")

# Calcular el máximo y el minimo
cant_numeros = 4
max_numero = float('-inf')
min_numero = float('+inf')

for cont in range(cant_numeros):
    print("Ingrese número",(cont+1))
    num = int(input())
    if num > max_numero:
        max_numero = num
    elif num < min_numero:
        min_numero = num

print("El maximo es", max_numero) 
print("El minimo es", min_numero) 

print("////////////////")

# 
cant_numeros = 4

print("Ingrese número 1")
num = int(input())

max_numero = num
min_numero = num
pos_max = 1
pos_min = 1


for cont in range(2,cant_numeros+1):
    print("Ingrese número",(cont+1))
    num = int(input())
    if num > max_numero:
        max_numero = num
        pos_max = cont
    elif num < min_numero:
        min_numero = num
        pos_min = cont

print("El maximo es", max_numero," y salió en la pos. ",pos_max) 
print("El minimo es", min_numero," y salió en la pos. ",pos_min) 