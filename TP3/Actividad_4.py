import random as rnd

# Configuración global reproducible
rnd.seed(1)
DIAS_SEMANA = 7


def generar_produccion() -> list[list[list[int]]]:
    """
    Genera los datos de producción de bicicletas para varias fábricas.
    Cada fábrica tiene registros diarios de 7 días (día, cantidad_producida).
    La cantidad de fábricas se genera aleatoriamente entre 1 y 5.
    """
    fabricas = []
    num_fabricas = rnd.randint(1, 5)

    for i in range(num_fabricas):
        produccion_fabrica = []
        for dia in range(1, DIAS_SEMANA + 1):
            cantidad = rnd.randint(0, 150)
            produccion_fabrica.append([dia, cantidad])
        fabricas.append(produccion_fabrica)
        print(f"Fábrica {i + 1}: {produccion_fabrica}")

    return fabricas


def mostrar_totales_fabrica(fabricas: list[list[list[int]]]) -> None:
    """Imprime el total semanal de bicicletas producidas por cada fábrica."""
    for i, fabrica in enumerate(fabricas, start=1):
        total = sum(produccion for _, produccion in fabrica)
        print(f"Fábrica {i}: produjo un total de {total} bicicletas.")


def mayor_produccion_diaria(fabricas: list[list[list[int]]]) -> None:
    """
    Determina la fábrica y el día con la mayor producción individual.
    """
    max_produccion = -1
    fabrica_max = dia_max = None

    for i, fabrica in enumerate(fabricas, start=1):
        for dia, cantidad in fabrica:
            if cantidad > max_produccion:
                max_produccion = cantidad
                dia_max = dia
                fabrica_max = i

    if fabrica_max:
        print(
            f"La mayor producción diaria fue de {max_produccion} bicicletas "
            f"en la fábrica {fabrica_max} el día {dia_max}."
        )
    else:
        print("No se encontraron datos de producción.")


def dia_mayor_produccion(fabricas: list[list[list[int]]]) -> None:
    """
    Calcula qué día (considerando todas las fábricas) fue el más productivo.
    """
    if not fabricas:
        print("No hay fábricas cargadas.")
        return

    total_por_dia = [0] * DIAS_SEMANA

    for fabrica in fabricas:
        for dia, cantidad in fabrica:
            total_por_dia[dia - 1] += cantidad

    dia_max = total_por_dia.index(max(total_por_dia)) + 1
    print(
        f"El día más productivo fue el día {dia_max}, "
        f"con {max(total_por_dia)} bicicletas en total."
    )


def minimo_diario_por_fabrica(fabricas: list[list[list[int]]]) -> list[int]:
    """
    Devuelve una lista con la menor cantidad de bicicletas fabricadas
    por cada fábrica en un solo día.
    """
    return [min(cantidad for _, cantidad in fabrica) for fabrica in fabricas]


def ejecutar_programa():
    """Función principal que coordina la ejecución del programa."""
    print("Generando datos de producción de bicicletas:\n")
    fabricas = generar_produccion()
    print()

    mostrar_totales_fabrica(fabricas)
    print()
    mayor_produccion_diaria(fabricas)
    print()
    dia_mayor_produccion(fabricas)

    print("\nMenor cantidad fabricada por fábrica:")
    for i, minimo in enumerate(minimo_diario_por_fabrica(fabricas), start=1):
        print(f"Fábrica {i}: {minimo} bicicletas")


if __name__ == "__main__":
    ejecutar_programa()