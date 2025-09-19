"""
Utilizar la técnica de listas por comprensión para construir una lista con todos los
números impares comprendidos entre 100 y 200.
"""
lista = [numero for numero in range(101, 200) if numero % 2 != 0]

print(lista)