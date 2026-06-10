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
