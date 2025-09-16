"""
La siguiente función permite averiguar el día de la semana para una fecha determi-
nada. La fecha se suministra en forma de tres parámetros enteros y la función de-
vuelve 0 para domingo, 1 para lunes, 2 para martes, etc. Escribir un programa para
imprimir por pantalla el calendario de un mes completo, correspondiente a un mes
y año cualquiera basándose en la función suministrada. Considerar que la semana
comienza en domingo.
"""
def diadelasemana(dia: int, mes: int, anio: int) -> bool:
    """
    Verifica si una fecha es válida teniendo en cuenta el día, mes y año proporcionados.
    """
    if mes < 3:
        mes = mes + 10
        año = anio - 1
    else:
        mes = mes - 2
        siglo = año // 100
        año2 = anio % 100
        diasem = (((26*mes-2)//10)+dia+año2+(año2//4)+(siglo//4)-(2*siglo))%7
    if diasem < 0:
        diasem = diasem + 7
        return diasem

def dias_en_mes(mes: int, anio: int) -> int:
    """Devuelve el número de días de un mes y año específico."""
    if mes in (1, 3, 5, 7, 8, 10, 12):
        return 31
    elif mes in (4, 6, 9, 11):
        return 30
    elif mes == 2:
        return 29 if validar_bisiesto(anio) else 28
    return 0

def validar_fecha(dia: int, mes: int, anio: int) -> bool:
    """Valida que una fecha exista en el calendario."""
    if anio < 1 or mes < 1 or mes > 12 or dia < 1:
        return False
    return dia <= dias_en_mes(mes, anio)

def validar_bisiesto(anio: int) -> bool:
    """Devuelve True si el año es bisiesto."""
    return anio % 4 == 0 and (anio % 100 != 0 or anio % 400 == 0)

def imprimir_calendario(mes: int, anio: int) -> None:
    """
    Imprime el calendario de un mes específico en formato semanal.
    """
    print(f"\nCalendario para {mes}/{anio}")
    print("Do  Lu  Ma  Mi  Ju  Vi  Sa")

    primer_dia = diadelasemana(1, mes, anio)

    # Espacios iniciales
    for _ in range(primer_dia):
        print("    ", end="")

    for dia in range(1, dias_en_mes(mes, anio) + 1):
        print(f"{dia:2}  ", end="")
        if (primer_dia + dia) % 7 == 0:
            print()

    print()

def main() -> None:
    """
    Ejecuta la aplicación para imprimir un calendario mensual.
    Solicita el mes y año al usuario y valida si es una fecha válida antes de imprimir el calendario.
    """
    mes_input = int(input("Introduce el mes (1-12): "))
    anio_input = int(input("Introduce el año: "))

    if validar_fecha(1, mes_input, anio_input):
        imprimir_calendario(mes_input, anio_input)
    else:
        print("Fecha inválida. Por favor, introduce un mes y año válidos.")

main()
