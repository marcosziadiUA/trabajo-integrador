# test_sales_manager.py
import pytest
import os
from src.sales_manager import bubble_sort_sucursales, procesar_reporte_ventas, ordenar_archivo

# --- PRUEBAS DE ORDENAMIENTO ---

def test_bubble_sort_sucursales_orden_alfabetico():
    entrada = [
        "Zarate,Harina,1,1,1,100\n",
        "Abasto,Leche,1,1,1,50\n",
        "Rosario,Azucar,1,1,1,80\n"
    ]
    esperado = [
        "Abasto,Leche,1,1,1,50\n",
        "Rosario,Azucar,1,1,1,80\n",
        "Zarate,Harina,1,1,1,100\n"
    ]
    assert bubble_sort_sucursales(entrada) == esperado

def test_bubble_sort_lista_vacia():
    assert bubble_sort_sucursales([]) == []

# --- PRUEBAS DE REPORTE (CORTE DE CONTROL) ---

@pytest.fixture
def csv_prueba(tmp_path):
    """Crea un archivo CSV temporal para pruebas de reporte."""
    d = tmp_path / "data"
    d.mkdir()
    f = d / "compras_test.csv"
    contenido = (
        "Sucursal,Producto,C3,C4,Cantidad,Precio\n"
        "Abasto,Leche,0,0,2,50.0\n"
        "Abasto,Leche,0,0,1,50.0\n"
        "Rosario,Pan,0,0,10,10.0\n"
    )
    f.write_text(contenido, encoding="utf-8")
    return str(f)

def test_procesar_reporte_valores_correctos(csv_prueba):
    """Verifica que los cálculos del reporte sean correctos."""
    resultado = procesar_reporte_ventas(csv_prueba)
    
    # Abasto: (2+1)*50 = 150
    # Rosario: 10*10 = 100
    # Total = 250
    assert resultado["total_sucursales"] == 2
    assert resultado["importe_general"] == 250.0

# --- PRUEBAS DE ORDENAR ARCHIVO ---

def test_ordenar_archivo_crea_file(tmp_path):
    """Verifica que la función modular de ordenar cree el archivo de salida."""
    ent = tmp_path / "suc_des.csv"
    ent.write_text("S\nZ,P,0,0,1,10\nA,P,0,0,1,10", encoding="utf-8")
    sal = tmp_path / "suc_ord.csv"
    
    exito = ordenar_archivo(str(ent), str(sal))
    
    assert exito is True
    assert os.path.exists(str(sal))
    with open(sal, 'r') as f:
        lineas = f.readlines()
        assert "A,P" in lineas[1]
