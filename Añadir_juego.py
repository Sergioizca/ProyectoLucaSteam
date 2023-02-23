import csv
from convertir_csv_diccionario import *


def obtener_valor(valor):
    if not valor:
        return 'Desconocido'
    else:
        return valor


def obtener_float(dato):
    while True:
        if not dato:
            return 'Desconocido'
        else:
            try:
                dato_float = float(dato)
                return dato_float
            except ValueError:
                print("El valor debe ser un número.")
        dato = input("Ingrese el valor nuevamente: ")

juegos=convertir_csv_diccionarios("vgsales.csv")

def agregar_juego(juegos):
    encurso = True

    print('Si el campo se deja vacio, se pondra como desconocido ')

    while encurso:
        
        nombre = input("Indica el nombre del juego: ")
        obtener_valor(nombre)
        plataforma = input("Indica la plataforma del juego: ")
        obtener_valor(plataforma)

        año = None  # Inicializar variable aquí

        while año is None:
            try:
                año = int(input("Indica el año de lanzamiento del juego: "))
                assert 1950 <= año <= 2024, "El año debe estar entre 1950 y 2024."
            except ValueError:
                print("El año debe ser un número entero.")
            except AssertionError as error:
                print(error)
                año = None

        genero = input("Indica el género del juego: ")
        obtener_valor(genero)
        empresa = input("Indica la empresa del juego: ")
        obtener_valor(empresa)
        na_sales = input('Indica valor de ventas de Norte America: ')
        obtener_float(na_sales)
        eu_sales = input('Indica valor de ventas de Europa: ')
        obtener_float(eu_sales)
        jp_sales = input('Indica valor de ventas de Japon: ')
        obtener_float(jp_sales)
        other_sales = input('Indica valor de ventas del resto del mundo; ')
        obtener_float(other_sales)
        global_sales = input('Indica valor de ventas a nivel global: ')
        obtener_float(global_sales)

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

        a = True
        while a:
            confirmar = input(
                f"¿Quieres agregar este juego? (1 = si/2 = no): {juego}")

            if confirmar == '1':
                juegos.append(juego)
                print("El juego se ha agregado correctamente.")
                a = False
            elif confirmar == '2':
                print("El juego no se ha agregado.")
                a = False
            else:
                print("Tiene que ser 1: Si o 2: No")
        b = True
        
        while b:
            confirmar = input(
                "¿Desea agregar otro juego? (1 = si/2 = no): ")

            if confirmar == '1':
                encurso = True
                b = False

            elif confirmar == '2':
                encurso = False
                b = False
            else:
                confirmar = input(
                        "¿Desea agregar otro juego? (1 = si/2 = no): ")
                b = True
                
