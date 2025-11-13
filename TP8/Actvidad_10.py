"""
Desarrollar una función eliminar_claves() que reciba como parámetros un diccionario
y una lista de claves. La función debe eliminar del diccionario todas las claves
contenidas en la lista, devolviendo el diccionario modificado y un número entero
que represente la cantidad de claves eliminadas. Desarrollar también un programa
para verificar su comportamiento.
"""

def eliminar_claves(diccionario: dict, claves: list) -> tuple[dict, int]:
    """
    Elimina del diccionario las claves especificadas en una lista.

    Parameters:
        diccionario (dict): Diccionario original.
        claves (list): Lista de claves a eliminar.

    Returns:
        tuple[dict, int]:
            - Diccionario modificado.
            - Cantidad de claves eliminadas.
    """
    eliminadas = 0
    for clave in claves:
        if clave in diccionario:
            del diccionario[clave]
            eliminadas += 1
    return diccionario, eliminadas


def main():
    """
    Programa de prueba para la función eliminar_claves.
    """
    diccionario = {"a": 1, "b": 2, "c": 3, "d": 4}
    claves_a_eliminar = ["a", "c", "e"]

    print(f"Diccionario inicial: {diccionario}")
    print(f"Claves a eliminar: {claves_a_eliminar}")

    diccionario_modificado, cantidad_eliminada = eliminar_claves(
        diccionario, claves_a_eliminar
    )

    print(f"Diccionario modificado: {diccionario_modificado}")
    print(f"Cantidad de claves eliminadas: {cantidad_eliminada}")


if __name__ == "__main__":
    main()