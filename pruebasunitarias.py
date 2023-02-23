import unittest
import pandas as pd
from buscar_nintendo import *


#comprueba que el archivo es válido para cargarlo.
class TestBuscarNintendo(unittest.TestCase):
    
    def test_buscar_nintendo(self):
        # Llamar a la función con un archivo válido
        archivo = "vgsales.csv"
        buscar_nintendo(archivo)

#dado un archivo csv con pandas compruebe que han cargado correctamente en una lista de diccionarios.
def carga_csv_lista(archivo):
    # Carga un archivo CSV en una lista de diccionarios
    datos = pd.read_csv(archivo)
    lista = datos.to_dict('records')
    return lista

class TestCarga(unittest.TestCase):

    def test_carga_csv_lista(self):
        lista = carga_csv_lista('vgsales.csv')
        self.assertEqual(len(lista), 16598)
        self.assertEqual(lista[0]['Rank'], 1)
        self.assertEqual(lista[0]['Name'], 'Wii Sports')
        self.assertEqual(lista[0]['Platform'], 'Wii')
        self.assertEqual(lista[0]['Year'], 2006)
        self.assertEqual(lista[0]['Genre'], 'Sports')
        self.assertEqual(lista[0]['Publisher'], 'Nintendo')
        self.assertEqual(lista[0]['NA_Sales'], 41.49)
        self.assertEqual(lista[0]['EU_Sales'], 29.02)
        self.assertEqual(lista[0]['JP_Sales'], 3.77)
        self.assertEqual(lista[0]['Other_Sales'], 8.46)
        self.assertEqual(lista[0]['Global_Sales'], 82.74)
        

 
if __name__ == '__main__':
    unittest.main()