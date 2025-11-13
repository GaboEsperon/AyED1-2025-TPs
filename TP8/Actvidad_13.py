"""
Escribir una función buscarclave() que reciba como parámetros un diccionario y un
valor, y devuelva una lista de claves que apunten a ese valor. Comprobar el
comportamiento mediante un programa apropiado.
"""

from typing import Any, List

def encontrar_claves_por_valor(diccionario: dict, valor: Any) -> List:
    """
    Devuelve una lista de claves que mapean al valor indicado.

    Parameters:
        diccionario (dict): Diccionario donde se buscarán las claves.
        valor (Any): Valor a buscar en el diccionario.

    Returns:
        list: Lista de claves que tienen asociado el valor indicado.
    """
    return [clave for clave, v in diccionario.items() if v == valor]


diccionario_valores = {
    'a': 10,
    'b': 20,
    'c': 10,
    'd': 30,
    'e': 20
}

valor_buscado = 10
claves_encontradas = encontrar_claves_por_valor(diccionario_valores, valor_buscado)

print(f"Las claves que mapean al valor {valor_buscado} son: {claves_encontradas}")
