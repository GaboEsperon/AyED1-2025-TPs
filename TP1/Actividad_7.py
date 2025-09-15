"""
Escribir una función diasiguiente(dia, mes año) que reciba como parámetro una
fecha cualquiera expresada por tres enteros y calcule y devuelva otros tres enteros
correspondientes el día siguiente al dado. Utilizando esta función sin modificaciones
ni agregados, desarrollar programas que permitan:

a. Sumar N días a una fecha.
b. Calcular la cantidad de días existentes entre dos fechas cualesquiera.
"""
def validar_bisiesto(anio: int) -> bool:
    """Devuelve True si el año es bisiesto."""
    return anio % 4 == 0 and (anio % 100 != 0 or anio % 400 == 0)


def dias_en_mes(mes: int, anio: int) -> int:
    """Devuelve la cantidad de días que tiene un mes de un año dado."""
    if mes == 2:
        return 29 if validar_bisiesto(anio) else 28
    dias_por_mes = (31, 30, 31, 30, 31, 31, 30, 31, 30, 31, 30, 31)
    return dias_por_mes[mes - 1]


def validar_fecha(dia: int, mes: int, anio: int) -> bool:
    """Valida que una fecha exista en el calendario."""
    if anio < 1 or mes < 1 or mes > 12 or dia < 1:
        return False
    return dia <= dias_en_mes(mes, anio)


def dia_siguiente(dia: int, mes: int, anio: int) -> tuple[int, int, int]:
    """Calcula el día siguiente a una fecha válida."""
    if not validar_fecha(dia, mes, anio):
        raise ValueError("Fecha no válida")

    if dia < dias_en_mes(mes, anio):
        return dia + 1, mes, anio
    elif mes == 12:
        return 1, 1, anio + 1
    else:
        return 1, mes + 1, anio


def sumar_n_dias(dia: int, mes: int, anio: int, n: int) -> tuple[int, int, int]:
    """Suma N días a una fecha dada."""
    for _ in range(n):
        dia, mes, anio = dia_siguiente(dia, mes, anio)
    return dia, mes, anio


def fecha_a_dias(dia: int, mes: int, anio: int) -> int:
    """Convierte una fecha a cantidad de días desde 1/1/1 (para comparar)."""
    dias_totales = dia
    for m in range(1, mes):
        dias_totales += dias_en_mes(m, anio)
    # sumar años anteriores
    for a in range(1, anio):
        dias_totales += 366 if validar_bisiesto(a) else 365
    return dias_totales


def dias_entre_fechas(dia1: int, mes1: int, anio1: int,
                      dia2: int, mes2: int, anio2: int) -> int:
    """Calcula la cantidad de días entre dos fechas."""
    return abs(fecha_a_dias(dia1, mes1, anio1) - fecha_a_dias(dia2, mes2, anio2))


def mostrar_opciones() -> None:
    """Muestra las opciones del menú al usuario."""
    opciones = [
        "Sumar N días a una fecha",
        "Calcular la cantidad de días entre dos fechas",
        "Salir"
    ]
    for count, items in enumerate(opciones, 1):
        print(f"{count} - {items}")


def menu() -> None:
    """Menú principal de la aplicación."""
    while True:
        mostrar_opciones()
        try:
            opcion = int(input("Elige una opción (1-3): "))
        except ValueError:
            print("Opción inválida, ingrese un número.")
            continue

        match opcion:
            case 1:
                try:
                    dia = int(input("Introduce el día: "))
                    mes = int(input("Introduce el mes: "))
                    anio = int(input("Introduce el año: "))
                    n = int(input("Introduce el número de días a sumar: "))
                    nuevo_dia, nuevo_mes, nuevo_anio = sumar_n_dias(dia, mes, anio, n)
                    print(f"Fecha luego de sumar {n} días: {nuevo_dia}/{nuevo_mes}/{nuevo_anio}")
                except ValueError as e:
                    print(f"Error: {e}")

            case 2:
                try:
                    dia1 = int(input("Introduce el primer día: "))
                    mes1 = int(input("Introduce el primer mes: "))
                    anio1 = int(input("Introduce el primer año: "))

                    dia2 = int(input("Introduce el segundo día: "))
                    mes2 = int(input("Introduce el segundo mes: "))
                    anio2 = int(input("Introduce el segundo año: "))

                    total_dias = dias_entre_fechas(dia1, mes1, anio1, dia2, mes2, anio2)
                    print(f"Cantidad de días entre las dos fechas: {total_dias}")
                except ValueError as e:
                    print(f"Error: {e}")

            case 3:
                print("Saliendo del programa...")
                break

            case _:
                print("Opción no válida. Intenta nuevamente.")


# Ejecución principal
if __name__ == "__main__":
    menu()