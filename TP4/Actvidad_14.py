"""
Se solicita crear un programa para leer direcciones de correo electrónico y verificar
si representan una dirección válida. Por ejemplo usuario@dominio.com.ar. Para que
una dirección sea considerada válida el nombre de usuario debe poseer solamente
caracteres alfanuméricos, la dirección contener un solo carácter @, el dominio debe
tener al menos un carácter y tiene que finalizar con .com o .com.ar.
Repetir el proceso de validación hasta ingresar una cadena vacía. Al finalizar mos-
trar un listado de todos los dominios, sin repetirlos y ordenados alfabéticamente,
recordando que las direcciones de mail no distinguen mayúsculas ni minúsculas.
"""
import re

def correo_valido(correo: str) -> bool:
    """
    Verifica si una dirección de correo electrónico es válida.

    Condiciones:
        - El nombre de usuario es alfanumérico (puede incluir '.' o '_')
        - Solo un carácter '@'
        - El dominio tiene al menos un carácter válido
        - Finaliza con '.com' o '.com.ar'

    Args:
        correo (str): dirección de correo a verificar.

    Returns:
        bool: True si es válida, False en caso contrario.
    """
    patron = r"^[a-zA-Z0-9._]+@[a-zA-Z0-9.-]+\.(com|com\.ar)$"
    return bool(re.fullmatch(patron, correo))


def sacar_dominio(correo: str) -> str:
    """
    Extrae el dominio del correo electrónico.

    Args:
        correo (str): dirección de correo.

    Returns:
        str: el dominio sin el nombre de usuario.
    """
    return correo.split("@")[1]


def main():
    """
    Programa principal: solicita correos, los valida y muestra dominios únicos.
    """
    dominios: set[str] = set()

    print("Validador de correos electrónicos")
    print("Ingrese direcciones de correo (Enter para finalizar)\n")

    while True:
        mail = input("Correo: ").strip().lower()
        if mail == "":
            break

        if correo_valido(mail):
            print(f"'{mail}' es un correo válido.\n")
            dominios.add(sacar_dominio(mail))
        else:
            print(f"'{mail}' no es válido. Intente nuevamente.\n")

    if dominios:
        print("\n DOMINIOS VÁLIDOS ORDENADOS ALFABÉTICAMENTE:\n")
        for dominio in sorted(dominios):
            print(f" - {dominio}")
    else:
        print("\n No se ingresaron dominios válidos.")




if __name__ == "__main__":
    main()
