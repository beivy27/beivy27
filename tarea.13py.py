
# Definir los nombres de las ciudades y el tamaño de las semanas y días
ciudades = ["Ciudad A", "Ciudad B", "Ciudad C"]
semanas = 4
dias_semana = 7

# Generar datos de temperaturas aleatorias para 3 ciudades durante 4 semanas
np.random.seed(42)  # Para reproducibilidad
temperaturas = np.random.randint(15, 35, (len(ciudades), dias_semana, semanas))

# Función para calcular el promedio de temperaturas por ciudad y semana
def calcular_promedio_temperaturas(temperaturas, ciudades):
    for ciudad_index, ciudad in enumerate(ciudades):
        print(f"Promedio de temperaturas para {ciudad}:")
        for semana in range(semanas):
            suma_temperaturas = 0
            for dia in range(dias_semana):
                suma_temperaturas += temperaturas[ciudad_index, dia, semana]
            promedio_semana = suma_temperaturas / dias_semana
            print(f"  Semana {semana + 1}: {promedio_semana:.2f}°C")
        print()
# Llamar a la función para calcular los promedios
 calcular_promedio_temperaturas(temperaturas, ciudades)
Promedio de temperaturas para Ciudad A:
  Semana 1: 22.29°C
  Semana 2: 25.86°C
  Semana 3: 27.57°C
  Semana 4: 22.86°C

Promedio de temperaturas para Ciudad B:
  Semana 1: 23.43°C
  Semana 2: 25.43°C
  Semana 3: 22.14°C
  Semana 4: 24.86°C

Promedio de temperaturas para Ciudad C:
  Semana 1: 23.57°C
  Semana 2: 27.29°C
  Semana 3: 24.57°C
  Semana 4: 26.00°C





