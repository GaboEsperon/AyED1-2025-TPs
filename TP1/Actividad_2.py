"""
Desarrollar una función que reciba tres números enteros positivos correspondientes al día, mes, año de una fecha 
y verifique si corresponden a una fecha válida.
Debe tenerse en cuenta la cantidad de días de cada mes, incluyendo los años bisiestos.
Devolver True o False según la fecha sea correcta o no.
Realizar también un programa para verificar el comportamiento de la función.
"""
def recibir_fecha() -> tuple[int, int, int]:
    """
    Solicita al usuario ingresar una fecha (día, mes y año) y valida que sean enteros.

    Retorna:
        tuple[int, int, int]: Una tupla con el día, mes y año ingresados.
    """
    while True:
        try:
            dia = int(input("Ingrese el día: "))
            mes = int(input("Ingrese el mes: "))
            anio = int(input("Ingrese el año: "))
            return dia, mes, anio
        except ValueError:
            print("Error: los números ingresados deben ser enteros.")


def validar_bisiesto(anio: int) -> bool:
    """
    Determina si un año es bisiesto.

    Parámetros:
        anio (int): Año a evaluar.

    Retorna:
        bool: True si el año es bisiesto, False en caso contrario.
    """
    return anio % 4 == 0 and (anio % 100 != 0 or anio % 400 == 0)


def validar_fecha(dia: int, mes: int, anio: int) -> bool:
    """
    Valida si una fecha es correcta considerando días, meses y años bisiestos.

    Parámetros:
        dia (int): Día de la fecha.
        mes (int): Mes de la fecha.
        anio (int): Año de la fecha.

    Retorna:
        bool: True si la fecha es válida, False si es inválida.
    """
    if dia < 1 or mes < 1 or anio < 1:
        return False
    if mes > 12:
        return False

    es_bisiesto = validar_bisiesto(anio)
    dias_por_mes = (
        31,
        29 if es_bisiesto else 28,
        31,
        30,
        31,
        30,
        31,
        31,
        30,
        31,
        30,
        31
    )

    if dia > dias_por_mes[mes - 1]:
        return False

    return True


def main():
    """
    Función principal que solicita una fecha al usuario, valida si es correcta
    y muestra el resultado por pantalla.
    """
    dia, mes, anio = recibir_fecha()
    if validar_fecha(dia, mes, anio):
        print("La fecha es válida.")
    else:
        print("La fecha es inválida.")


if __name__ == "__main__":
    main()
