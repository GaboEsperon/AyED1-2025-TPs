""" 
Las siguientes matrices responden distintos patrones de relleno. Desarrollar funcio
nes que generen cada una de ellas sin intervención humana y escribir un programa 
que las invoque e imprima por pantalla. El tamaño de las matrices debe estable
cerse como N x N, donde N se ingresa a través del teclado.
"""

def matriz_a(n: int) -> list[list[int]]:
    """
    Genera una matriz con la diagonal principal formada por números impares crecientes.
    """
    return [[2 * i + 1 if i == j else 0 for j in range(n)] for i in range(n)]


def matriz_b(n: int) -> list[list[int]]:
    """
    Genera una matriz con la diagonal secundaria formada por divisiones sucesivas de 27 entre 3.
    """
    return [[27 // (3 ** i) if j == n - 1 - i else 0 for j in range(n)] for i in range(n)]


def matriz_c(n: int) -> list[list[int]]:
    """
    Genera una matriz donde cada fila i tiene valores decrecientes a partir de la diagonal principal.
    """
    return [[(n - j) if j >= i else 0 for j in range(n)] for i in range(n)]


def matriz_d(n: int) -> list[list[int]]:
    """
    Genera una matriz donde todas las filas repiten la secuencia de valores: 8, 4, 2, 1,...
    """
    return [[8 // (2 ** j) for j in range(n)] for _ in range(n)]


def matriz_e(n: int) -> list[list[int]]:
    """
    Genera una matriz con valores crecientes en posiciones alternadas (según paridad de i+j).
    """
    valor = 0
    return [[(valor := valor + 1) if (i + j) % 2 == 1 else 0 for j in range(n)] for i in range(n)]


def matriz_f(n: int) -> list[list[int]]:
    """
    Genera una matriz con la diagonal secundaria formada por números crecientes desde 1 hasta N.
    """
    valor = 0
    matriz = []
    for i in range(n):
        fila = []
        for j in range(n):
            if j == n - 1 - i:
                valor += 1
                fila.append(valor)
            else:
                fila.append(0)
        matriz.append(fila)
    return matriz


def show_matriz(matriz: list[list[int]]):
    """Muestra una matriz en formato cuadrado en la terminal."""
    for fila in matriz:
        print(" ".join(str(x) for x in fila))
    print()


def matriz_g(n: int) -> list[list[int]]:
    """
    Genera una matriz con dos patrones:
      - La primera fila contiene números crecientes desde 1 hasta N.
      - La primera columna contiene números crecientes desde 1 hasta N.
      - El resto de la matriz se completa de forma creciente en bloques,
        siguiendo la estructura del ejemplo de la guía.
    """
    matriz = [[0] * n for _ in range(n)]
    valor = 1
    inicio, fin = 0, n - 1

    while inicio <= fin:
        # Lado superior (izq -> der)
        for j in range(inicio, fin + 1):
            matriz[inicio][j] = valor
            valor += 1
        # Lado derecho (arriba -> abajo)
        for i in range(inicio + 1, fin + 1):
            matriz[i][fin] = valor
            valor += 1
        # Lado inferior (der -> izq)
        for j in range(fin - 1, inicio - 1, -1):
            matriz[fin][j] = valor
            valor += 1
        # Lado izquierdo (abajo -> arriba)
        for i in range(fin - 1, inicio, -1):
            matriz[i][inicio] = valor
            valor += 1
        inicio += 1
        fin -= 1

    return matriz


def matriz_h(n: int) -> list[list[int]]:
    """
    Genera una matriz con números consecutivos dispuestos por columnas (de arriba hacia abajo).
    """
    matriz = [[0] * n for _ in range(n)]
    valor = 1
    for j in range(n):
        for i in range(n):
            matriz[i][j] = valor
            valor += 1
    return matriz


def matriz_i(n: int) -> list[list[int]]:
    """
    Genera una matriz con números consecutivos dispuestos por filas (de izquierda a derecha).
    """
    matriz = [[0] * n for _ in range(n)]
    valor = 1
    for i in range(n):
        for j in range(n):
            matriz[i][j] = valor
            valor += 1
    return matriz


if __name__ == "__main__":
    try:
        n = int(input("Ingrese el tamaño N de la matriz: "))

        print("MATRIZ A")
        show_matriz(matriz_a(n))

        print("MATRIZ B")
        show_matriz(matriz_b(n))

        print("MATRIZ C")
        show_matriz(matriz_c(n))

        print("MATRIZ D")
        show_matriz(matriz_d(n))

        print("MATRIZ E")
        show_matriz(matriz_e(n))

        print("MATRIZ F")
        show_matriz(matriz_f(n))
        
        print("MATRIZ G")
        show_matriz(matriz_g(n))

        print("MATRIZ H")
        show_matriz(matriz_h(n))

        print("MATRIZ I")
        show_matriz(matriz_i(n))
    
    except ValueError:
        print("Debe ingresar un número entero válido.")
