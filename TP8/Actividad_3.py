"""
Desarrollar un programa que utilice una función que reciba como parámetro una
cadena de caracteres conteniendo una dirección de correo electrónico y devuelva
una tupla con las distintas partes que componen dicha dirección. Ejemplo:
alguien@uade.edu.ar -> (alguien, uade, edu, ar). La función debe detectar
formatos de fecha inválidos y devolver una tupla vacía.
"""
import re

def descomponer_correo(correo: str) -> tuple[str, ...]:
    """
    Descompone una dirección de correo electrónico válida en sus partes:
    usuario, dominio y subdominios.

    Parameters:
        correo (str): Dirección de correo electrónico.

    Returns:
        tuple: Una tupla (usuario, dominio, subdominios...).
               Si el formato es inválido, retorna una tupla vacía.
    """
    # Patrón más estricto: usuario@dominio.subdominio
    patron = r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"

    if not re.match(patron, correo):
        return ()

    try:
        usuario, resto = correo.split("@")
        partes_dominio = resto.split(".")
        return (usuario, *partes_dominio)
    except ValueError:
        return ()
    

def main():
    """
    Programa principal: solicita un correo y muestra sus partes.
    """
    correo = input("Ingrese una dirección de correo electrónico: ").strip()
    partes = descomponer_correo(correo)

    if partes:
        print("Las partes de la dirección son:", partes)
    else:
        print("La dirección de correo electrónico es inválida.")


if __name__ == "__main__":
    main()
