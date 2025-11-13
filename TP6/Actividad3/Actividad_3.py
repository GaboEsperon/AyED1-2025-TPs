"""
Una institución deportiva necesita clasificar a sus atletas para inscribirlos en los
próximos Juegos Panamericanos. Para eso encargó la realización de un programa
que incluya las siguientes funciones:
GrabarRangoAlturas(): Graba en un archivo las alturas de los atletas de distintas
disciplinas, los que se ingresan desde el teclado. Cada dato se debe grabar en una
línea distinta. Ejemplo:

<Deporte 1>
<altura del atleta 1>
<altura del atleta 2>
<. . . >
<Deporte 2>
<altura del atleta 1>
<altura del atleta 2>
<. . . >
GrabarPromedio(): Graba en un archivo los promedios de las alturas de los atle-
tas, leyendo los datos del archivo generado en el paso anterior. La disciplina y el
promedio deben grabarse en líneas diferentes. Ejemplo:
<Deporte 1>
<Promedio de alturas deporte 1>
<Deporte 2>
<Promedio de alturas deporte 2>
<. . . >
MostrarMasAltos() Muestra por pantalla las disciplinas deportivas cuyos atletas
superan la estatura promedio general. Obtener los datos del segundo archivo.
"""
def grabar_rango_alturas(archivo: str) -> None:
    """
    Graba deportes y alturas de atletas en un archivo de texto.
    Formato:
    <Deporte>
    <altura>
    <altura>
    """
    with open(archivo, "wt", encoding="utf-8") as f:
        while True:
            deporte = input("Ingrese deporte (q para salir): ").strip()
            if deporte.lower() == "q":
                break
            if not deporte:
                continue

            f.write(f"{deporte}\n")

            while True:
                altura = input("Ingrese altura en cm (-1 para terminar deporte): ")
                if altura == "-1":
                    break
                try:
                    altura_int = int(altura)
                    if altura_int <= 0:
                        print("Altura inválida.")
                        continue
                    f.write(f"{altura_int}\n")
                except ValueError:
                    print("Debe ingresar un número entero.")


def grabar_promedio(archivo: str, archivo_prom: str = "promedio_alturas.txt") -> dict:
    """
    Lee el archivo de alturas y genera un archivo con:
    <Deporte>
    <Promedio>
    Devuelve dict {deporte: [alturas]}
    """
    alturas = {}
    deporte_actual = None

    with open(archivo, "rt", encoding="utf-8") as f:
        for linea in f:
            linea = linea.strip()
            if not linea:
                continue

            # Si es texto, asumimos deporte
            if not linea.isdigit():
                deporte_actual = linea
                alturas[deporte_actual] = []
            else:
                alturas[deporte_actual].append(int(linea))

    # Grabar promedios
    with open(archivo_prom, "wt", encoding="utf-8") as out:
        for dep, vals in alturas.items():
            if vals:
                promedio = sum(vals) / len(vals)
                out.write(f"{dep}\n{promedio:.2f}\n")

    return alturas


def mostrar_mas_altos(archivo_prom: str) -> None:
    """
    Muestra los deportes cuyo promedio supera el promedio general.
    """
    deportes = []
    promedios = []

    # Leer archivo
    with open(archivo_prom, "rt", encoding="utf-8") as f:
        lineas = [l.strip() for l in f if l.strip()]

    for i in range(0, len(lineas), 2):
        dep = lineas[i]
        prom = float(lineas[i + 1])
        deportes.append(dep)
        promedios.append(prom)

    if not promedios:
        print("No hay datos para procesar.")
        return

    promedio_general = sum(promedios) / len(promedios)

    print("Disciplinas que superan el promedio general:")
    for dep, prom in zip(deportes, promedios):
        if prom > promedio_general:
            print(dep)


# Programa principal
nombre_archivo = "alturas.txt"
grabar_rango_alturas(nombre_archivo)
grabar_promedio(nombre_archivo)
mostrar_mas_altos("promedio_alturas.txt")
