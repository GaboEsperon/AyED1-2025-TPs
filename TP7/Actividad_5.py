"""
Realizar una función que devuelva el resto de dos números enteros,
utilizando restas sucesivas y aplicando recursividad.
"""

def calcular_resto_recursivo(dividendo, divisor):
    """
    Calcula el resto de la división entre dos números enteros mediante restas sucesivas
    utilizando recursividad.

    Parameters:
        dividendo (int): Número a dividir.
        divisor (int): Número divisor (distinto de 0).

    Returns:
        int: El resto de la división entre dividendo y divisor.
    """

    if divisor == 0:
        raise ValueError("El divisor no puede ser 0.")

    # Manejo de signos
    abs_dividendo = abs(dividendo)
    abs_divisor = abs(divisor)

    # Caso base: cuando el dividendo ya es menor que el divisor
    if abs_dividendo < abs_divisor:
        return abs_dividendo if dividendo >= 0 else -abs_dividendo

    # Caso recursivo: restar el divisor y continuar
    return calcular_resto_recursivo(abs_dividendo - abs_divisor, abs_divisor)
