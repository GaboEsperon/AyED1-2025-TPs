"""
Desarrollar una función que devuelva una cadena de caracteres con el nombre del
mes cuyo número se recibe como parámetro. Los nombres de los meses deberán
obtenerse de una lista de cadenas de caracteres inicializada dentro de la función.
Devolver una cadena vacía si el número de mes es inválido. La detección de meses
inválidos deberá realizarse a través de excepciones.
"""
def numero_a_mes(num: int) -> str:
    """
    Devuelve el nombre del mes correspondiente al número dado.

    Parameters:
        num (int): Número del mes (1-12).

    Returns:
        str: Nombre del mes si el número es válido, o una cadena vacía si no lo es.
    """
    meses = [
        "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
        "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"
    ]

    try:
        return meses[int(num) - 1]
    except (ValueError, IndexError):
        return ""
