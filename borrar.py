import csv
import os
from convertir_csv_diccionario import *

# Introducir bucle que pregunte si quiere salir con teclado
# o si quiere continuar eliminando otro juego


def pregunta_continuar(mensaje):
    respuesta = input(mensaje).lower()
    if respuesta == "n":
        return False
    return True


def borrar(juegos):
    continuar = True
    while continuar:
        nombre_borrar = input(
            "Inserta el nombre del juego que deseas borrar: \n")
        juego_encontrado = False
        for juego in juegos:
            if juego["nombre"] == nombre_borrar:
                juegos.remove(juego)
                juego_encontrado = True
                break
        if juego_encontrado:
            continuar = pregunta_continuar(
                "Se ha borrado la entrada seleccionada. ¿Quieres eliminar otra entrada? s/n:\n")
        else:
            continuar = pregunta_continuar(
                "Ese juego no consta en nuestro archivo. ¿Quieres intentarlo de nuevo? s/n:\n")


def main():
    borrar(convertir_csv_diccionarios("prueba.csv"))


main()
