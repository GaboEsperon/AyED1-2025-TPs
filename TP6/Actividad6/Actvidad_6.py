"""
Un hotel necesita un programa para gestionar la operación de sus habitaciones. El hotel
cuenta con 10 pisos y 6 habitaciones por piso. Por cada huésped o grupo familiar que se alo-
ja en el mismo se registra la siguiente información:
DNI del cliente (número entero)
Apellido y Nombre
Fecha de ingreso (DDMMAAAA)
Fecha de egreso (DDMMAAAA)
Cantidad de ocupantes
Se solicita desarrollar un programa para realizar las siguientes tareas:
Registrar el ingreso de huéspedes al hotel, hasta que se ingrese un número de DNI -1.
Esta información deberá grabarse en un archivo CSV donde cada registro incluirá todos
los campos indicados más arriba. Tener en cuenta que los números de DNI no pueden
repetirse y que la fecha de salida debe ser mayor a la de entrada.
Finalizado el ingreso de huéspedes se solicita:
a. Leer el archivo de huéspedes y asignar la habitaciones a cada uno. El piso y
habitación son asignados arbitrariamente, y no puede asignarse una habitación ya
otorgada.
b. Mostrar el piso con mayor cantidad de habitaciones ocupadas.
c. Mostrar cuántas habitaciones vacías hay en todo el hotel.
d. Mostrar el piso con mayor cantidad de personas.
e. Mostrar cuál será la próxima habitación en desocuparse. La fecha actual se ingresa
por teclado. Mostrar todas las que correspondan.
f. Mostrar un listado de todos los huéspedes registrados en el hotel, ordenado por
cantidad de días de alojamiento.
"""
import csv
from datetime import datetime


def registrar_huespedes(ruta: str) -> None:
    """
    Registra huéspedes en un archivo CSV hasta que se ingrese DNI = -1.
    Valida:
        - DNI no repetido
        - Fecha de ingreso < fecha de egreso

    Parameters:
        ruta (str): Ruta del archivo CSV donde se guardarán los registros.
    """
    try:
        dnis_registrados = set()

        try:
            with open(ruta, "r", encoding="utf-8", newline="") as file:
                lector = csv.reader(file)
                for fila in lector:
                    if fila:
                        dnis_registrados.add(int(fila[0]))
        except FileNotFoundError:
            pass

        with open(ruta, "a", encoding="utf-8", newline="") as file:
            escritor = csv.writer(file)

            while True:
                try:
                    dni = int(input("Ingrese DNI del huésped (-1 para terminar): ").strip())
                except ValueError:
                    print("Debe ingresar un número válido.")
                    continue

                if dni == -1:
                    break

                if dni in dnis_registrados:
                    print("El DNI ya se encuentra registrado.")
                    continue

                apellido_nombre = input("Apellido y Nombre: ").strip()
                fecha_ing = input("Fecha de ingreso (DDMMAAAA): ").strip()
                fecha_egr = input("Fecha de egreso (DDMMAAAA): ").strip()

                try:
                    f_ing = datetime.strptime(fecha_ing, "%d%m%Y")
                    f_egr = datetime.strptime(fecha_egr, "%d%m%Y")
                except ValueError:
                    print("Fechas inválidas.")
                    continue

                if f_ing >= f_egr:
                    print("La fecha de egreso debe ser mayor que la de ingreso.")
                    continue

                try:
                    cant = int(input("Cantidad de ocupantes: ").strip())
                    if cant <= 0:
                        raise ValueError
                except ValueError:
                    print("Cantidad de ocupantes inválida.")
                    continue

                escritor.writerow([dni, apellido_nombre, fecha_ing, fecha_egr, cant])
                dnis_registrados.add(dni)

        print("Registro de huéspedes finalizado.")

    except Exception as e:
        print("No se pudo completar el registro:", e)


