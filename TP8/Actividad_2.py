"""
Escribir una función que reciba como parámetro una tupla conteniendo una fecha
(día,mes,año) y devuelva una cadena de caracteres con la misma fecha expresada
en formato extendido. La función debe contemplarse que el año se ingrese en dos
dígitos, los que serán interpretados según un año de corte definido dentro del
programa. Cualquier año mayor que éste se considerará del siglo pasado. Por
ejemplo, si el año de corte fuera 30, la función devuelve "12 de Octubre de 2030"
para (12,10,30). Pero si la tupla fuera (25, 12, 31) devolverá "25 de Diciembre de
1931". Si el año se ingresa en cuatro dígitos el año de corte no será tenido en
cuenta. Escribir también un programa para ingresar los datos, invocar a la función y
mostrar el resultado.
"""
from datetime import datetime

# Lista de nombres de meses (fuera de la función)
MESES = [
    "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
    "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"
]

ANIO_CORTE = 30  # Años mayores a 30 se consideran del siglo XX


def fecha_a_texto(fecha: tuple[int, int, int], corte: int = ANIO_CORTE) -> str:
    """
    Convierte una fecha (día, mes, año) a formato extendido.
    Si el año tiene dos dígitos, usa el año de corte para determinar el siglo.
    """
    dia, mes, anio = fecha

    if anio < 100:  # Año en dos dígitos
        anio = 2000 + anio if anio <= corte else 1900 + anio

    return f"{dia} de {MESES[mes - 1]} de {anio}"


def main():
    """
    Programa principal: pide una fecha, la valida y muestra su formato extendido.
    """
    fecha_input = input("Ingrese una fecha (DD/MM/AA o DD/MM/AAAA): ").strip()

    try:
        dia, mes, anio = map(int, fecha_input.split("/"))

        # Aplicar año de corte antes de validar
        anio_real = anio
        if anio < 100:
            anio_real = 2000 + anio if anio <= ANIO_CORTE else 1900 + anio

        # Validar la fecha real
        datetime(anio_real, mes, dia)

        texto = fecha_a_texto((dia, mes, anio), ANIO_CORTE)
        print("Fecha en formato extendido:", texto)

    except ValueError:
        print("Fecha inválida. Asegúrese de ingresar DD/MM/AA o DD/MM/AAAA válida.")


if __name__ == "__main__":
    main()
