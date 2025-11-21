"""
La función de Ackermann A(m,n) se define de la siguiente forma:

    A(0, n)       = n + 1
    A(m, 0)       = A(m - 1, 1)
    A(m, n)       = A(m - 1, A(m, n - 1))

Imprimir un cuadro con los valores que adopta la función para valores de m entre 0 y 3
y de n entre 0 y 7.
"""

def funcion_ack(m, n):
    """
    Calcula la función de Ackermann utilizando recursividad.

    Parameters:
        m (int): Parámetro m de la función de Ackermann (>= 0).
        n (int): Parámetro n de la función de Ackermann (>= 0).

    Returns:
        int: Resultado de A(m,n) según su definición recursiva.
    """
    if m == 0:
        return n + 1
    if n == 0:
        return funcion_ack(m - 1, 1)
    return funcion_ack(m - 1, funcion_ack(m, n - 1))


def imprimir_tabla_ack():
    """
    Imprime un cuadro con los valores de la función de Ackermann
    para m entre 0 y 3 y n entre 0 y 7.
    """
    for m in range(0, 4):
        fila = []
        for n in range(0, 8):
            fila.append(funcion_ack(m, n))
        print(f"m = {m}: {fila}")



imprimir_tabla_ack()