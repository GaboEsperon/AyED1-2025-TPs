"""
Escribir un programa que permita ingresar un número entero N y genere un
diccionario por comprensión con la tabla de multiplicar de N del 1 al 12. Mostrar la
tabla de multiplicar con el formato apropiado.
"""
def generar_tabla_multiplicar(num: int) -> dict:
    """
    Genera un diccionario que representa la tabla de multiplicar de un número dado.
    
    Parameters:
        num (int): Número para el cual se genera la tabla de multiplicar.

    Returns:
        dict: Diccionario cuyas claves van del 1 al 12 y cuyos valores son num * clave.
    """
    return {i: num * i for i in range(1, 13)}


def main():
    """
    Programa principal: solicita un número entero, genera su tabla y la muestra.
    """
    try:
        numero = int(input("Ingrese un número entero: "))
        tabla = generar_tabla_multiplicar(numero)

        print(f"Tabla de multiplicar del {numero}:")
        for i in range(1, 13):
            print(f"{i} x {numero} = {tabla[i]}")

    except ValueError:
        print("Debe ingresar un número entero.")


if __name__ == "__main__":
    main()
