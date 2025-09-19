"""
Resolver el siguiente problema, utilizando funciones:
Se desea llevar un registro de los socios que visitan un club cada día. Para ello, se
ingresa el número de socio de cinco dígitos hasta ingresar un cero como fin de car-
ga. Se solicita:
a. Informar para cada socio, cuántas veces ingresó al club. Cada socio debe
aparecer una sola vez en el informe.
b. Solicitar un número de socio que se dio de baja del club y eliminar todos sus
ingresos. Mostrar los registros de entrada al club antes y después de
eliminarlo. Informar cuántos ingresos se eliminaron.
"""
CODIGO_FIN = 0
LONGITUD_SOCIO = 5

def registrar_socios() -> list[int]:
    """
    Permite ingresar números de socios de 5 dígitos y los almacena en una lista.

    La entrada termina cuando el usuario ingresa 0.
    """
    socios = []
    while True:
        entrada = input(f"Ingrese el número de socio ({LONGITUD_SOCIO} dígitos, {CODIGO_FIN} para finalizar): ")

        if entrada == str(CODIGO_FIN):
            print("Fin del ingreso de socios.")
            break

        if not entrada.isdigit() or len(entrada) != LONGITUD_SOCIO:
            print(f"Error: El número de socio debe tener exactamente {LONGITUD_SOCIO} dígitos numéricos.")
            continue

        socio = int(entrada)
        socios.append(socio)
        print(f"Socio {socio} registrado exitosamente.")

    return socios


def contar_ingresos_socios(lista_socios: list[int]) -> dict[int, int]:
    """
    Cuenta cuántas veces cada socio ingresó y muestra los resultados.
    """
    if not lista_socios:
        print("No hay socios registrados para contar.")
        return {}

    conteo = {}
    for socio in lista_socios:
        conteo[socio] = conteo.get(socio, 0) + 1

    print("\nCantidad de ingresos por socio:")
    for socio, cantidad in sorted(conteo.items()):
        print(f"Socio {socio} ingresó {cantidad} veces.")

    return conteo


def eliminar_registro_socio(conteo_socios: dict[int, int]) -> None:
    """
    Elimina los ingresos de un socio específico, mostrando antes y después.
    """
    if not conteo_socios:
        print("No hay registros para eliminar.")
        return

    print("\nRegistros antes de eliminar:")
    for socio, cantidad in sorted(conteo_socios.items()):
        print(f"Socio {socio}: {cantidad} ingresos")

    entrada = input("\nIngrese el número de socio que desea eliminar: ")
    if not entrada.isdigit():
        print("Error: Ingrese un número válido.")
        return

    socio_eliminar = int(entrada)
    eliminados = conteo_socios.pop(socio_eliminar, None)

    if eliminados is not None:
        print(f"\nSe eliminaron {eliminados} ingresos del socio {socio_eliminar}.")
    else:
        print(f"\nEl socio {socio_eliminar} no existe en los registros.")

    print("\nRegistros después de eliminar:")
    for socio, cantidad in sorted(conteo_socios.items()):
        print(f"Socio {socio}: {cantidad} ingresos")


def mostrar_opciones(menu: list[str]) -> None:
    """Muestra las opciones del menú principal."""
    for idx, opcion in enumerate(menu, 1):
        print(f"{idx} - {opcion}")


def main():
    """Función principal que gestiona el menú de socios."""
    lista_socios = []
    conteo_socios = {}
    menu_opciones = [
        "Ingresar socios",
        "Contar cantidad de ingresos",
        "Eliminar socio",
        "Salir"
    ]

    while True:
        mostrar_opciones(menu_opciones)
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            lista_socios = registrar_socios()
        elif opcion == "2":
            conteo_socios = contar_ingresos_socios(lista_socios)
        elif opcion == "3":
            eliminar_registro_socio(conteo_socios)
        elif opcion == "4":
            print("Saliendo...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")


main()
