"""
Se dispone de dos formatos diferentes de archivos de texto en los que se almace-
nan datos de empleados, detallados más abajo. Desarrollar un programa para con-
vertir cada uno de los formatos suministrados, grabando los datos obtenidos en
otro archivo con formato CSV. Los archivos de entrada pueden generarse con Block
de Notas o cualquier otro editor, copiando y pegando los ejemplos proporcionados.
Ambos archivos tienen tres campos por registro: Apellido y Nombre, Fecha de alta
y Domicilio.
"""
from datetime import datetime

def validar_nombre(nombre: str) -> str:
    if not nombre.replace(" ", "").isalpha():
        raise ValueError("El nombre y apellido solo deben contener letras y espacios.")
    return nombre.strip()

def validar_fecha(fecha: str) -> str:
    try:
        datetime.strptime(fecha, "%Y%m%d")
        return fecha
    except ValueError:
        raise ValueError("La fecha debe tener formato AAAAMMDD y ser válida.")

def validar_domicilio(dom: str) -> str:
    if not dom or dom.strip() == "":
        raise ValueError("El domicilio no puede estar vacío.")
    return dom.strip()


def generar_formato_uno(archivo_salida: str) -> None:
    """
    Genera un archivo en formato 1: campos de longitud fija.
    """
    try:
        nombre = validar_nombre(input("Nombre y apellido: "))
        fecha = validar_fecha(input("Fecha de alta (AAAAMMDD): "))
        domicilio = validar_domicilio(input("Domicilio: "))

        # Ajustar longitudes
        nombre_f = nombre.ljust(15)[:15]
        fecha_f = fecha.ljust(8)[:8]
        domicilio_f = domicilio.ljust(36)[:36]

        with open(archivo_salida, "wt", encoding="utf-8") as f:
            f.write(nombre_f + fecha_f + domicilio_f)

        print(f"Archivo '{archivo_salida}' generado correctamente.")

    except Exception as e:
        print(f"Error al generar formato 1: {e}")


def convertir_formato_uno_csv(archivo_entrada: str, archivo_csv: str) -> None:
    """
    Convierte un archivo en formato posicional fijo a CSV.
    """
    try:
        with open(archivo_entrada, "rt", encoding="utf-8") as f:
            linea = f.readline()

        if len(linea) < 15 + 8 + 36:
            raise ValueError("La línea del archivo es demasiado corta para el formato 1.")

        nombre = linea[0:15].strip()
        fecha = linea[15:23].strip()
        domicilio = linea[23:59].strip()

        with open(archivo_csv, "wt", encoding="utf-8") as out:
            out.write("Nombre,Fecha,Domicilio\n")
            out.write(f"{nombre},{fecha},{domicilio}\n")

        print(f"Archivo CSV '{archivo_csv}' generado correctamente.")

    except Exception as e:
        print(f"Error al convertir formato 1 a CSV: {e}")


def generar_formato_dos(archivo_salida: str) -> None:
    """
    Genera un archivo en formato 2: <len><texto>.
    """
    try:
        nombre = validar_nombre(input("Nombre y apellido: "))
        fecha = validar_fecha(input("Fecha de alta (AAAAMMDD): "))
        domicilio = validar_domicilio(input("Domicilio: "))

        partes = []
        for campo in (nombre, fecha, domicilio):
            longitud = len(campo)
            if longitud > 99:
                raise ValueError("Un campo supera los 99 caracteres (límite del formato).")
            partes.append(f"{longitud:02}{campo}")

        with open(archivo_salida, "wt", encoding="utf-8") as f:
            f.write("".join(partes))

        print(f"Archivo '{archivo_salida}' generado correctamente.")

    except Exception as e:
        print(f"Error al generar formato 2: {e}")


def convertir_formato_dos_csv(archivo_entrada: str, archivo_csv: str) -> None:
    """
    Convierte un archivo con campos precedidos por longitud a CSV.
    """
    try:
        with open(archivo_entrada, "rt", encoding="utf-8") as f:
            linea = f.readline().strip()

        idx = 0
        campos = []

        while idx < len(linea):
            largo = int(linea[idx:idx+2])
            idx += 2
            campo = linea[idx:idx+largo]
            idx += largo
            campos.append(campo)

        if len(campos) != 3:
            raise ValueError("Formato incorrecto: deben existir exactamente 3 campos.")

        nombre, fecha, domicilio = campos

        with open(archivo_csv, "wt", encoding="utf-8") as out:
            out.write("Nombre,Fecha,Domicilio\n")
            out.write(f"{nombre},{fecha},{domicilio}\n")

        print(f"Archivo CSV '{archivo_csv}' generado correctamente.")

    except Exception as e:
        print(f"Error al convertir formato 2 a CSV: {e}")

if __name__ == "__main__":
    # FORMATO 1
    generar_formato_uno("formato1.txt")
    convertir_formato_uno_csv("formato1.txt", "formato1.csv")

    # FORMATO 2
    generar_formato_dos("formato2.txt")
    convertir_formato_dos_csv("formato2.txt", "formato2.csv")
