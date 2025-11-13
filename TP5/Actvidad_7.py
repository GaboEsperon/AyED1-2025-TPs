"""
Escribir un programa que juegue con el usuario a adivinar un número. El programa
debe generar un número al azar entre 1 y 500 y el usuario debe adivinarlo. Para
eso, cada vez que se introduce un valor se muestra un mensaje indicando si el nú-
mero que tiene que adivinar es mayor o menor que el ingresado. Cuando consiga
adivinarlo, se debe imprimir en pantalla la cantidad de intentos que le tomó hallar
el número. Si el usuario introduce algo que no sea un número se mostrará un
mensaje en pantalla y se lo contará como un intento más.
"""
import random as rn

def generar_numero_azar() -> int:
    """
    Genera un número aleatorio entre 1 y 500.
    """
    return rn.randint(1, 500)


def jugar_adivinanza() -> None:
    """
    Juego de adivinar un número entre 1 y 500.
    Cuenta cada intento, incluyendo entradas inválidas.
    """
    objetivo = generar_numero_azar()
    intentos = 0

    while True:
        intentos += 1
        try:
            valor = int(input("Ingrese un número entre 1 y 500: "))

            if not 1 <= valor <= 500:
                print("El número debe estar entre 1 y 500.")
                continue

            if valor > objetivo:
                print("El número ingresado es mayor que el número a adivinar.")
            elif valor < objetivo:
                print("El número ingresado es menor que el número a adivinar.")
            else:
                print(f"Se encontró el número en {intentos} intentos.")
                break

        except ValueError:
            print("Entrada inválida: debe ingresar un número entero.")


jugar_adivinanza()
