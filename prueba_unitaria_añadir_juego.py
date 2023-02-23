from convertir_csv_diccionario import *
from Añadir_juego import *


def prueba_cantidad():
    juegos = convertir_csv_diccionarios("vgsales.csv")

    cantidad = 0
    for i in juegos:
        cantidad += 1

    print(cantidad)

    agregar_juego(juegos)


prueba_cantidad()


def agregar_juego_automaticamente(nombre, plataforma, año, genero, empresa, na_sales, eu_sales, jp_sales, other_sales, global_sales):
    juegos = []  # crea una lista vacía para que se agregue el nuevo juego
    juego = {
        "nombre": nombre,
        "plataforma": plataforma,
        "año": año,
        "genero": genero,
        "publisher": empresa,
        "na_sales": na_sales,
        "eu_sales": eu_sales,
        "jp_sales": jp_sales,
        "other_sales": other_sales,
        "global_sales": global_sales
    }
    # llama a la función agregar_juego() con la lista vacía y agrega el juego
    agregar_juego(juegos)
    return juegos  # devuelve la lista de juegos actualizada

juegos = agregar_juego_automaticamente("Super Mario Bros.", "Nintendo Entertainment System", 1985, "Plataformas", "Nintendo", 40.24, 29.08, 6.81, 9.23, 85.36)