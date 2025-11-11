"""
Desarrollar un programa que permita realizar reservas en una sala de cine de N
filas con M butacas por cada fila. Desarrollar las siguientes funciones y utilizarlas
en un mismo programa:
mostrar_butacas: Mostrará por pantalla el estado de cada una de las butacas
del cine. Esta función deberá ser invocada antes de que se realice la reserva, y
se volverá a invocar luego de la misma con los estados actualizados.
reservar: Deberá recibir una matriz y la butaca seleccionada, y actualizará la
sala en caso de estar disponible dicha butaca. La función devolverá True/False
si logró o no reservar la butaca.
cargar_sala: Recibirá una matriz como parámetro y la cargará con valores
aleatorios para simular una sala con butacas ya reservadas.
butacas_libres: Recibirá como parámetro la matriz y retornará cuántas buta-
cas desocupadas hay en la sala.
butacas_contiguas: Buscará la secuencia más larga de butacas libres conti-
guas en una misma fila y devolverá las coordenadas de inicio de la misma.
"""
import random as rnd

rnd.seed(1)


def generar_sala(filas: int, butacas: int) -> list[list[int]]:
    """
    Genera una matriz que representa la sala del cine.
    Cada elemento puede ser:
        0 → butaca libre
        1 → butaca ocupada
    """
    return [[rnd.randint(0, 1) for _ in range(butacas)] for _ in range(filas)]


def mostrar_butacas(sala: list[list[int]]) -> None:
    """
    Muestra el estado actual de las butacas.
    O = libre, X = ocupada.
    """
    print("\nEstado actual de la sala:")
    for i, fila in enumerate(sala, start=1):
        estado = " ".join("O" if b == 0 else "X" for b in fila)
        print(f"Fila {i:2}: {estado}")
    print()


def reservar_butaca(sala: list[list[int]], fila: int, butaca: int) -> bool:
    """
    Intenta reservar la butaca indicada (índices base 0).
    Retorna True si la reserva fue exitosa, False si ya estaba ocupada.
    """
    try:
        if sala[fila][butaca] == 0:
            sala[fila][butaca] = 1
            return True
        return False
    except IndexError:
        print("Error: fila o butaca fuera del rango válido.")
        return False


def contar_butacas_libres(sala: list[list[int]]) -> int:
    """Devuelve la cantidad total de butacas libres en toda la sala."""
    return sum(fila.count(0) for fila in sala)


def buscar_butacas_contiguas(sala: list[list[int]]) -> tuple[int, int, int]:
    """
    Busca la secuencia más larga de butacas contiguas libres (0) en una misma fila.
    Devuelve una tupla (fila, inicio, longitud).

    Si no hay butacas libres, devuelve (-1, -1, 0).
    """
    mejor_fila = mejor_inicio = -1
    mejor_longitud = 0

    for i, fila in enumerate(sala):
        contador = 0
        inicio_actual = 0
        for j, butaca in enumerate(fila):
            if butaca == 0:
                contador += 1
                if contador == 1:
                    inicio_actual = j
                if contador > mejor_longitud:
                    mejor_longitud = contador
                    mejor_fila = i
                    mejor_inicio = inicio_actual
            else:
                contador = 0  # se corta la secuencia

    return mejor_fila, mejor_inicio, mejor_longitud


def mostrar_opciones(lista: list[str]) -> None:
    """Muestra las opciones disponibles del menú principal."""
    print("\n--- MENÚ DE OPCIONES ---")
    for i, item in enumerate(lista, start=1):
        print(f"{i} - {item}")


def ejecutar_programa():
    """
    Programa principal: gestiona las reservas de una sala de cine.
    """
    filas = int(input("Ingrese el número de filas: "))
    butacas = int(input("Ingrese el número de butacas por fila: "))

    sala = generar_sala(filas, butacas)
    mostrar_butacas(sala)

    opciones = [
        "Mostrar estado de las butacas",
        "Reservar una butaca",
        "Ver cuántas butacas libres hay",
        "Ver secuencia más larga de butacas contiguas libres",
        "Salir",
    ]

    while True:
        mostrar_opciones(opciones)
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            mostrar_butacas(sala)

        elif opcion == "2":
            try:
                fila = int(input("Ingrese el número de fila: ")) - 1
                butaca = int(input("Ingrese el número de butaca: ")) - 1
                if reservar_butaca(sala, fila, butaca):
                    print(f"Butaca reservada en fila {fila + 1}, butaca {butaca + 1}.")
                else:
                    print("La butaca ya estaba ocupada o no existe.")
            except ValueError:
                print("Entrada inválida. Debe ingresar números enteros.")

        elif opcion == "3":
            libres = contar_butacas_libres(sala)
            print(f"Hay {libres} butacas libres en total.")

        elif opcion == "4":
            fila, inicio, largo = buscar_butacas_contiguas(sala)
            if largo > 0:
                print(
                    f"La secuencia más larga de butacas contiguas libres tiene {largo} asientos "
                    f"en la fila {fila + 1}, empezando en la butaca {inicio + 1}."
                )
            else:
                print("No hay butacas contiguas libres.")

        elif opcion == "5":
            print("Saliendo del programa...")
            break

        else:
            print("Opción no válida. Intente nuevamente.")


if __name__ == "__main__":
    ejecutar_programa()