def asignar_habitaciones(ruta: str) -> list:
    """
    Asigna habitaciones a cada huésped de forma arbitraria.
    Devuelve una lista con los datos incluyendo piso y habitación.

    El hotel tiene:
        - 10 pisos
        - 6 habitaciones por piso
    """
    try:
        habitaciones = [[None for _ in range(6)] for _ in range(10)]
        asignados = []

        with open(ruta, "r", encoding="utf-8") as file:
            lector = csv.reader(file)
            for fila in lector:
                dni, nombre_completo, f_ing, f_egr, cant = fila
                asignado = False

                for piso in range(10):
                    for hab in range(6):
                        if habitaciones[piso][hab] is None:
                            habitaciones[piso][hab] = {
                                "dni": dni,
                                "nombre": nombre_completo,
                                "f_ing": f_ing,
                                "f_egr": f_egr,
                                "cant": int(cant),
                                "piso": piso + 1,
                                "habitacion": hab + 1,
                            }
                            asignados.append(habitaciones[piso][hab])
                            asignado = True
                            break
                    if asignado:
                        break

        return asignados, habitaciones

    except FileNotFoundError:
        print("El archivo de huéspedes no existe.")
        return [], []
    except Exception as e:
        print("Ocurrió un error al asignar habitaciones:", e)
        return [], []


def piso_mas_ocupado(habs: list) -> int:
    """
    Devuelve el piso con mayor cantidad de habitaciones ocupadas.
    """
    max_piso = 1
    max_ocupadas = 0

    for i, piso in enumerate(habs, start=1):
        ocupadas = sum(1 for x in piso if x is not None)
        if ocupadas > max_ocupadas:
            max_ocupadas = ocupadas
            max_piso = i

    return max_piso


def habitaciones_vacias(habs: list) -> int:
    """
    Devuelve la cantidad total de habitaciones vacías.
    """
    vacias = 0
    for piso in habs:
        for hab in piso:
            if hab is None:
                vacias += 1
    return vacias


def piso_mas_personas(asignados: list) -> int:
    """
    Devuelve el piso que tiene mayor cantidad de personas alojadas.
    """
    personas_por_piso = [0] * 10

    for h in asignados:
        personas_por_piso[h["piso"] - 1] += h["cant"]

    return personas_por_piso.index(max(personas_por_piso)) + 1


def proximos_en_desocupar(asignados: list) -> list:
    """
    Devuelve la lista de habitaciones que se desocupan antes
    o en la fecha ingresada.
    """
    try:
        fecha_actual = input("Ingrese fecha actual (DDMMAAAA): ").strip()
        f_act = datetime.strptime(fecha_actual, "%d%m%Y")

        a_desocupar = []

        for h in asignados:
            f_egr = datetime.strptime(h["f_egr"], "%d%m%Y")
            if f_egr <= f_act:
                a_desocupar.append(h)

        return a_desocupar
    except ValueError:
        print("Fecha inválida.")
        return []


def listado_por_estadia(asignados: list) -> list:
    """
    Ordena los huéspedes según la cantidad de días que se alojan.
    """
    datos = []

    for h in asignados:
        f_ing = datetime.strptime(h["f_ing"], "%d%m%Y")
        f_egr = datetime.strptime(h["f_egr"], "%d%m%Y")
        dias = (f_egr - f_ing).days
        datos.append((dias, h))

    datos.sort(key=lambda x: x[0], reverse=True)
    return datos


def main():
    ruta = "huespedes.csv"
    registrar_huespedes(ruta)

    asignados, habitaciones = asignar_habitaciones(ruta)
    if not asignados:
        return

    print("Piso con más habitaciones ocupadas:", piso_mas_ocupado(habitaciones))
    print("Habitaciones vacías:", habitaciones_vacias(habitaciones))
    print("Piso con mayor cantidad de personas:", piso_mas_personas(asignados))

    print("Próximas habitaciones en desocuparse:")
    for h in proximos_en_desocupar(asignados):
        print(f"Piso {h['piso']} - Habitación {h['habitacion']} - DNI {h['dni']}")

    print("Listado ordenado por cantidad de días:")
    for dias, h in listado_por_estadia(asignados):
        print(f"{h['dni']} - {h['nombre']} - {dias} días")


main()
