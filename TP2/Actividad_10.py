"""
Generar una lista con números al azar entre 1 y 100 y crear una nueva lista con los
elementos de la primera que sean impares. El proceso deberá realizarse utilizando
la función filter(). Imprimir las dos listas por pantalla.
"""
import random as rnd

lista = [rnd.randint(1, 100) for _ in range(20)]

impares = list(filter(lambda x: x % 2 != 0, lista))

print(f"Lista original: {lista}")
print(f"Lista impares: {impares}")