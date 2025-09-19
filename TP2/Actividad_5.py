"""
Escribir una función que reciba una lista como parámetro y devuelva True si la lista
está ordenada en forma ascendente o False en caso contrario. Por ejemplo,
ordenada([1, 2, 3]) retorna True y ordenada(['b', 'a']) retorna False. Desarrollar
además un programa para verificar el comportamiento de la función.
"""
import random as rnd

rnd.seed(1)


def esta_ordenada(lista: list) -> bool:
    """
    Verifica si una lista está ordenada de forma ascendente.

    Parámetros:
        lista (list): Lista de elementos comparables (números o letras).

    Retorna:
        bool: True si la lista está ordenada ascendentemente, False en caso contrario.
    """
    return all(lista[i] <= lista[i + 1] for i in range(len(lista) - 1))


def generar_listas_prueba(tam: int = 10):
    """
    Genera listas de prueba ordenadas y desordenadas, tanto de números como de letras.

    Parámetros:
        tam (int): Tamaño de las listas.

    Retorna:
        tuple: Cuatro listas (ordenadas_numeros, desordenadas_numeros, ordenadas_letras, desordenadas_letras)
    """
    letras = [chr(97 + i) for i in range(tam)]
    ordenadas_numeros = list(range(1, tam + 1))
    desordenadas_numeros = [rnd.randint(1, tam) for _ in range(tam)]
    ordenadas_letras = letras.copy()
    desordenadas_letras = letras.copy()
    rnd.shuffle(desordenadas_letras)

    return ordenadas_numeros, desordenadas_numeros, ordenadas_letras, desordenadas_letras


def probar_funcion_orden():
    """Prueba la función esta_ordenada con listas de números y letras."""
    lista_orden_num, lista_desorden_num, lista_orden_letras, lista_desorden_letras = generar_listas_prueba()

    print("Lista ordenada de números:", lista_orden_num)
    print("Lista desordenada de números:", lista_desorden_num)
    print("Lista ordenada de letras:", lista_orden_letras)
    print("Lista desordenada de letras:", lista_desorden_letras)

    print("\nResultados de la función esta_ordenada:")
    print(f"Lista ordenada de números: {esta_ordenada(lista_orden_num)}")
    print(f"Lista desordenada de números: {esta_ordenada(lista_desorden_num)}")
    print(f"Lista ordenada de letras: {esta_ordenada(lista_orden_letras)}")
    print(f"Lista desordenada de letras: {esta_ordenada(lista_desorden_letras)}")


if __name__ == "__main__":
    probar_funcion_orden()
