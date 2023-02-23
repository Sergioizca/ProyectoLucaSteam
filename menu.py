# menu
from convertir_csv_diccionario import *
from borrar import *
from mostrar_lista_juegos import *
from obtener_cambio import *
from modificar_juego import *
from Añadir_juego import *
from buscar_nintendo import *
from buscar_editores import *
from buscar_5topventas import *
from buscar_siglo_veinte import *
from top5porregiones import *
from listar_juegos_genero import *
from media_ventas_globales import *
from buscar_anios_pares import *




def menu(lista):
    seguir = True
    while seguir:
        print("\n"
              "Bienvenido al menú del listado de videojuegos. Teclee el número al que desea acceder:\n\n"
              "1. Añadir videojuego a la lista \n\n"
              "2. Borrar videojuego de la lista \n\n"
              "3. Modificar videojuego de la lista \n\n"
              "4. Ver listado completo de videojuegos \n\n"
              "5. Ver listado de juegos de Nintendo \n\n"
              "6. Ver listado de Editores\n\n"
              "7. Ver los 5 juegos más vendidos del mundo\n\n"
              "8. Ver juegos del siglo XX\n\n"
              "9. Ver los 5 juegos más vendidos por regiones\n\n"
              "10. Ver listado de juegos de filtrados por género \n\n"
              "11. Ver listado de juegos con ventas mayores a la media \n\n"
              "12. Ver listado de juegos que salieron en años pares\n\n"
              "13. Salir del menú \n "
              )
        valor = int(input("Selecciona una opción: "))
        if (valor > 0 and valor <= 13):
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
                    print("Ver listado de juegos de Nintendo")
                    buscar_nintendo(archivo)
                case 6 | None:
                    print("Ver listado de Editores")
                    buscar_editores(archivo)
                case 7 | None:
                    print("Ver los 5 juegos más vendidos del mundo")
                    buscar_top_5_ventas_globales(archivo)
                case 8 | None:
                    print("Ver juegos del siglo XX")
                    buscar_siglo_veinte(archivo)
                case 9 | None:
                    print("Ver los 5 juegos más vendidos por regiones")
                    elegir_region(archivo)
                case 10 | None:
                    print("Ver listado de juegos de filtrados por género")
                    listar_juegos_genero(archivo)
                case 11 | None:
                    print("Ver listado de juegos con ventas mayores a la media")
                    media_ventas_globales(archivo)
                case 12 | None:
                    print("Ver listado de juegos que salieron en años pares")
                    buscar_anios_pares(archivo)
                case 13 | None:
                    print("Has salido correctamente")
                    seguir = False
        else:
            print("----------Selecciona una opción correcta----------")


if __name__ == "__main__":
    archivo = str("vgsales.csv")
    def main():
        lista = convertir_csv_diccionarios("vgsales.csv")
        menu(lista)
    main()

# Pdte ampliar el menú (si fuera necesario), try-except.
