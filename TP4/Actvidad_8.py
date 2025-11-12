"""
Desarrollar una función que devuelva una subcadena con los últimos N caracteres
de una cadena dada. La cadena y el valor de N se pasan como parámetros.
"""
def ultimos_caracteres(cadena: str, n: int) -> str:
    """
    Devuelve los últimos N caracteres de una cadena.

    Parámetros:
        cadena (str): cadena original
        n (int): cantidad de caracteres a extraer desde el final

    Retorna:
        str: los últimos N caracteres, o cadena vacía si N es inválido.

    """
    if n <= 0:
        return "" 
    return cadena[-n:]


def main():
    """
    Programa de prueba para la función ultimos_caracteres().
    """
    string = "El acero se templa en el fuego, y el carácter en la adversidad."
    print(f"Cadena original:\n{string}\n")

    try:
        num = int(input("Ingrese N (cantidad de caracteres a mostrar desde el final): "))
        resultado = ultimos_caracteres(string, num)
        print(f"\nÚltimos {num} caracteres: '{resultado}'")
    except ValueError:
        print("Error: debe ingresar un número entero.")


if __name__ == "__main__":
    main()
