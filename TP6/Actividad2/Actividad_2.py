"""
Escribir un programa que permita dividir un archivo de texto cualquiera en partes
que se puedan enviar por correo electrónico. El tamaño máximo de las partes se
ingresa por teclado. Los nombres de los archivos generados deben respetar el
nombre original con el agregado de un sufijo que indique de qué parte se trata.
Tener en cuenta que ningún registro puede ser dividido; la partición debe efectuar-
se después del delimitador del mismo. Mostrar un mensaje de error si el proceso no
pudiera llevarse a cabo. Recordar que no se permite cargar el archivo completo en
memoria.
"""
def dividir_archivo() -> None:
    """
    Solicita un archivo de texto y un tamaño máximo para cada parte,
    y lo divide en archivos más pequeños sin cortar registros.
    
    El archivo se procesa línea por línea para evitar cargarlo
    completo en memoria. Los archivos generados respetan el nombre
    original con un sufijo indicando la parte correspondiente.
    
    Raises:
        ValueError: Si el tamaño máximo es inválido o si el archivo
                    no puede procesarse correctamente.
    """
    try:
        ruta_archivo = input("Ingrese el nombre del archivo a dividir: ").strip()
        tam_max = int(input("Ingrese el tamaño máximo por parte (en bytes): "))

        if tam_max <= 0:
            raise ValueError("El tamaño máximo debe ser un número positivo.")

        # Intentar abrir el archivo original
        try:
            archivo_original = open(ruta_archivo, "r", encoding="utf-8")
        except FileNotFoundError:
            raise ValueError("No se pudo abrir el archivo indicado.")

        nombre_base = ruta_archivo.rsplit(".", 1)[0]
        extension = ruta_archivo.rsplit(".", 1)[1] if "." in ruta_archivo else "txt"

        parte = 1
        tam_actual = 0

        # Abrimos la primera parte
        archivo_salida = open(f"{nombre_base}_parte{parte}.{extension}", "w", encoding="utf-8")

        with archivo_original:
            for linea in archivo_original:
                tam_linea = len(linea.encode("utf-8"))

                # Si la línea no entra en la parte actual, abrir una nueva
                if tam_actual + tam_linea > tam_max:
                    archivo_salida.close()
                    parte += 1
                    tam_actual = 0
                    archivo_salida = open(f"{nombre_base}_parte{parte}.{extension}", "w", encoding="utf-8")

                archivo_salida.write(linea)
                tam_actual += tam_linea

        archivo_salida.close()
        print("El archivo fue dividido exitosamente.")

    except ValueError as e:
        print("Error:", e)
    except Exception as e:
        print("No se pudo completar la operación:", e)


dividir_archivo()
