"""
Escribir una función que reciba una lista de números enteros como parámetro y la
normalice, es decir que todos sus elementos deben sumar 1.0, respetando las pro-
porciones relativas que cada elemento tiene en la lista original. Desarrollar también
un programa que permita verificar el comportamiento de la función. Por ejemplo,
normalizar([1, 1, 2]) debe devolver [0.25, 0.25, 0.50].
"""
import random as rnd

rnd.seed(1)

def normalizar_numeros(lista: list) -> list:
    """
    Normaliza los números de una lista para que su suma sea 1.0.
    Retorna una lista vacía si la entrada está vacía.
    Los valores se redondean a 3 decimales para mayor precisión.
    """
    if not lista:
        return []

    suma_total = sum(lista)
    if suma_total == 0:
        return [0.0] * len(lista)

    lista_normalizada = [round(i / suma_total, 3) for i in lista]
    return lista_normalizada


def probar_normalizacion():
    """
    Función de prueba que verifica la normalización de diferentes listas.
    Imprime la lista original, la lista normalizada y su suma.
    """
    ejemplos = [
        [10, 20, 30],
        [8, 2, 0],
        [0, 0, 0, 0],
        [15, 25, 35, 25],
        [1],
    ]

    for i, ejemplo in enumerate(ejemplos, 1):
        normalizada = normalizar_numeros(ejemplo)
        suma_normalizada = sum(normalizada) if normalizada else 0
        print(f"Prueba {i}:")
        print(f"Lista original: {ejemplo}")
        print(f"Lista normalizada: {normalizada}")
        print(f"Suma de elementos normalizados: {suma_normalizada}\n")


probar_normalizacion()
