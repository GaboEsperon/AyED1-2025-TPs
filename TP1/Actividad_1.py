"""
Desarrollar una función que reciba tres números enteros positivos y devuelva el mayor de los tres,
sólo si éste es único (es decir el mayor estricto).Devolver -1 en caso de no haber ninguno.
No utilizar operadores lógicos (and, or, not). Desarrollar también un programa para ingresar los tres valores,
invocar a la función y mostrar el máximo hallado, o un mensaje informativo si éste no existe.
"""
def num_max_estrict(lista_num):
    num_mayor = max(lista_num)
    if lista_num.count(num_mayor) > 1:
        return -1
    else:
        return num_mayor
    
def recibir_num(): 
    numbers = []
    while len(numbers) < 3:
        try:
            new_num = int(input(f"ingrese un numer {len(numbers)+1}: "))
            if new_num <= 0:
                print("el numero ingresado debe ser positivo")
            else:
                numbers.append(new_num)
        except ValueError: 
            print("Error: el numero ingresado debe ser entero")
    return numbers
    
def main():
    nums = recibir_num()
    resultado = num_max_estrict(nums)
    if resultado != -1:
        print("El número mayor estricto es:", resultado)
    else:
        print("No hay un número mayor estricto")


main()



    
    


        
