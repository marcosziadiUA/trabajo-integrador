# sales_manager.py

# --- MÓDULO DE LÓGICA DE ORDENAMIENTO ---

def bubble_sort_sucursales(filas_datos):
    """
    Lógica pura de ordenamiento (Algoritmo de Burbuja).
    Recibe una lista de strings y devuelve una lista ordenada por la primera columna.
    """
    n = len(filas_datos)
    datos = list(filas_datos)
    
    for i in range(n):
        for j in range(0, n - i - 1):
            try:
                sucursal_actual = datos[j].split(',')[0].strip()
                sucursal_siguiente = datos[j + 1].split(',')[0].strip()

                if sucursal_actual > sucursal_siguiente:
                    datos[j], datos[j + 1] = datos[j + 1], datos[j]
            except IndexError:
                continue
    return datos

def ordenar_archivo(path_entrada, path_salida):
    """Lee un archivo, lo ordena por sucursal y guarda el resultado."""
    try:
        with open(path_entrada, 'r', encoding='utf-8') as f:
            lineas = f.readlines()
        
        if not lineas:
            return False

        encabezado = lineas[0]
        cuerpo = lineas[1:]
        datos_ordenados = bubble_sort_sucursales(cuerpo)

        with open(path_salida, 'w', encoding='utf-8') as f_salida:
            f_salida.write(encabezado)
            for linea in datos_ordenados:
                if not linea.endswith('\n'):
                    linea += '\n'
                f_salida.write(linea)
        return True
    except Exception as e:
        print(f"Error al ordenar: {e}")
        return False
