import numpy as np

def eliminacion_gaussiana(matriz_aumentada):
    num_ecuaciones, num_variables = matriz_aumentada.shape

    print("Paso a paso - Eliminación Gaussiana:")
    print(matriz_aumentada)
    print("\n---\n")

    for i in range(num_ecuaciones):
        divisor = matriz_aumentada[i, i]
        matriz_aumentada[i, :] /= divisor

        for j in range(i + 1, num_ecuaciones):
            factor = matriz_aumentada[j, i]
            matriz_aumentada[j, :] -= factor * matriz_aumentada[i, :]

        print(matriz_aumentada)
        print("\n---\n")

    return matriz_aumentada

def eliminacion_gaussiana_jordana(matriz_aumentada):
    matriz_aumentada = eliminacion_gaussiana(matriz_aumentada)

    num_ecuaciones, num_variables = matriz_aumentada.shape

    print("Paso a paso - Eliminación Gaussiana-Jordana:")
    print(matriz_aumentada)
    print("\n---\n")

    for i in range(num_ecuaciones - 1, 0, -1):
        for j in range(i - 1, -1, -1):
            factor = matriz_aumentada[j, i]
            matriz_aumentada[j, :] -= factor * matriz_aumentada[i, :]

        print(matriz_aumentada)
        print("\n---\n")

    return matriz_aumentada

# Definir la matriz aumentada [A|B]
matriz_aumentada = np.array([[2, 1, -1, 8],
                             [-3, -1, 2, -11],
                             [-2, 1, 2, -3]], dtype=float)

# Aplicar eliminación gaussiana-jordana con impresiones paso a paso
matriz_reducida = eliminacion_gaussiana_jordana(matriz_aumentada)

# Extraer la solución
solucion = matriz_reducida[:, -1]
print("\nLa solución del sistema es:", solucion)
