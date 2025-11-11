"""
Leer una cadena de caracteres e imprimirla centrada en pantalla. Suponer que la
misma tiene 80 columnas.
"""
def centrar_cadena(cadena: str) -> None:
    columnas = 80
    long = len(cadena)

    espacios_izquierda = (columnas - long) // 2
    cadena_centrada = ' ' * espacios_izquierda + cadena

    print(cadena_centrada)

centrar_cadena("lore ipsum")