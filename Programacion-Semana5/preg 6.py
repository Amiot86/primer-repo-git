n=5
a=[0]*n
b=[0]*n

for i in range(n):
    b[i]=i*2

contador=0
for i in range(n):
    if a[0] == a[i] and a[0] == b[i]:
        contador+=1
        n=n-contador

resultado=str(contador)

if a[0] == 1:
    resultado="VERDADERO"
elif a[0] == 2:
    resultado="2"
elif a[0] == 3:
    resultado = "FALSO"

print(resultado)
