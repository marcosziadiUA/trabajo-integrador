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
