contador=1
suma=0
bandera=True

num1=int(input("inrese un valor n°1:"))

while bandera:

    num2=int(input("Ingrese un valor n°2:"))
    suma = suma+num2
    contador=contador+1

    while contador <= num1:
        print(suma,end=",")
        bandera=False
        if contador == num1:
            bandera=True
        break