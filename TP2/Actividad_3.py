"""
Crear una lista con los cuadrados de los números entre 1 y N (ambos incluidos),
donde N se ingresa desde el teclado. Luego se solicita imprimir los últimos 10 valo-
res de la lista.
"""
def generar_lista_cuadrados(n: int) -> list[int]:
    """Genera una lista de cuadrados desde 1 hasta n."""
    return [i ** 2 for i in range(1, n + 1)]


def main() -> None:
    """Función principal que solicita un número y muestra los cuadrados."""
    while True:
        try:
            numero = int(input("Ingrese un número entero positivo: "))
            if numero > 0:
                break
            print("El número debe ser mayor que 0.")
        except ValueError:
            print("Entrada inválida. Debe ingresar un número entero.")

    lista_cuadrados = generar_lista_cuadrados(numero)

    # Mostrar toda la lista
    print(f"\nLista completa de cuadrados ({len(lista_cuadrados)} elementos): {lista_cuadrados}")

    # Mostrar últimos 10 elementos, si hay al menos 10
    ultimos = lista_cuadrados[-10:] if len(lista_cuadrados) >= 10 else lista_cuadrados
    print("\nÚltimos elementos de la lista:")
    for elem in ultimos:
        print(elem)


if __name__ == "__main__":
    main()
