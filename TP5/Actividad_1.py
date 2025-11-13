"""
Desarrollar una función para ingresar a través del teclado un número natural. La
función rechazará cualquier ingreso inválido de datos utilizando excepciones y
mostrará la razón exacta del error. Controlar que se ingrese un número, que ese
número sea entero y que sea mayor que 0, mostrando un mensaje con la razón
exacta del error en caso necesario. Devolver el valor ingresado cuando éste sea
correcto. Escribir también un programa que permita probar el correcto funciona-
miento de la misma.
"""
def leer_numero_natural() -> int:
    """
    Solicita al usuario un número natural (entero mayor que 0), validando el ingreso.

    Returns:
        int: El número natural ingresado correctamente.
    """
    while True:
        try:
            entrada = input("Ingrese un número natural: ")
            numero = int(entrada)

            if numero <= 0:
                raise ValueError("El número debe ser mayor que 0.")

            return numero

        except ValueError as e:
            print(f"Error: {e}")


def main():
    numero = leer_numero_natural()
    print(f"Número natural ingresado: {numero}")


if __name__ == "__main__":
    main()
