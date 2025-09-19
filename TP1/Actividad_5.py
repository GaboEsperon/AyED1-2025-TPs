"""
5. Escribir funciones lambda para:

a. Informar si un número es oblongo. Se dice que un número es oblongo cuando
se puede obtener multiplicando dos números naturales consecutivos. Por ejem-
plo 6 es oblongo porque resulta de multiplicar 2 * 3.

b. Informar si un número es triangular. Un número se define como triangular si
puede expresarse como la suma de un grupo de números naturales consecuti-
vos comenzando desde 1. Por ejemplo 10 es un número triangular porque se
obtiene sumando 1+2+3+4.

Ambas funciones lambda reciben como único parámetro el número a evaluar y de-
vuelven True o False. No se permite utilizar ayudas externas a las mismas.
"""
def es_oblongo(numero: int) -> bool:
    """
    Determina si un número es oblongo (rectangular),
    es decir, si se puede expresar como n*(n+1) para algún entero n.

    Parámetros:
        numero (int): Número a evaluar.

    Retorna:
        bool: True si el número es oblongo, False en caso contrario.
    """
    return int((4 * numero + 1) ** 0.5) ** 2 == 4 * numero + 1


def es_triangular(numero: int) -> bool:
    """
    Determina si un número es triangular,
    es decir, si se puede expresar como n*(n+1)//2 para algún entero n.

    Parámetros:
        numero (int): Número a evaluar.

    Retorna:
        bool: True si el número es triangular, False en caso contrario.
    """
    return any(n * (n + 1) // 2 == numero for n in range(1, int((2 * numero) ** 0.5) + 1))


def main() -> None:
    """
    Función principal que solicita un número al usuario, 
    verifica si es oblongo y/o triangular, y muestra los resultados.
    """
    while True:
        try:
            num = int(input("Ingrese un número: "))
            
            if es_oblongo(num):
                print("El número es oblongo.")
            else:
                print("El número no es oblongo.")
            
            if es_triangular(num):
                print("El número es triangular.")
            else:
                print("El número no es triangular.")
            
            break
        except ValueError:
            print("Por favor, ingrese un valor entero.")


if __name__ == "__main__":
    main()
