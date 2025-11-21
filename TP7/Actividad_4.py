"""
Desarrollar una función que devuelva el producto de dos números enteros 
por sumas sucesivas, utilizando recursividad.
"""

def multiplicar_sumas_recursivas(x, y):
    """
    Calcula el producto de dos números enteros usando sumas sucesivas de forma recursiva.

    Parameters:
        x (int): Primer número.
        y (int): Segundo número.

    Returns:
        int: Producto de x e y calculado mediante sumas sucesivas.
    """

    # Manejo del signo
    if y < 0:
        return -multiplicar_sumas_recursivas(x, -y)

    # Caso base
    if y == 0:
        return 0

    # Caso recursivo
    return x + multiplicar_sumas_recursivas(x, y - 1)
