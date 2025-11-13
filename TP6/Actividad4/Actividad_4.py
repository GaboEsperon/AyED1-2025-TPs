"""
Desarrollar un programa para eliminar todos los comentarios de un programa es-
crito en lenguaje Python. Tener en cuenta que los comentarios comienzan con el
signo # (siempre que éste no se encuentre encerrado entre comillas simples o do-
bles) y que también se considera comentario a las cadenas de documentación
(docstrings).
"""
def eliminar_comentarios() -> None:
    """
    Solicita un archivo .py y genera una versión limpia sin comentarios.
    Se eliminan:
        - Comentarios iniciados con #
        - Docstrings entre triple comillas simples o dobles

    Se procesa el archivo línea por línea para evitar cargarlo completo
    en memoria. Los comentarios dentro de cadenas no se eliminan.

    Raises:
        ValueError: Si el archivo no puede abrirse o procesarse.
    """
    try:
        ruta = input("Ingrese el nombre del archivo Python a limpiar: ").strip()

        try:
            archivo_original = open(ruta, "r", encoding="utf-8")
        except FileNotFoundError:
            raise ValueError("No se pudo abrir el archivo indicado.")

        nombre_base = ruta.rsplit(".", 1)[0]
        archivo_salida = open(f"{nombre_base}_limpio.py", "w", encoding="utf-8")

        dentro_docstring = False  # Para saber si estamos dentro de un docstring

        with archivo_original, archivo_salida:
            for linea in archivo_original:

                # Primero manejamos docstrings
                # Buscamos triples comillas simples o dobles
                if '"""' in linea or "'''" in linea:
                    triple = '"""' if '"""' in linea else "'''"

                    # Caso 1: docstring de apertura
                    if not dentro_docstring:
                        # Si está en una sola línea (`""" texto """`), lo saltamos entero
                        if linea.count(triple) == 2:
                            continue
                        else:
                            dentro_docstring = True
                            continue
                    else:
                        # Caso 2: docstring de cierre
                        dentro_docstring = False
                        continue

                # Si estamos en un docstring, ignoramos todo
                if dentro_docstring:
                    continue

                # Eliminación de comentarios con #
                nueva_linea = ""
                comillas = False
                tipo_comilla = None

                for i, ch in enumerate(linea):
                    # Detectar apertura/cierre de cadena
                    if ch in ("'", '"'):
                        if not comillas:
                            comillas = True
                            tipo_comilla = ch
                        elif tipo_comilla == ch:
                            comillas = False
                            tipo_comilla = None

                    # Si encontramos # fuera de una cadena → comentario
                    if ch == "#" and not comillas:
                        break

                    nueva_linea += ch

                # Escribir la línea resultante solo si no queda vacía o solo espacios
                if nueva_linea.strip() != "":
                    archivo_salida.write(nueva_linea.rstrip() + "\n")

        print("Archivo limpio generado correctamente.")

    except ValueError as e:
        print("Error:", e)
    except Exception as e:
        print("No se pudo completar la operación:", e)


eliminar_comentarios()
