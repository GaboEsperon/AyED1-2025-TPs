"""
Escribir una función que devuelva la cantidad de dígitos de un número entero,
sin utilizar cadenas de caracteres.
"""

def calcular_total_digitos(numero: int) -> int:
    """
    Función recursiva que devuelve la cantidad de dígitos de un número entero,
    positivo o negativo, sin convertirlo en cadena.

    Parameters:
        numero (int): El número entero cuyo total de dígitos se desea calcular.

    Returns:
        int: Cantidad de dígitos que posee el número.
    """
    numero = abs(numero)

    if numero < 10:
        return 1
    return 1 + calcular_total_digitos(numero // 10)