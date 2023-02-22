import csv
import os
from convertir_csv_diccionario import *
from obtener_cambio import *
def encontrar(juegos):
    print (juegos)
    nombre_encontrar = input(
            "Inserta el nombre del juego que deseas encontrar: \n")    
    for juego in juegos:
            if juego["nombre"] == nombre_encontrar:
                return juego
def modificar_juego(juegos, cambio):
    if cambio == 1:
        juegos.update(
            {"nombre": input("Ingrese el nuevo nombre: ")})
        print(f"\nElemento editado correctamente: {juegos}\n")
    elif cambio == 2:
        juegos.update(
            {"plataforma": input("Ingrese la nueva plataforma: ")})
        print(f"\nElemento editado correctamente: {juegos}\n")
    elif cambio == 3:
        juegos.update({"año": input("Ingrese el nuevo año: ")})
        print(f"\nElemento editado correctamente: {juegos}\n")
    elif cambio == 4:
        juegos.update(
            {"genero": input("Ingrese el nuevo genero: ")})
        print(f"\nElemento editado correctamente: {juegos}\n")
    elif cambio == 5:
        juegos.update(
            {"publisher": input("Ingrese la nueva empresa: ")})
        print(f"\nElemento editado correctamente: {juegos}\n")
    elif cambio == 6:
        juegos.update(
            {"na_sales": input("Ingrese las nuevas ventas de NA: ")})
        print(f"\nElemento editado correctamente: {juegos}\n")
    elif cambio == 7:
        juegos.update(
            {"eu_sales": input("Ingrese las nuevas ventas de EU: ")})
        print(f"\nElemento editado correctamente: {juegos}\n")
    elif cambio == 8:
        juegos.update(
            {"jp_sales": input("Ingrese las nuevas ventas de Japon: ")})
        print(f"\nElemento editado correctamente: {juegos}\n")
    elif cambio == 9:
        juegos.update({"other_sales": input(
            "Ingrese las nuevas ventas de otras regiones: ")})
        print(f"\nElemento editado correctamente: {juegos}\n")
    elif cambio == 10:
        juegos.update(
            {"global_sales": input("Ingrese las nuevas ventas globales: ")})
        print(f"\nElemento editado correctamente: {juegos}\n")
    else:
        print(f"\nSeleccione un elemento correcto")
"""
def main():
    juegos = convertir_csv_diccionarios("vgsales.csv")
    diccionario = encontrar(juegos)
    print(f"\n{diccionario}\n")
    cambio = obtener_cambio()
    modificar_juego(diccionario, cambio)
main()"""
