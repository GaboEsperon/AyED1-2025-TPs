"""
Intercalar los elementos de una lista entre los elementos de otra. La intercalación
deberá realizarse exclusivamente mediante la técnica de rebanadas y no se creará
una lista nueva sino que se modificará la primera. Por ejemplo, si lista1 = [8, 1, 3]
y lista2 = [5, 9, 7], lista1 deberá quedar como [8, 5, 1, 9, 3, 7]. Las listas pueden
tener distintas longitudes.
"""
def intercalar(lista1: list[int], lista2: list[int]) -> None:
    """
    Combina dos listas intercalando los elementos de lista2 dentro de lista1.

    - Si lista2 es más corta, solo se intercalan los elementos existentes.
    - Si lista2 es más larga, los elementos restantes se agregan al final.
    - No devuelve nada, modifica lista1 en sitio.
    """
    if not lista1 and not lista2:
        return

    len_mas_corto = min(len(lista1), len(lista2))

    for i in range(len_mas_corto):
        lista1[2 * i + 1:2 * i + 1] = [lista2[i]]

    if len(lista2) > len_mas_corto:
        lista1.extend(lista2[len_mas_corto:])


def main():
    """Función principal que prueba la intercalación de listas."""

    # Ejemplos de prueba sin pedir entrada manual
    lista_a = [1, 3, 5]
    lista_b = [2, 4, 6, 8, 10]

    print("Lista A original:", lista_a)
    print("Lista B original:", lista_b)

    intercalar(lista_a, lista_b)
    print("Lista intercalada:", lista_a)

    # Otro ejemplo
    lista_c = [10, 20]
    lista_d = [15, 25, 35]
    intercalar(lista_c, lista_d)
    print("Segunda intercalación:", lista_c)

    # Ejemplo con listas vacías
    lista_e = []
    lista_f = [1, 2, 3]
    intercalar(lista_e, lista_f)
    print("Intercalación con lista vacía:", lista_e)



main()
