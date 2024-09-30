# Escritura de Archivo de Texto
# Crea un archivo llamado 'my_notes.txt' y escribe tres líneas de texto en él.
with open('my_notes.txt', 'w') as file:
    # Escribir tres líneas de notas personales en el archivo
    file.write("Primera línea: Estoy practicando la manipulación de archivos en Python.\n")
    file.write("Segunda línea: Python tiene métodos sencillos para lectura y escritura de archivos.\n")
    file.write("Tercera línea: Este es un ejercicio práctico para mejorar mis habilidades.\n")

# Lectura de Archivo de Texto
# Abre el archivo 'my_notes.txt' para lectura y lee su contenido línea por línea.
with open('my_notes.txt', 'r') as file:
    # Leer línea por línea el contenido del archivo
    line = file.readline()  # Leer la primera línea
    while line:
        # Imprimir la línea en la consola eliminando los saltos de línea extra con strip()
        print(line.strip())
        line = file.readline()  # Leer la siguiente línea

# No es necesario cerrar los archivos manualmente porque 'with' se encarga de ello.

