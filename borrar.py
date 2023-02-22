import csv
from convertir_csv_diccionario import *



def borrar(juegos):
    a = True
    while True:
        nombre_borrar = input("Inserta el nombre del juego que deseas borrar: \n")
        if nombre_borrar in juegos:
            del juegos[nombre_borrar]
            print("Se ha borrado la entrada seleccionada")
            a = False
        else:
            print("Ese videojuego no consta en nuestro archivo. Vuelve a intentarlo")



def main():
    borrar(convertir_csv_diccionarios("prueba.csv"))
    
main()