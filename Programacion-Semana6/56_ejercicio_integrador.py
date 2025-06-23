import utils
# Definicion de funciones
def imprimir_matriz(nro_columnas, nro_filas):
    utils.imprimir_simbolo("X, nro_columnas")

# Programa principal
ancho = utils.leer_entero_validado("Ingrese el ancho", 1)
alto = utils.leer_entero_validado("Ingrese el alto", 1)
# print (f"Seguimos adelante con ancho {ancho} y alto {alto}")
imprimir_matriz(ancho, alto)

