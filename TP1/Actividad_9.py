"""
Un productor frutihortícola desea contabilizar sus cajones de naranjas según el peso
para poder cargar los camiones de reparto. La empresa cuenta con N camiones, y
cada uno puede transportar hasta media tonelada (500 kilogramos). En un cajón
caben 100 naranjas con un peso de entre 200 y 300 gramos cada una. Si el peso
de alguna naranja se encuentra fuera del rango indicado se la clasifica para
procesar como jugo. Desarrollar un programa para ingresar la cantidad de naranjas
cosechadas e informar cuántos cajones se pueden llenar, cuántas naranjas son para
jugo y si hay algún sobrante de naranjas que deba considerarse para el siguiente
reparto. Simular el peso de cada unidad generando un número entero al azar entre
150 y 350.
Además, se desea saber cuántos camiones se necesitan para transportar la cose-
cha, considerando que la ocupación del camión no debe ser inferior al 80%; en
caso contrario el camión no serán despachado por su alto costo.
"""
import random as rnd
import math


rnd.seed(1)


PESO_MINIMO = 200
PESO_MAXIMO = 300
NARANJAS_POR_CAJON = 100
PESO_MAX_CAMION = 500
PORCENTAJE_MINIMO_OCUPACION_CAMION = 0.80


def validar_entrada_naranjas(num: int) -> bool:
    """
    Valida que el número de naranjas sea mayor a 0.
    """
    return num > 0


def ingresar_naranjas_cosechadas() -> int:
    """
    Solicita al usuario que ingrese la cantidad de naranjas cosechadas.
    """
    while True:
        try:
            cantidad = int(input("Ingrese la cantidad de naranjas cosechadas: "))
            if validar_entrada_naranjas(cantidad):
                return cantidad
            else:
                print("El número debe ser mayor a 0.")
        except ValueError:
            print("Por favor, ingrese un número válido.")


def generar_peso_naranja() -> float:
    """
    Genera un peso aleatorio para una naranja entre 150g y 350g, convertido a kg.
    """
    return rnd.randint(150, 350) / 1000


def procesar_naranjas(cantidad_de_naranjas: int) -> tuple:
    """
    Procesa la cantidad de naranjas, determinando cuántos cajones se llenan,
    cuántas naranjas son para jugo, cuántas sobran, y cuántos camiones se necesitan.
    """
    naranjas_por_cajon = 0
    naranjas_para_jugo = 0
    peso_total_cosecha = 0.0

    for _ in range(cantidad_de_naranjas):
        peso_naranja = generar_peso_naranja()
        if PESO_MINIMO / 1000 <= peso_naranja <= PESO_MAXIMO / 1000:
            naranjas_por_cajon += 1
            peso_total_cosecha += peso_naranja
        else:
            naranjas_para_jugo += 1

    cajones_llenos = naranjas_por_cajon // NARANJAS_POR_CAJON
    naranjas_sobrantes = naranjas_por_cajon % NARANJAS_POR_CAJON

    camiones_necesarios = math.ceil(peso_total_cosecha / PESO_MAX_CAMION)
    camiones_despachados = 0

    peso_restante = peso_total_cosecha
    for _ in range(camiones_necesarios):
        peso_actual = min(peso_restante, PESO_MAX_CAMION)
        if peso_actual / PESO_MAX_CAMION >= PORCENTAJE_MINIMO_OCUPACION_CAMION:
            camiones_despachados += 1
        peso_restante -= peso_actual

    return cajones_llenos, naranjas_para_jugo, naranjas_sobrantes, camiones_despachados


def main() -> None:
    """
    Función principal que coordina la ejecución del programa.
    """
    cantidad_naranjas = ingresar_naranjas_cosechadas()
    cajones_llenos, naranjas_para_jugo, naranjas_sobrantes, camiones_despachados = (
        procesar_naranjas(cantidad_naranjas)
    )

    print(f"Cajones llenos: {cajones_llenos}")
    print(f"Naranjas para jugo: {naranjas_para_jugo}")
    print(f"Naranjas sobrantes para el siguiente reparto: {naranjas_sobrantes}")
    print(f"Camiones despachados: {camiones_despachados}")


main()