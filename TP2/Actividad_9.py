"""
Generar e imprimir una lista por comprensión entre A y B con los múltiplos de 7
que no sean múltiplos de 5. A y B se ingresar desde el teclado.
"""
a = int(input("Ingresar N° 1: "))
b = int(input("Ingresar N° 2: "))

lista = [numero for numero in range(a, b) if numero % 7 == 0 and numero % 5 != 0]

if a > b:
    print("Ingresar rango valido.")
elif len(lista) >= 1:
    print(lista)
else:
    print("No hay numeros que cumplan con el criterio.")