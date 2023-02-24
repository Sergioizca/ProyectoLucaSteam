from convertir_csv_diccionario import *
from borrar import *
from mostrar_lista_juegos import *
from obtener_cambio import *
from modificar_juego import *
from Añadir_juego import *
from buscar_nintendo import *
from buscar_editores import *
from Buscar_5topventas import *
from buscar_siglo_veinte import *
from top5porregiones import *
from listar_juegos_genero import *
from media_ventas_globales import *
from buscar_anios_pares import *


lista1 = convertir_csv_diccionarios('vgsales.csv')
lista2 = convertir_csv_diccionarios('vgsales.csv')

def agregar_fallout4():
    juego = {
        "nombre": "1",
        "plataforma": "1",
        "año": 2015,
        "genero": "1",
        "publisher": "1",
        "na_sales": float(1),
        "eu_sales": float(1),
        "jp_sales": float(1),
        "other_sales": float(1),
        "global_sales": float(1)
        }
    lista2.append(juego)
    print("Se ha agregado el juego 'Fallout 4' para la plataforma 'PS5' a la lista de juegos.")

def asegurar():
    agregar_fallout4()
    print(lista2)
   
    agregar_juego(lista1)
    assert len(lista1) == len(lista2), "Las listas no tienen la misma longitud."
    for dic in lista1:
        assert dic in lista2, f"El diccionario {dic} no está en la lista2."
    print("Las listas son iguales.")

asegurar()
        
