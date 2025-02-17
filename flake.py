import subprocess
import datetime
import sys
import os

# Verificar si se proporcionó un archivo como argumento
if len(sys.argv) < 2:
    print("Uso: python flake.py <archivo_a_analizar>")
    sys.exit(1)

# Obtener el archivo de la línea de comandos
archivo_analizado = sys.argv[1]

# Definir la ruta absoluta para el archivo de salida
archivo_salida = os.path.join(os.getcwd(), "flake-test.txt")

# Obtener fecha actual
fecha_actual = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Ejecutar flake8 y capturar salida
resultado = subprocess.run(["flake8", archivo_analizado], capture_output=True, text=True)

# Formatear el contenido a escribir
contenido = (
    f"Nombre del archivo analizado: {archivo_analizado}\n"
    f"Fecha: {fecha_actual}\n"
    f"Resultado:\n{resultado.stdout if resultado.stdout else 'Sin errores detectados.'}\n"
    "-------------------------------------------------------------\n"
)

# Verificar si flake8 generó salida antes de escribir en el archivo
if resultado.stdout or "Sin errores detectados." in contenido:
    print("Guardando el resultado en flake-test.txt...\n")

    # Asegurar que el archivo se cree si no existe
    with open(archivo_salida, "a", encoding="utf-8") as file:
        file.write(contenido)

    print("Archivo flake-test.txt actualizado correctamente.")
else:
    print("No hubo salida de flake8, nada que escribir.")
