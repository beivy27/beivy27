import numpy as np


def calcular_promedio_temperaturas(temperaturas):
    """
    Calcula la temperatura promedio para cada ciudad durante un período de semanas.

    Parámetros:
    temperaturas: np.array, una matriz 3D que contiene las temperaturas diarias de varias ciudades.
                  La dimensión debe ser (ciudades, días de la semana, semanas).

    Retorna:
    promedios: np.array, un arreglo con el promedio de temperaturas para cada ciudad.
    """
    num_ciudades = temperaturas.shape[0]
    num_semanas = temperaturas.shape[2]

    # Inicializamos un array para almacenar los promedios de cada ciudad por semana
    promedios = np.zeros((num_ciudades, num_semanas))

    # Iteramos sobre cada ciudad y calculamos su promedio por semana
    for i in range(num_ciudades):
        for j in range(num_semanas):
            promedios[i, j] = np.mean(temperaturas[i, :, j])

    return promedios


# Ejemplo de uso
ciudades = ['Ciudad1', 'Ciudad2', 'Ciudad3']
dias_semana = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']
semanas = 4

# Datos aleatorios de temperaturas para 3 ciudades, 7 días de la semana y 4 semanas
temperaturas = np.random.randint(15, 35, size=(len(ciudades), len(dias_semana), semanas))

# Calculamos los promedios
promedios = calcular_promedio_temperaturas(temperaturas)

# Mostramos el resultado
for i, ciudad in enumerate(ciudades):
    print(f"Promedios de {ciudad}:")
    for j in range(semanas):
        print(f"  Semana {j + 1}: {promedios[i, j]:.2f} °C")
