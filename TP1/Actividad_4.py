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

def ingresar_compra():
    while True:
        try:
            compra = int(input("Ingrese el total de su compra: "))
            recibido = int(input("Ingrese el dinero recibido: "))
            if compra < 0 and recibido < 0: 
                print("Por favor ingresar números mayores mayores a 0.")
            elif recibido < compra:
                print("el dinero recibido debe ser mayor al valor de la compra")    
            else:
                return compra, recibido
        except ValueError:
            print("Por favor ingrese un número válido.")

def calcular_vuelto(compra,recibido):
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
    compra , recibido  = ingresar_compra()

    vuelto_efectivo = calcular_vuelto(compra,recibido)
    
    if vuelto_efectivo == -1:
        print("no se puede dar un vuelto exacto")

    else:
        for billete, cantidad in vuelto_efectivo.items():
            print(f"su vuelto en efectivo es {cantidad} billete(s) de ${billete}")

main()



