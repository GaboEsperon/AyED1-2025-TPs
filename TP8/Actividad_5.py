"""
En geometría un vector es un segmento de recta orientado que va desde un punto
A hasta un punto B. Los vectores en el plano se representan mediante un par orde-
nado de números reales (x, y) llamados componentes. Para representarlos basta
con unir el origen de coordenadas con el punto indicado en sus componentes:
Dos vectores son ortogonales cuando son perpendiculares entre sí. Para determi-
narlo basta calcular su producto escalar y verificar si es igual a 0. Ejemplo:
A = (2,3) y B = (-3,2) => 2 * (-3) + 3 * 2 = -6 + 6 = 0 => Son ortogonales
"""
def son_vectores_ortogonales(vector_a: tuple[float, float], vector_b: tuple[float, float]) -> bool:
    """
    Determina si dos vectores son ortogonales (perpendiculares).

    Parameters:
        vector_a (tuple): Primer vector (valores reales o enteros).
        vector_b (tuple): Segundo vector (valores reales o enteros).

    Returns:
        bool: True si el producto escalar es igual (o casi igual) a 0, False en caso contrario.
    """
    if len(vector_a) != len(vector_b):
        raise ValueError("Ambos vectores deben tener la misma cantidad de componentes.")

    producto_escalar = sum(a * b for a, b in zip(vector_a, vector_b))
    return abs(producto_escalar) < 1e-9


def main():
    """
    Programa principal para probar la función son_vectores_ortogonales().
    """
    v1 = (3, 4)
    v2 = (-4, 3)
    v3 = (1, 1)

    print(f"{v1} y {v2} son ortogonales: {son_vectores_ortogonales(v1, v2)}")
    print(f"{v1} y {v3} son ortogonales: {son_vectores_ortogonales(v1, v3)}")


if __name__ == "__main__":
    main()
