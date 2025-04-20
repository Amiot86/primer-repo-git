numero = int(input("Ingrese un número entre 1 y 10: "))

if numero >= 1 and numero <= 10:
    for contador in range(1,11):
        print(numero,"X",contador,"=",(numero * contador))
else:
    print("No puso un número entre 1 y 10")