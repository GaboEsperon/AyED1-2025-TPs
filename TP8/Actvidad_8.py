"""
Generar e imprimir un diccionario donde las claves sean números enteros entre 1 y
20 (ambos incluidos) y los valores asociados sean el cuadrado de las claves.
"""
def crear_diccionario_cuadrados() -> dict:
    """
    Genera un diccionario donde las claves son números enteros del 1 al 20,
    y los valores son los cuadrados de dichas claves.

    Returns:
        dict: Diccionario con pares clave-valor (número: número al cuadrado).
    """
    return {n: n**2 for n in range(1, 21)}


def main():
    """
    Programa principal: genera el diccionario y lo imprime.
    """
    diccionario = crear_diccionario_cuadrados()
    print("Diccionario generado:")
    for clave, valor in diccionario.items():
        print(f"{clave}: {valor}")


if __name__ == "__main__":
    main()
