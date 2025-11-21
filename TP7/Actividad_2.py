"""
Desarrollar una función que reciba un número binario y lo devuelva convertido 
a base decimal.
"""

def convertir_binario_decimal(valor_bin, pot=0) -> int:
    """
    Convierte un número binario a base decimal utilizando recursividad.

    Parameters:
        valor_bin (int): Número binario a convertir.
        pot (int): Exponente para calcular potencias de 2 durante la recursión.

    Returns:
        int: Número equivalente en base decimal.
    """

    if valor_bin == 0:
        return 0
    
    dig = valor_bin % 10
    return dig * (2 ** pot) + convertir_binario_decimal(valor_bin // 10, pot + 1)
