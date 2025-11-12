import random

def crear_baraja_espanola() -> list[str]:
    """
    Crea una lista con todos los naipes de la baraja española (48 cartas, del 1 al 12 en cada palo).

    Cada carta se representa como una cadena con el formato:
    "<número> <palo>", por ejemplo: "1 Oros" o "12 Espadas".

    Retorna:
        list[str]: lista con todas las cartas de la baraja.

    """
    numeros = list(range(1, 13))  # incluye del 1 al 12
    palos = ["Oros", "Copas", "Bastos", "Espadas"]

    # comprensión de listas para generar todas las combinaciones
    baraja = [f"{numero} {palo}" for palo in palos for numero in numeros]
    return baraja


def main():
    """
    Muestra la baraja española completa y una versión mezclada
    """
    print("BARAJA ESPAÑOLA COMPLETA (1 al 12 en cada palo):\n")

    baraja = crear_baraja_espanola()
    print(", ".join(baraja))

    random.shuffle(baraja)
    print("\nBaraja mezclada:\n")
    for carta in baraja[:10]:
        print("-", carta)
    print("... (resto del mazo barajado)\n")

    print("'Cuando apuestas con un brujo, asegúrate de no jugar con fuego.'")


if __name__ == "__main__":
    main()
