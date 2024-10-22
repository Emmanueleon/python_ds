import os  # importar la librería os

cpu_num = os.cpu_count()  # obtener el número de CPU en el sistema
# imprimir el número de CPU
print(f"Mi computadora tiene {cpu_num} núcleos de CPU")
