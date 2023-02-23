import csv
import os
from convertir_csv_diccionario import *
from obtener_cambio import *

def encontrar(juegos):
    nombre_encontrar = input(
            "Inserta el nombre del juego que deseas encontrar: \n")    
    for juego in juegos:
            if juego["nombre"] == nombre_encontrar:
                print(juego)
                return juego
            
juego = convertir_csv_diccionarios("vgsales.cvs")

encontrar(juego)
