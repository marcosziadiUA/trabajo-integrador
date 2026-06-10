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

# --- MÓDULO DE PROCESAMIENTO (CORTE DE CONTROL) ---

def procesar_reporte_ventas(path_archivo):
    """
    Ejecuta la lógica de Corte de Control y retorna un diccionario con el resumen
    para facilitar el testing, además de imprimir en consola.
    """
    resumen = {"total_sucursales": 0, "importe_general": 0.0}
    
    try:
        with open(path_archivo, mode='r', encoding='utf-8') as file:
            lineas = file.readlines()
            if len(lineas) <= 1: return resumen
            
            indice = 1
            total_general = 0
            cant_sucursales = 0

            while indice < len(lineas):
                data = lineas[indice].strip().split(",")
                if not data or data == ['']: break
                
                prsuc_actual = data[0]
                totsuc_unidades = 0
                total_suc_pesos = 0
                myprod, myimpor = None, -1
                mnprod, mnimpor = None, float('inf')
                cant_sucursales += 1
                
                print(f"\nSUCURSAL: {prsuc_actual}")
                print("-" * 40)

                while indice < len(lineas) and lineas[indice].split(",")[0] == prsuc_actual:
                    data = lineas[indice].strip().split(",")
                    prcod_actual = data[1]
                    totuni_producto = 0
                    totpes_producto = 0

                    while indice < len(lineas) and lineas[indice].split(",")[0] == prsuc_actual and lineas[indice].split(",")[1] == prcod_actual:
                        data = lineas[indice].strip().split(",")
                        cant = int(data[4])
                        precio = float(data[5])
                        totuni_producto += cant
                        totpes_producto += (cant * precio)
                        indice += 1

                    print(f"Prod: {prcod_actual} | Unidades: {totuni_producto} | Total: ${round(totpes_producto, 2)}")
                    
                    total_suc_pesos += totpes_producto
                    totsuc_unidades += totuni_producto
                    
                    if totpes_producto > myimpor:
                        myimpor, myprod = totpes_producto, prcod_actual
                    if totpes_producto < mnimpor:
                        mnimpor, mnprod = totpes_producto, prcod_actual

                print(f">>> TOTAL {prsuc_actual}: {totsuc_unidades} unidades.")
                print(f">>> MAYOR COMPRA: {myprod} (${round(myimpor, 2)})")
                print(f">>> MENOR COMPRA: {mnprod} (${round(mnimpor, 2)})")
                total_general += total_suc_pesos

            resumen["total_sucursales"] = cant_sucursales
            resumen["importe_general"] = round(total_general, 2)
            
            print(f"\n{'='*60}")
            print(f"CANTIDAD TOTAL SUCURSALES: {cant_sucursales}")
            print(f"IMPORTE TOTAL GENERAL: ${resumen['importe_general']}")
            print(f"{'='*60}")
            
    except FileNotFoundError:
        print("Error: El archivo no existe.")
    
    return resumen

# --- INTERFAZ DE USUARIO ---

import os

def menu():
    print("\n--- SISTEMA DE GESTIÓN DE COMPRAS ---")
    path_csv = input("Indique el path del csv: ")
    
    if not os.path.exists(path_csv):
        print("El path indicado no es válido.")
        return

    esta_ordenado = input("¿El archivo está ordenado? (S/N): ").upper()
    path_a_procesar = path_csv

    if esta_ordenado == "N":
        path_temp = "temp_ordenado.csv"
        print("Ordenando datos...")
        if ordenar_archivo(path_csv, path_temp):
            path_a_procesar = path_temp
        else:
            print("No se pudo ordenar el archivo.")
            return

    procesar_reporte_ventas(path_a_procesar)

    if esta_ordenado == "N" and os.path.exists("temp_ordenado.csv"):
        os.remove("temp_ordenado.csv")

if __name__ == "__main__":
    menu()
