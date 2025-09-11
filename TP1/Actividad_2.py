"""
Desarrollar una función que reciba tres números enteros positivos correspondientes al día, mes, año de una fecha 
y verifique si corresponden a una fecha válida.
Debe tenerse en cuenta la cantidad de días de cada mes, incluyendo los años bisiestos.
Devolver True o False según la fecha sea correcta o no.
Realizar también un programa para verificar el comportamiento de la función.
"""
def recibir_fecha():
    while True:
        try:
            dia = int(input("ingrese el dia: "))
            mes = int(input("ingrese el mes: "))
            anio = int(input("ingrese el año: "))
            return dia, mes, anio
        except ValueError:
            print("los numeros ingresado deben ser enteros") 
        
           
    
def validar_fecha(dia, mes , anio):
    if dia < 1 or mes < 1 or anio < 1:
        return False
    if mes < 1 or mes > 12:
        return False
    
    es_bisiesto = validar_bisiesto(anio)
    dias_por_mes = (31, 29 if es_bisiesto else 28, 31, 30, 31, 30,31, 31, 30, 31, 30, 31)
    
    
    if dia > dias_por_mes[mes - 1]:
        return False
    
    return True
        
        
def validar_bisiesto(anio):
    return anio % 4 == 0 and (anio % 100 != 0 or anio % 400 == 0)

def main():
    dia, mes, anio = recibir_fecha()
    resultado = validar_fecha(dia, mes, anio)
    if resultado:
        print("la fecha es valida")
    else:
        print("la fecha es invalida")


main()