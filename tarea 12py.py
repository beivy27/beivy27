# Definimos las ciudades, días y semanas
ciudades = ['Ciudad1', 'Ciudad2', 'Ciudad3']
dias_semana = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']
semanas = 4  # Supongamos que tenemos 4 semanas de datos

# Creación de la matriz 3D para almacenar las temperaturas (ciudades, días, semanas)
import random

# Temperaturas aleatorias entre 15 y 35 grados
temperaturas = [[[random.randint(15, 35) for dia in range(len(dias_semana))] for semana in range(semanas)] for ciudad in range(len(ciudades))]

# Calcular el promedio de temperaturas para cada ciudad por semana
for ciudad in range(len(ciudades)):
    print(f"Promedio de temperaturas para {ciudades[ciudad]}:")
    for semana in range(semanas):
        suma_temperaturas = 0
        for dia in range(len(dias_semana)):
            suma_temperaturas += temperaturas[ciudad][semana][dia]
        promedio = suma_temperaturas / len(dias_semana)
        print(f"  Semana {semana + 1}: {promedio:.2f}°C")

# Muestra la matriz de temperaturas para verificar
print("\nDatos de temperaturas:")
for ciudad in range(len(ciudades)):
    print(f"{ciudades[ciudad]}: {temperaturas[ciudad]}")