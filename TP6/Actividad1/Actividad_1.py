"""
Escribir un programa que lea un archivo de texto conteniendo un conjunto de ape-
llidos y nombres en formato "Apellido, Nombre" y guarde en el archivo
ARMENIA.TXT los registros de aquellas personas cuyo apellido termina con la cade-
na "IAN", en el archivo ITALIA.TXT los terminados en "INI" y en ESPAÑA.TXT los
terminados en "EZ". Descartar el resto. Ejemplo:
Arslanian, Gustavo –> ARMENIA.TXT
Rossini, Giuseppe
Pérez, Juan
Smith, John
–> ITALIA.TXT
–> ESPAÑA.TXT
–> descartar
El archivo puede ser creado mediante el Block de Notas o el cualquier otro editor.
"""
def leer_archivo_nombres(ruta: str) -> list[tuple[str, str]]:
    """
    Lee un archivo de texto y devuelve una lista de tuplas (apellido, nombre).
    Solo acepta líneas en formato 'Apellido, Nombre'.
    """
    nombres = []
    try:
        with open(ruta, "rt", encoding="utf-8") as file:
            for linea in file:
                partes = linea.strip().split(",")
                if len(partes) != 2:
                    continue  # descartar líneas incorrectas

                apellido = partes[0].strip()
                nombre = partes[1].strip()

                if apellido and nombre:
                    nombres.append((apellido, nombre))

        return nombres

    except FileNotFoundError:
        print("El archivo especificado no existe.")
        return []


def clasificar_por_apellido(registros: list[tuple[str, str]]) -> None:
    """
    Clasifica los registros según el sufijo del apellido,
    y los escribe en archivos ARMENIA.TXT, ITALIA.TXT y ESPAÑA.TXT.
    """
    criterios = {
        "ARMENIA.TXT": lambda ap: ap.lower().endswith("ian"),
        "ITALIA.TXT": lambda ap: ap.lower().endswith("ini"),
        "ESPAÑA.TXT": lambda ap: ap.lower().endswith("ez"),
    }

    # Inicializar archivos vacíos
    for archivo in criterios:
        with open(archivo, "wt", encoding="utf-8"):
            pass

    # Clasificar y escribir
    for apellido, nombre in registros:
        for archivo, condicion in criterios.items():
            if condicion(apellido):
                with open(archivo, "a", encoding="utf-8") as f:
                    f.write(f"{apellido}, {nombre}\n")
                break  # evitar escribir un nombre en más de un archivo


# Programa principal
ruta = "ej01_nombres.txt"
lista_nombres = leer_archivo_nombres(ruta)
if lista_nombres:
    clasificar_por_apellido(lista_nombres)
