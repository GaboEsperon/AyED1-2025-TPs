"""
Desarrollar una función que reciba tres números enteros positivos y devuelva el mayor de los tres,
sólo si éste es único (es decir el mayor estricto).Devolver -1 en caso de no haber ninguno.
No utilizar operadores lógicos (and, or, not). Desarrollar también un programa para ingresar los tres valores,
invocar a la función y mostrar el máximo hallado, o un mensaje informativo si éste no existe.
"""
def num_max_estrict(lista_num: list[int]) -> int:
    """
    Devuelve el número mayor de una lista solo si es estrictamente mayor, 
    es decir, si no se repite en la lista. 

    Parámetros:
        lista_num (list[int]): Lista de números enteros.

    Retorna:
        int: El número mayor estricto si existe, o -1 si hay repetición del mayor.
    """
    num_mayor = max(lista_num)
    if lista_num.count(num_mayor) > 1:
        return -1
    else:
        return num_mayor


def recibir_num() -> list[int]:
    """
    Solicita al usuario ingresar 3 números enteros positivos. 
    Valida que sean enteros y mayores a cero.

    Retorna:
        list[int]: Lista con los 3 números ingresados.
    """
    numbers = []
    while len(numbers) < 3:
        try:
            new_num = int(input(f"Ingrese un número {len(numbers)+1}: "))
            if new_num <= 0:
                print("El número ingresado debe ser positivo.")
            else:
                numbers.append(new_num)
        except ValueError:
            print("Error: el número ingresado debe ser entero.")
    return numbers


def main():
    """
    Función principal que solicita al usuario 3 números, 
    calcula el número mayor estricto y muestra el resultado.
    """
    nums = recibir_num()
    resultado = num_max_estrict(nums)
    if resultado != -1:
        print("El número mayor estricto es:", resultado)
    else:
        print("No hay un número mayor estricto.")


if __name__ == "__main__":
    main()




    
    


        
