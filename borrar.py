import csv
from convertir_csv_diccionario import *

# Introducir bucle que pregunte si quiere salir con teclado
# o si quiere continuar eliminando otro juego

def borrar(juegos):
    a = True
    while True:
        nombre_borrar = input(
            "Inserta el nombre del juego que deseas borrar: \n")
        for i in juegos:
            if i["nombre"] == nombre_borrar and a:
                juegos.remove(i)
                print("Se ha borrado la entrada seleccionada")
                a = False
            else:
                print("Ese videojuego no consta en nuestro archivo. Vuelve a intentarlo")


def main():
    borrar(convertir_csv_diccionarios("prueba.csv"))


main()
