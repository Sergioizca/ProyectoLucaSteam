from borrar import *
from convertir_csv_diccionario import *

# Prueba unitaria para borrar.py
# Comprueba que ocurre si el csv no se ha leído correctamente
lista = convertir_csv_diccionarios("vgsales.csv")
def prueba_borrar_de_dic(lista):
    print(len(lista))
    
prueba_borrar_de_dic()

    
