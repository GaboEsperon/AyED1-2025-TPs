"""
Desarrollar las siguientes funciones utilizando tuplas para representar fechas y ho-
rarios, y luego escribir un programa que las vincule:
a. Ingresar una fecha desde el teclado, verificando que corresponda a una fecha
válida.
b. Sumar N días a una fecha.
c. Ingresar un horario desde teclado, verificando que sea correcto.
d. Calcular la diferencia entre dos horarios. Si el primer horario fuera mayor al
segundo se considerará que el primero corresponde al día anterior. En ningún
caso la diferencia en horas puede superar las 24 horas.
"""
from datetime import datetime, date, timedelta

def es_bisiesto(anio: int) -> bool:
    return anio % 4 == 0 and (anio % 100 != 0 or anio % 400 == 0)

def leer_fecha() -> tuple[int]:
    while True:
        fecha_str = input("Ingrese la fecha (DD/MM/AAAA): ")
        try:
            fecha = datetime.strptime(fecha_str, "%d/%m/%Y")
            return (fecha.year, fecha.month, fecha.day)
        except ValueError:
            print("Fecha inválida. Intente nuevamente.")

def sumar_dias_fecha(fecha: tuple[int]) -> tuple[int]:
    anio, mes, dia = fecha
    n = int(input("Ingrese cantidad de días a sumar: "))
    nueva_fecha = date(anio, mes, dia) + timedelta(days=n)
    return (nueva_fecha.year, nueva_fecha.month, nueva_fecha.day)

def leer_horario() -> tuple[int]:
    while True:
        hora_str = input("Ingrese horario (HH:MM): ")
        try:
            h, m = map(int, hora_str.split(":"))
            if 0 <= h <= 23 and 0 <= m <= 59:
                return (h, m)
            else:
                print("Horario fuera de rango. Intente nuevamente.")
        except ValueError:
            print("Formato inválido. Intente nuevamente.")

def diferencia_horarios(horario1: tuple[int]) -> tuple[int]:
    segundo = input("Ingrese el segundo horario (HH:MM): ")
    try:
        h2, m2 = map(int, segundo.split(":"))
        if not (0 <= h2 <= 23 and 0 <= m2 <= 59):
            raise ValueError

        h1, m1 = horario1
        minutos1 = h1 * 60 + m1
        minutos2 = h2 * 60 + m2

        if minutos2 < minutos1:
            minutos2 += 24 * 60

        diff = minutos2 - minutos1
        return (diff // 60, diff % 60)
    except ValueError:
        print("Horario inválido.")
        return None

def main():
    fecha = None
    horario = None
    while True:
        print("\n--- MENÚ ---")
        print("1. Ingresar fecha válida")
        print("2. Sumar N días a fecha")
        print("3. Ingresar horario válido")
        print("4. Calcular diferencia entre horarios")
        print("5. Salir")

        try:
            opcion = int(input("Seleccione opción: "))
        except ValueError:
            print("Debe ingresar un número.")
            continue

        if opcion == 1:
            fecha = leer_fecha()
            print("Fecha registrada:", fecha)
        elif opcion == 2:
            if fecha:
                print("Nueva fecha:", sumar_dias_fecha(fecha))
            else:
                print("Primero ingrese una fecha válida (opción 1).")
        elif opcion == 3:
            horario = leer_horario()
            print("Horario registrado:", horario)
        elif opcion == 4:
            if horario:
                diff = diferencia_horarios(horario)
                if diff:
                    print(f"Diferencia: {diff[0]}h {diff[1]}m")
            else:
                print("Primero ingrese un horario válido (opción 3).")
        elif opcion == 5:
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    main()
