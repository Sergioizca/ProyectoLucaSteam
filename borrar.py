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
        for i in juegos:
            if i["nombre"] == nombre_borrar and a:
                juegos.remove(i)
                print("Se ha borrado la entrada seleccionada")
                continuar = pregunta_continuar("¿Quieres eliminar otra entrada? s/n:\n")
            else:
                print("Ese videojuego no consta en nuestro archivo")
                continuar = pregunta_continuar("¿Quieres eliminar otra entrada? s/n:\n")
                print("Ese videojuego no consta en nuestro archivo. Vuelve a intentarlo")


def main():
    borrar(convertir_csv_diccionarios("prueba.csv"))


main()
