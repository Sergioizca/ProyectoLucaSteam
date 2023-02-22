from mostrar_lista_juegos import *
from convertir_csv_diccionario import *
from menu import *

lista = convertir_csv_diccionarios("vgsales.csv")

#Prueba unitaria01 mostrar_lista_juegos

def prueba_mostrar_lista_juegos(lista):
    check1 = len(lista)
    check2 = len(mostrar_lista_juegos(lista))
    ok = False
    if(check1==check2):
        ok=True
        print("Carga de datos correcta")
    else:
        ok=False
        print("Error en la carga de datos")
    return ok

#Prueba unitaria02 mostrar_lista_juegos
def prueba_mostrar_lista_juegos2(lista):
    check1 = len(lista)
    check2 = len(mostrar_lista_juegos(lista))
    assert check1==check2, "Carga de datos incorrecta"
    print("Carga de datos correcta")


def main():
    prueba_mostrar_lista_juegos(lista)
    prueba_mostrar_lista_juegos2(lista)


main()
