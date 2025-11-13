"""
El método index permite buscar un elemento dentro de una lista, devolviendo la
posición que éste ocupa. Sin embargo, si el elemento no pertenece a la lista se
produce una excepción de tipo ValueError. Desarrollar un programa que cargue
una lista con números enteros ingresados a través del teclado (terminando con -1)
y permita que el usuario ingrese el valor de algunos elementos para visualizar la
posición que ocupan, utilizando el método index. Si el número no pertenece a la
lista se imprimirá un mensaje de error y se solicitará otro para buscar. Abortar el
proceso al tercer error detectado. No utilizar el operador indurante la búsqueda.
"""
def cargar_enteros() -> list[int]:
    """
    Carga una lista de números enteros proporcionados por el usuario.
    Finaliza cuando se ingresa -1.
    """
    numeros = []
    while True:
        try:
            valor = int(input("Ingrese un número entero (-1 para finalizar): "))
            if valor == -1:
                break
            numeros.append(valor)
        except ValueError:
            print("Entrada inválida: debe ingresar un número entero.")
    return numeros


def buscar_posiciones() -> None:
    """
    Permite ingresar valores para buscar su posición en la lista usando index().
    Aborta si se producen tres errores de búsqueda.
    """
    lista = cargar_enteros()

    if not lista:
        print("La lista está vacía.")
        return

    errores = 0

    while errores < 3:
        try:
            buscado = int(input("Ingrese un número a buscar en la lista: "))
            posicion = lista.index(buscado)
            print(f"El número {buscado} está en la posición {posicion}.")
        except ValueError:
            errores += 1
            print("Error: el número no se encuentra en la lista.")
            if errores == 3:
                print("Se alcanzó el límite de errores. Proceso finalizado.")
                return


buscar_posiciones()
