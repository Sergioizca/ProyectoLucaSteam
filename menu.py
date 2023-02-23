# menu
from convertir_csv_diccionario import *
from borrar import *
from mostrar_lista_juegos import *
from obtener_cambio import *
from modificar_juego import *
from Añadir_juego import *


def menu(lista):
    seguir = True
    while seguir:
        print("\nBienvenido al menú del listado de videojuegos. Teclee el número al que desea acceder: \n\n 1. Añadir videojuego a la lista \n\n 2. Borrar videojuego de la lista \n\n 3. Modificar videojuego de la lista \n\n 4. Ver listado completo de videojuegos \n\n 5. Salir del menú \n ")
        valor = int(input("Selecciona una opción: "))
        if (valor > 0 and valor <= 5):
            match valor:
                case 1 | None:
                    print("Añadir videojuego a la lista")
                    agregar_juego(lista)
                case 2 | None:
                    print("Borrar videojuego de la lista")
                    borrar_de_dic(lista)
                case 3 | None:
                    print("Modificar videojuego de la lista")
                    modificar_juego(encontrar(lista), obtener_cambio())
                case 4 | None:
                    print("Ver listado completo de videojuegos")
                    mostrar_lista_juegos()
                case 5 | None:
                    print("Has salido correctamente")
                    seguir = False
        else:
            print("----------Selecciona una opción correcta----------")


if __name__ == "__main__":
    def main():
        lista = convertir_csv_diccionarios("vgsales.csv")
        menu(lista)
    main()

# Pdte ampliar el menú (si fuera necesario), try-except.
