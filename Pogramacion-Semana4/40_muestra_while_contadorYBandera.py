
# sueldo_anual = 0

# for cont_meses in range(1,13):
    # print("Ingrese su sueldo para el mes n°",cont_meses)
    # sueldo_mensual = float(input())
    #sueldo_anual += sueldo_mensual

# print("Tu sueldo anual es", sueldo_anual)

sueldo_anual = 0
cont_meses = 1

print("Ingrese su sueldo para el mes n°",cont_meses)
sueldo_mensual = float(input())
while cont_meses < 12 and sueldo_mensual > 0:
    sueldo_anual += sueldo_mensual
    cont_meses += 1
    print("Ingrese su sueldo para el mes n°",cont_meses)
    sueldo_mensual = float(input())

if sueldo_mensual > 0:
    sueldo_anual += sueldo_mensual

print("Tu sueldo anual es", sueldo_anual)