"""
Dados dos números enteros no negativos, devolver el resultado de calcular el Máximo
Común Divisor (MCD) basándose en las siguientes propiedades:

    MCD(X, X) = X
    MCD(X, Y) = MCD(Y, X)
    Si X > Y  =>  MCD(X, Y) = MCD(X - Y, Y)

Utilizando la función anterior calcular el MCD de todos los elementos de una lista de 
números enteros, sabiendo que:

    MCD(X, Y, Z) = MCD(MCD(X, Y), Z)
"""

def calcular_mcd(a, b):
    """
    Calcula el Máximo Común Divisor (MCD) entre dos enteros no negativos
    utilizando únicamente recursividad y restas sucesivas.

    Parameters:
        a (int): Primer número entero no negativo.
        b (int): Segundo número entero no negativo.

    Returns:
        int: El MCD entre a y b.
    """
    if a == b:
        return a
    if a < b:
        return calcular_mcd(b, a)
    return calcular_mcd(a - b, b)


def mcd_lista_rec(lista):
    """
    Calcula el MCD de todos los elementos de una lista de enteros no negativos
    aplicando recursividad y sin usar iteraciones.

    Parameters:
        lista (list[int]): Lista de enteros no negativos.

    Returns:
        int: El MCD de todos los elementos de la lista.
    """

    # Caso base: un solo elemento
    if len(lista) == 1:
        return lista[0]

    # Caso recursivo: aplicar MCD sobre el primer elemento y el resto de la lista
    primero = lista[0]
    resto = lista[1:]

    return calcular_mcd(primero, mcd_lista_rec(resto))
