"""
Los números de claves de dos cajas fuertes están intercalados dentro de un número
entero llamado "clave maestra", cuya longitud no se conoce. Realizar un programa
para obtener ambas claves, donde la primera se construye con los dígitos ubicados
en posiciones impares de la clave maestra y la segunda con los dígitos ubicados en
posiciones pares. Los dígitos se numeran desde la izquierda. Ejemplo: Si clave
maestra fuera 18293, la clave 1 sería 123 y la clave 2 sería 89.
"""
import random as rnd

rnd.seed()


def generar_clave_maestra() -> str:
    """
    Genera una clave maestra aleatoria compuesta por entre 10 y 20 dígitos.
    """
    longitud = rnd.randint(10, 20)
    return "".join(str(rnd.randint(0, 9)) for _ in range(longitud))


def obtener_claves(clave_maestra: str) -> tuple[str, str]:
    """
    A partir de una clave maestra, obtiene las dos claves intercaladas:
    - Clave 1: dígitos en posiciones impares (1, 3, 5, ...)
    - Clave 2: dígitos en posiciones pares (2, 4, 6, ...)

    Ejemplo:
        clave_maestra = "18293"
        → clave_1 = "123"
        → clave_2 = "89"
    """
    clave_1 = ""
    clave_2 = ""

    for i, digito in enumerate(clave_maestra, start=1):  # empieza en 1
        if i % 2 != 0:  # posición impar
            clave_1 += digito
        else:  # posición par
            clave_2 += digito

    return clave_1, clave_2


def main():
    clave = generar_clave_maestra()
    clave_1, clave_2 = obtener_claves(clave)

    print(f"Clave maestra generada: {clave}")
    print(f"Clave 1 (posiciones impares): {clave_1}")
    print(f"Clave 2 (posiciones pares):   {clave_2}")


if __name__ == "__main__":
    main()