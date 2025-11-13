"""
Realizar una función que reciba como parámetros dos cadenas de caracteres con-
teniendo números reales, sume ambos valores y devuelva el resultado como un
número real. Devolver -1 si alguna de las cadenas no contiene un número válido,
utilizando manejo de excepciones para detectar el error.
"""
def sumar_reales_desde_cadenas(cadena_uno: str, cadena_dos: str) -> float:
    """
    Suma dos cadenas de caracteres que representan números reales.

    Parameters:
        cadena_uno (str): Primera cadena con un número real.
        cadena_dos (str): Segunda cadena con un número real.

    Returns:
        float: La suma de los dos números o -1 si alguna cadena no puede convertirse.
    """
    try:
        num_uno = float(cadena_uno)
        num_dos = float(cadena_dos)
        return num_uno + num_dos
    except ValueError:
        return -1


cadena_uno = input("Ingrese la primera cadena numérica: ")
cadena_dos = input("Ingrese la segunda cadena numérica: ")

resultado = sumar_reales_desde_cadenas(cadena_uno, cadena_dos)
print(f"Resultado: {resultado}")
