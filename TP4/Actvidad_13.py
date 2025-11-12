def convertir_a_letras(num: int) -> str:
    """
    Convierte un número entero entre 0 y 1 billón (1.000.000.000.000) a letras en español.

    Parámetros:
        num (int): número entero a convertir.

    Retorna:
        str: número expresado en letras.
    """
    if num < 0 or num > 1_000_000_000_000:
        return "Número fuera de rango"
    if num == 0:
        return "cero"
    if num == 1_000_000_000_000:
        return "un billón"

    unidades = [
        "", "uno", "dos", "tres", "cuatro", "cinco",
        "seis", "siete", "ocho", "nueve"
    ]
    especiales = [
        "diez", "once", "doce", "trece", "catorce",
        "quince", "dieciséis", "diecisiete", "dieciocho", "diecinueve"
    ]
    decenas = [
        "", "diez", "veinte", "treinta", "cuarenta", "cincuenta",
        "sesenta", "setenta", "ochenta", "noventa"
    ]
    centenas = [
        "", "cien", "doscientos", "trescientos", "cuatrocientos",
        "quinientos", "seiscientos", "setecientos", "ochocientos", "novecientos"
    ]

    partes = []

    # Billones y millones
    if num >= 1_000_000_000:
        miles_de_millones = num // 1_000_000_000
        if miles_de_millones == 1:
            partes.append("mil millones")
        else:
            partes.append(convertir_a_letras(miles_de_millones) + " mil millones")
        num %= 1_000_000_000

    if num >= 1_000_000:
        millones = num // 1_000_000
        if millones == 1:
            partes.append("un millón")
        else:
            partes.append(convertir_a_letras(millones) + " millones")
        num %= 1_000_000

    if num >= 1_000:
        miles = num // 1_000
        if miles == 1:
            partes.append("mil")
        else:
            partes.append(convertir_a_letras(miles) + " mil")
        num %= 1_000

    if num >= 100:
        centenas_valor = num // 100
        if centenas_valor == 1 and num % 100 != 0:
            partes.append("ciento")
        else:
            partes.append(centenas[centenas_valor])
        num %= 100

    if 10 <= num < 20:
        partes.append(especiales[num - 10])
        num = 0
    elif num >= 20:
        decena_valor = num // 10
        resto = num % 10
        palabra = decenas[decena_valor]
        if resto > 0:
            if decena_valor == 2:
                palabra = "veinti" + unidades[resto]
            else:
                palabra += " y " + unidades[resto]
        partes.append(palabra)
        num = 0

    if num > 0:
        partes.append(unidades[num])

    return " ".join(p for p in partes if p).strip()


def main():
    """
    Programa de prueba
    """
    numero = int(input("Ingrese un número (0 a 1 billón): "))
    texto = convertir_a_letras(numero)
    print(f"\n{numero} en letras es:\n{texto}\n")




if __name__ == "__main__":
    main()
