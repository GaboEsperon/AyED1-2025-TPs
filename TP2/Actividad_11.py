"""
Resolver el siguiente problema, diseñando las funciones a utilizar:
Una clínica necesita un programa para atender a sus pacientes. Cada paciente que
ingresa se anuncia en la recepción indicando su número de afiliado (número entero
de 4 dígitos) y además indica si viene por una urgencia (ingresando un 0) o con
turno (ingresando un 1). Para finalizar se ingresa -1 como número de socio. Luego
se solicita:
a. Mostrar un listado de los pacientes atendidos por urgencia y un listado de
los pacientes atendidos por turno en el orden que llegaron a la clínica.
b. Realizar la búsqueda de un número de afiliado e informar cuántas veces fue
atendido por turno y cuántas por urgencia. Repetir esta búsqueda hasta
que se ingrese -1 como número de afiliado.
"""
TIPO_URGENCIA = 0
TIPO_TURNO = 1

def ingresar_pacientes() -> list[tuple[int, int]]:
    """
    Solicita datos de pacientes y los retorna como lista de tuplas (afiliado, tipo_atencion).

    Validaciones:
    - Número de afiliado: 4 dígitos.
    - Tipo de atención: 0 para urgencia, 1 para turno.
    """
    lista_pacientes = []
    while True:
        try:
            afiliado = input("Ingrese su número de afiliado (4 dígitos) o -1 para finalizar: ")
            if afiliado == "-1":
                print("Fin del ingreso de pacientes.")
                break

            if not afiliado.isdigit() or len(afiliado) != 4:
                print("El número de afiliado debe contener 4 dígitos numéricos.")
                continue

            afiliado_int = int(afiliado)

            atencion = input("Ingrese 0 para urgencia o 1 con turno: ")
            if atencion not in ("0", "1"):
                print("Opción inválida. Ingrese 0 para urgencia o 1 con turno.")
                continue

            tipo = int(atencion)
            tipo_texto = "urgencia" if tipo == TIPO_URGENCIA else "turno"
            print(f"Paciente con número {afiliado_int} viene por {tipo_texto}.")

            lista_pacientes.append((afiliado_int, tipo))

        except ValueError:
            print("Error: Ingrese un número válido.")

    return lista_pacientes


def mostrar_pacientes(lista: list[tuple[int, int]]) -> None:
    """Muestra los pacientes por tipo de atención de manera ordenada."""
    urgencia = [p for p in lista if p[1] == TIPO_URGENCIA]
    turno = [p for p in lista if p[1] == TIPO_TURNO]

    print("\nPacientes atendidos por urgencia:")
    for idx, p in enumerate(urgencia, 1):
        print(f"{idx} - Afiliado: {p[0]}")

    print("\nPacientes atendidos con turno:")
    for idx, p in enumerate(turno, 1):
        print(f"{idx} - Afiliado: {p[0]}")


def buscar_paciente(lista: list[tuple[int, int]]) -> None:
    """Permite buscar cuántas veces un afiliado fue atendido por urgencia y turno."""
    while True:
        afiliado = input("Ingrese el número de afiliado a buscar o -1 para finalizar: ")
        if afiliado == "-1":
            print("Fin de la búsqueda.")
            break

        if not afiliado.isdigit():
            print("Error: Ingrese un número válido.")
            continue

        afiliado_int = int(afiliado)
        contador_urgencia = sum(1 for p in lista if p[0] == afiliado_int and p[1] == TIPO_URGENCIA)
        contador_turno = sum(1 for p in lista if p[0] == afiliado_int and p[1] == TIPO_TURNO)

        if contador_urgencia == 0 and contador_turno == 0:
            print(f"Afiliado {afiliado_int} no encontrado.")
        else:
            print(f"Afiliado {afiliado_int}: {contador_urgencia} urgencia, {contador_turno} turno.")


def mostrar_opciones(menu: list[str]) -> None:
    """Muestra las opciones del menú principal."""
    for idx, opcion in enumerate(menu, 1):
        print(f"{idx} - {opcion}")


def main():
    """Función principal que ejecuta el menú de pacientes."""
    lista_pacientes = []
    menu_opciones = [
        "Ingresar datos de pacientes.",
        "Mostrar listados de pacientes atendidos.",
        "Buscar un número de afiliado.",
        "Salir.",
    ]

    while True:
        mostrar_opciones(menu_opciones)
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            lista_pacientes = ingresar_pacientes()
        elif opcion == "2":
            if lista_pacientes:
                mostrar_pacientes(lista_pacientes)
            else:
                print("No hay pacientes ingresados.")
        elif opcion == "3":
            if lista_pacientes:
                buscar_paciente(lista_pacientes)
            else:
                print("No hay pacientes ingresados.")
        elif opcion == "4":
            print("Saliendo...")
            break
        else:
            print("Opción inválida. Intente de nuevo.")


main()
