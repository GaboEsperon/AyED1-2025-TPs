"""
Desarrollar un programa para rellenar una matriz de N x N con números enteros al
azar comprendidos en el intervalo [0,N2), de tal forma que ningún número se repi-
ta. Imprimir la matriz por pantalla.
"""
import random as rnd

def generar_matriz_aleatoria() -> list[list[int]]:
    """
    Genera una matriz cuadrada N x N con números enteros únicos del 0 al N^2-1.
    Los números se mezclan aleatoriamente.
    """
    while True:
        try:
            n = int(input("Ingrese el tamaño N para la matriz NxN: "))
            if n > 0:
                break
            else:
                print("El tamaño debe ser un número entero positivo.")
        except ValueError:
            print("Entrada inválida. Ingrese un número entero.")

    numeros_disponibles = list(range(n**2))
    rnd.shuffle(numeros_disponibles)

    matriz = []
    for i in range(n):
        fila = numeros_disponibles[i * n:(i + 1) * n]
        matriz.append(fila)

    return matriz


def mostrar_matriz(matriz: list[list[int]]) -> None:
    """
    Imprime la matriz de forma legible, mostrando cada fila en una línea.
    """
    for fila in matriz:
        print(fila)


def main():
    matriz = generar_matriz_aleatoria()
    print("\nMatriz generada aleatoriamente:")
    mostrar_matriz(matriz)


if __name__ == "__main__":
    main()
