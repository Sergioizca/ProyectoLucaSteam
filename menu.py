# menu
from convertir_csv_diccionario import *
from borrar import *
from mostrar_lista_juegos import *
from obtener_cambio import *
from modificar_juego import *


seguir=True
lista=convertir_csv_diccionarios("vgsales.csv")
while seguir:
    print(" **** MENU **** \n **** 1.Añadir **** \n **** 2.Borrar **** \n **** 3.Modificar **** \n **** 4.Listar **** \n **** 5.Salir **** \n ***************")
    valor=int(input("Selecciona una opción: "))
    if (valor>0 and valor<=5):
        match valor:
            case 1 | None:
                # agregar_juego()
                print("Añadir")
            case 2 | None:
                print("Eliminar")
                borrar_de_dic(lista)
            case 3 | None:
                print("Modificar")
                modificar_juego(encontrar(lista), obtener_cambio())
            case 4 | None:
                print("Listar")
                mostrar_lista_juegos(lista)
            case 5 | None:
                print("Has salido correctamente")
                seguir=False
    else:
        print("----------Selecciona una opción correcta----------")

# Pdte ampliar el menú (si fuera necesario), try-except.
