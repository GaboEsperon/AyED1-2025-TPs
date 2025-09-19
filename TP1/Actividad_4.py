"""
Un comercio de electrodomésticos necesita para su línea de cajas un programa que
le indique al cajero el cambio que debe entregarle al cliente. Para eso se ingresan
dos números enteros, correspondientes al total de la compra y al dinero recibido.
Informar cuántos billetes de cada denominación deben ser entregados como vuelto,
de tal forma que se minimice la cantidad de billetes. Considerar que existen billetes
de $5000, $1000, $500, $200, $100, $50 y $10. Emitir un mensaje de error si el
dinero recibido fuera insuficiente o si el cambio no pudiera entregarse debido a falta
de billetes con denominaciones adecuadas. Ejemplo: Si la compra es de $3170 y se
abona con $5000, el vuelto debe contener 1 billete de $1000, 1 billete de $500, 1
billete de $200, 1 billete de $100 y 3 billetes de $10.
"""

def ingresar_compra() -> tuple[int, int]:
    """
    Solicita al usuario ingresar el total de la compra y el dinero recibido.
    Valida que ambos sean números enteros positivos y que el dinero recibido
    sea mayor o igual al total de la compra.

    Retorna:
        tuple[int, int]: Una tupla con el total de la compra y el dinero recibido.
    """
    while True:
        try:
            compra = int(input("Ingrese el total de su compra: "))
            recibido = int(input("Ingrese el dinero recibido: "))
            if compra < 0 or recibido < 0:
                print("Por favor ingresar números mayores a 0.")
            elif recibido < compra:
                print("El dinero recibido debe ser mayor o igual al valor de la compra.")
            else:
                return compra, recibido
        except ValueError:
            print("Por favor ingrese un número válido.")


def calcular_vuelto(compra: int, recibido: int) -> dict[int, int] | int:
    """
    Calcula el vuelto exacto en billetes según las denominaciones disponibles.
    
    Parámetros:
        compra (int): Total de la compra.
        recibido (int): Dinero recibido por el cliente.

    Retorna:
        dict[int, int]: Diccionario con billetes como claves y cantidad como valores.
        int: -1 si no se puede entregar un vuelto exacto.
    """
    billetes_val = [5000, 1000, 500, 200, 100, 50, 10]
    cambio = recibido - compra
    vuelto_efectivo = {}

    for billete in billetes_val:
        if cambio >= billete:
            cantidad_billetes = cambio // billete
            vuelto_efectivo[billete] = cantidad_billetes
            cambio -= cantidad_billetes * billete

    if cambio != 0:
        return -1

    return vuelto_efectivo


def main():
    """
    Función principal que solicita los datos de compra al usuario,
    calcula el vuelto exacto y muestra el resultado en billetes.
    """
    compra, recibido = ingresar_compra()
    vuelto_efectivo = calcular_vuelto(compra, recibido)

    if vuelto_efectivo == -1:
        print("No se puede dar un vuelto exacto.")
    else:
        print("Su vuelto en efectivo es:")
        for billete, cantidad in vuelto_efectivo.items():
            print(f"{cantidad} billete(s) de ${billete}")


if __name__ == "__main__":
    main()


