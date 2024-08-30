# Crear la matriz 3x3
matriz = [
    [9, 2, 3],
    [4, 5, 6],
    [7, 8, 1]
]

# Función para ordenar una fila de la matriz utilizando Bubble Sort
def ordenar_fila(matriz, fila_index):
    fila = matriz[fila_index]
    n = len(fila)
    for i in range(n):
        for j in range(0, n-i-1):
            if fila[j] > fila[j+1]:
                fila[j], fila[j+1] = fila[j+1], fila[j]
    matriz[fila_index] = fila

# Mostrar la matriz original
print("Matriz original:")
for fila in matriz:
    print(fila)

# Ordenar la segunda fila (índice 1)
ordenar_fila(matriz, 1)

# Mostrar la matriz después de ordenar la fila
print("\nMatriz después de ordenar la fila 2:")
for fila in matriz:
    print(fila)
