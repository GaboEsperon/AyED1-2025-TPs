"""
Realizar la implementación recursiva del método de selección para ordenar una lista 
de números enteros. Sugerencia: Colocar el elemento más pequeño en la primera 
posición, y luego ordenar el resto de la lista con una llamada recursiva. No usar las 
funciones min() ni max() de Python.
"""

def encontrar_menor(lista, indice=0, menor=None, pos_menor=0):
    """
    Encuentra el valor mínimo de una lista y su posición usando recursividad,
    sin utilizar min().

    Parameters:
        lista (list[int]): Lista de números enteros.
        indice (int): Índice actual en la recursión.
        menor (int): Valor mínimo encontrado hasta el momento.
        pos_menor (int): Posición del valor mínimo.

    Returns:
        tuple: (menor_valor, posicion_del_menor)
    """

    # Inicializar menor en la primera llamada
    if menor is None:
        menor = lista[0]
        pos_menor = 0

    # Caso base: fin de la lista
    if indice == len(lista):
        return menor, pos_menor

    # Actualizar si encontramos un elemento menor
    if lista[indice] < menor:
        menor = lista[indice]
        pos_menor = indice

    return encontrar_menor(lista, indice + 1, menor, pos_menor)


def ordenar_seleccion_rec(lista):
    """
    Ordena una lista de números enteros usando el método de selección
    implementado de forma recursiva.

    Parameters:
        lista (list[int]): Lista de números enteros a ordenar.

    Returns:
        list[int]: Nueva lista ordenada en forma ascendente.
    """

    # Caso base: lista vacía o de un solo elemento
    if len(lista) <= 1:
        return lista

    # Encontrar el mínimo manualmente
    menor, pos = encontrar_menor(lista)

    # Colocar el menor al inicio
    resto = lista[:pos] + lista[pos+1:]

    # Recursión sobre el resto de la lista
    return [menor] + ordenar_seleccion_rec(resto)
