"""
La raíz cuadrada de un número puede obtenerse mediante la función sqrt() del
módulo math. Escribir un programa que utilice esta función para calcular la raíz
cuadrada de un número cualquiera ingresado a través del teclado. El programa
debe utilizar manejo de excepciones para evitar errores si se ingresa un número
negativo.
"""
import math

def calcular_raiz_cuadrada() -> float:
    """
    Solicita al usuario un número no negativo y calcula su raíz cuadrada.
    Repite la solicitud hasta recibir un valor válido.

    Returns:
        float: La raíz cuadrada del número ingresado.
    """
    while True:
        try:
            num = float(input("Ingrese un número no negativo: "))
            if num < 0:
                raise ValueError("El número no puede ser negativo.")
            return math.sqrt(num)
        except ValueError as e:
            print("Error:", e)


resultado = calcular_raiz_cuadrada()
print("La raíz cuadrada es:", resultado)
