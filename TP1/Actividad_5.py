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
es_oblongo = lambda x: int((4 * x + 1) ** 0.5) ** 2 == 4 * x + 1

es_triangular = lambda x: any(n * (n + 1) // 2 == x for n in range(1, int((2 * x)**0.5) + 1))

def main() -> None:
    
    while True:
        
        try:
        
            num = int(input("ingrese un numero: "))
        
            if es_oblongo(num):
                print("el numero es oblongo")
            else:
                print("el numero no es oblongo")
        
            if es_triangular(num):
                print("el numero es triangular")
            else:
                print("el numero no es triangular")        
            break
        except ValueError:
            print("por favor ingresar un valor entero: ")

main()
