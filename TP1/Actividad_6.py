"""
Desarrollar una función que reciba como parámetros dos números enteros positivos
y devuelva como valor de retorno el número que resulte de concatenar ambos
parámetros. Por ejemplo, si recibe 1234 y 567 debe devolver 1234567.
En este caso, se permite usar f-strings.
"""

def concatenar_nums(num1: int, num2: int) -> int:
    """
    Concatena dos números enteros positivos usando f-strings.
    """
    return int(f"{num1}{num2}")


def main() -> None:
    """
    Pide al usuario dos números positivos y muestra el número concatenado.
    """
    while True:
        try:
            num1 = int(input("Ingrese el primer número: "))
            num2 = int(input("Ingrese el segundo número: "))
            if num1 <= 0 or num2 <= 0:
                print("Por favor, ingrese números positivos.")
            else:
                resultado = concatenar_nums(num1, num2)
                print(f"El número concatenado es: {resultado}")
                break
        except ValueError:
            print("Por favor, ingrese números enteros válidos.")

    main()
