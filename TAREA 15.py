# Crear un diccionario llamado informacion_personal
informacion_personal = {
    "nombre": "Beivy Rivera",
    "edad": 35,
    "ciudad": "Quito",
    "profesion": "Ingeniera"
}

# Acceder al valor de la clave "ciudad" y modificarlo
informacion_personal["ciudad"] = "Quito"

# Agregar una nueva clave-valor para la "profesion"
informacion_personal["profesion"] = "Desarrollador de Software"

# Verificar si la clave "telefono" existe y agregarla si no existe
if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "0996148438"

# Eliminar la clave "edad"
del informacion_personal["edad"]

# Imprimir el diccionario final
print(informacion_personal)

