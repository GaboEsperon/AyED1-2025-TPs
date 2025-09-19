"""
Desarrollar cada una de las siguientes funciones y escribir un programa que permi-
ta verificar su funcionamiento, imprimiendo la matriz luego de invocar a cada fun-
ción:
a. Cargar números enteros en una matriz de N x N, ingresando los datos desde
teclado.
b. Ordenar en forma ascendente cada una de las filas de la matriz.
c. Intercambiar dos filas, cuyos números se reciben como parámetro.
d. Intercambiar dos columnas dadas, cuyos números se reciben como parámetro.
e. Trasponer la matriz sobre si misma. (intercambiar cada elemento A por A )
f. Calcular el promedio de los elementos de una fila, cuyo número se recibe como
parámetro.
g. Calcular el porcentaje de elementos con valor impar en una columna, cuyo nú-
mero se recibe como parámetro.
h. Determinar si la matriz es simétrica con respecto a su diagonal principal.
i. Determinar si la matriz es simétrica con respecto a su diagonal secundaria.
j. Determinar qué columnas de la matriz son palíndromos (capicúas), devolviendo
una lista con los números de las mismas.
NOTA: El valor de N debe leerse por teclado. Las funciones deben servir cualquiera
sea el valor ingresado.
"""
def cargar_matriz(n: int) -> list[list[int]]:
    """Carga una matriz NxN con valores ingresados por el usuario."""
    return [
        [int(input(f"Ingrese elemento [{i+1},{j+1}]: ")) for j in range(n)]
        for i in range(n)
    ]


def ordenar_filas(matriz: list[list[int]]) -> list[list[int]]:
    """Ordena cada fila de la matriz en orden ascendente."""
    for fila in matriz:
        fila.sort()
    return matriz


def es_valido(indice: int, n: int) -> bool:
    """Valida que un índice esté dentro del rango de la matriz."""
    return 0 <= indice < n


def intercambiar_filas(matriz: list[list[int]], fila1: int, fila2: int) -> None:
    """Intercambia dos filas de la matriz."""
    matriz[fila1], matriz[fila2] = matriz[fila2], matriz[fila1]


def intercambiar_columnas(matriz: list[list[int]], col1: int, col2: int) -> None:
    """Intercambia dos columnas de la matriz."""
    for fila in matriz:
        fila[col1], fila[col2] = fila[col2], fila[col1]


def transponer(matriz: list[list[int]]) -> None:
    """Transpone la matriz en sitio."""
    n = len(matriz)
    for i in range(n):
        for j in range(i + 1, n):
            matriz[i][j], matriz[j][i] = matriz[j][i], matriz[i][j]


def promedio_fila(matriz: list[list[int]], fila_indice: int) -> float:
    """Calcula el promedio de los elementos de una fila específica."""
    fila = matriz[fila_indice]
    return sum(fila) / len(fila) if fila else 0


def porcentaje_impares(matriz: list[list[int]], col_indice: int) -> float:
    """Calcula el porcentaje de elementos impares en una columna específica."""
    n = len(matriz)
    if n == 0:
        return 0
    total_impares = sum(1 for fila in matriz if fila[col_indice] % 2 != 0)
    return (total_impares / n) * 100


def es_simetrica_principal(matriz: list[list[int]]) -> bool:
    """Verifica si la matriz es simétrica respecto a la diagonal principal."""
    n = len(matriz)
    return all(matriz[i][j] == matriz[j][i] for i in range(n) for j in range(n))


def es_simetrica_secundaria(matriz: list[list[int]]) -> bool:
    """Verifica si la matriz es simétrica respecto a la diagonal secundaria."""
    n = len(matriz)
    return all(matriz[i][j] == matriz[n - 1 - j][n - 1 - i] for i in range(n) for j in range(n))


def columna_capicua(columna: list[int]) -> bool:
    """Verifica si una columna es capicúa."""
    return columna == columna[::-1]


def columnas_capicuas(matriz: list[list[int]]) -> list[int]:
    """Devuelve los índices de las columnas que son capicúas."""
    n = len(matriz)
    resultado = []
    for col in range(n):
        if columna_capicua([fila[col] for fila in matriz]):
            resultado.append(col)
    return resultado


def mostrar_matriz(matriz: list[list[int]]) -> None:
    """Imprime la matriz."""
    for fila in matriz:
        print(fila)


def main():
    while True:
        try:
            n = int(input("Ingrese tamaño N de la matriz NxN: "))
            if n > 0:
                break
        except ValueError:
            print("Debe ingresar un número entero positivo.")

    matriz = cargar_matriz(n)
    mostrar_matriz(matriz)

    ordenar_filas(matriz)
    mostrar_matriz(matriz)

    fila1 = int(input("Ingrese fila a intercambiar: "))
    fila2 = int(input("Ingrese otra fila: "))
    if es_valido(fila1, n) and es_valido(fila2, n):
        intercambiar_filas(matriz, fila1, fila2)
        mostrar_matriz(matriz)

    col1 = int(input("Ingrese columna a intercambiar: "))
    col2 = int(input("Ingrese otra columna: "))
    if es_valido(col1, n) and es_valido(col2, n):
        intercambiar_columnas(matriz, col1, col2)
        mostrar_matriz(matriz)

    transponer(matriz)
    mostrar_matriz(matriz)

    fila_op = int(input("Ingrese fila para calcular promedio: "))
    if es_valido(fila_op, n):
        print(f"Promedio fila {fila_op}: {promedio_fila(matriz, fila_op)}")

    col_op = int(input("Ingrese columna para porcentaje de impares: "))
    if es_valido(col_op, n):
        print(f"Porcentaje de impares columna {col_op}: {porcentaje_impares(matriz, col_op):.2f}%")

    print(f"Simétrica principal: {es_simetrica_principal(matriz)}")
    print(f"Simétrica secundaria: {es_simetrica_secundaria(matriz)}")
    print(f"Columnas capicúas: {columnas_capicuas(matriz)}")


if __name__ == "__main__":
    main()
