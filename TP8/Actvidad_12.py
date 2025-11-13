"""
Una librería almacena su lista de precios en un diccionario. Diseñar un programa
para crearlo, incrementar los precios de los cuadernos en un 15%, imprimir un
listado con todos los elementos de la lista de precios e indicar cuál es el ítem más
costoso que venden en el comercio.
"""

def ajustar_precio(precios: dict, producto: str, porcentaje: float) -> dict:
    """
    Incrementa el precio de un producto según un porcentaje.

    Parameters:
        precios (dict): Diccionario de productos y precios.
        producto (str): Producto a modificar.
        porcentaje (float): Porcentaje de aumento.

    Returns:
        dict: El diccionario actualizado.
    """
    if producto in precios:
        precios[producto] *= 1 + porcentaje / 100
    return precios


def buscar_item_mayor_precio(precios: dict) -> str:
    """
    Devuelve el producto más costoso.

    Parameters:
        precios (dict): Diccionario de productos y precios.

    Returns:
        str: Nombre del ítem más costoso.
    """
    return max(precios, key=precios.get)


def mostrar_precios(precios: dict) -> None:
    """
    Muestra la lista de productos y sus precios.

    Parameters:
        precios (dict): Diccionario de productos y precios.
    """
    print("Listado de precios:")
    for producto, precio in precios.items():
        print(f"{producto}: ${precio:.2f}")


def main():
    precios = {
        "cuaderno": 50.0,
        "lapiz": 15.0,
        "borrador": 10.0,
        "regla": 30.0,
        "lapicera": 20.0,
    }

    ajustar_precio(precios, "cuaderno", 15)

    mostrar_precios(precios)

    item_mayor = buscar_item_mayor_precio(precios)
    print(f"\nEl ítem más costoso es: {item_mayor} con un precio de ${precios[item_mayor]:.2f}")


if __name__ == "__main__":
    main()
