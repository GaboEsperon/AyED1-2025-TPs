"""
Escribir una función que devuelva la suma de los N primeros números naturales.
"""

def sumar_naturales(num):
    """
    Calcula la suma de los N primeros números naturales utilizando recursividad.

    Parameters:
        num (int): Número hasta el cual se desea sumar (debe ser >= 0).

    Returns:
        int: Suma de los N primeros números naturales.
    """
    if num < 0:
        raise ValueError("El número debe ser mayor o igual a 0.")

    if num == 0:
        return 0

    return num + sumar_naturales(num - 1)
