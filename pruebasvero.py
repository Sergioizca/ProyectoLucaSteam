from borrar import *
from convertir_csv_diccionario import *
from menu import *

# Prueba unitaria para borrar.py
# Comprueba que la enrtada que se ha borrado ya no figura en la lista
lista = convertir_csv_diccionarios("vgsales.csv")

def prueba_borrar_de_dic():
    # traer funcion borrar_de_dic
    # chequear longitud de la lista antes de borrar una entrada
    # confirmar que se ha borrado porque la lista ya no tiene la misma longitud
    sin_borrar = len(lista)
    if juego_encontrado = True
    borrar_de_dic() #ejecutamos la función para eliminar una entrada
    borrado = len(lista) 
    assert sin_borrar != borrado, "Se ha borrado una entrada" # asegura que la lista ha cambiado
    # porque se ha eliminado una entrada
                                                              
                                                            
# Comprueba que la lista vacia no esta vacia

 def is_list_empty(lista):
    assert len(lista) != 0:
         return True
    return False                                                      

