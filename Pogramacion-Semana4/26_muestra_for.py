# 26_muestra for.py

cont = 1
while cont <= 5:
    print(cont, "Debo caprender ciclos")
    cont = cont + 1

print("//////////////////")

for x in range(6):
    print(x,"Debo aprender ciclos")

print("//////////////////")

for x in range(1,6): #Va del 1 al 5 porque no toma el 6
    print(x,"Debo aprender ciclos")

print("//////////////////")

for x in range(1,11,2): #Va del 1 al 10 porque no toma el 11
    print(x,"Debo aprender ciclos")

print("//////////////////")

for x in range(100,90,-1): #Va del 100 al 91 porque no incluye el 90
    print(x,"Debo aprender ciclos")