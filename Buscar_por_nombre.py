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
                
            
juegos = convertir_csv_diccionarios("vgsales.csv")

encontrar(juegos)