"""
Todo programa Python es susceptible de ser interrumpido mediante la pulsación de
las teclas Ctrl-C, lo que genera una excepción del tipo KeyboardInterrupt. Realizar
un programa para imprimir los números enteros entre 1 y 100000, y que solicite
confirmación al usuario antes de detenerse cuando se presione Ctrl-C.
"""
def imprimir_numeros(num_inicio: int) -> None:
    """
    Imprime números consecutivos desde `num_inicio` hasta 100000.
    Si se presiona Ctrl-C, solicita confirmación antes de detener el programa.
    """
    while num_inicio <= 100_000:
        try:
            print(num_inicio)
            num_inicio += 1
        except KeyboardInterrupt:
            confirmacion = input("\nDesea frenar el programa? (y/n): ")
            if confirmacion.lower() == "y":
                print("Programa detenido.")
                return
            else:
                print("Continuando...")
