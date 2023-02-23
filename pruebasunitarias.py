import unittest
import pandas as pd
from buscar_nintendo import *


#comprueba que el archivo es válido para cargarlo.
class TestBuscarNintendo(unittest.TestCase):
    
    def test_buscar_nintendo(self):
        # Llamar a la función con un archivo válido
        archivo = "vgsales.csv"
        buscar_nintendo(archivo)


def load_csv_to_dict_list(csv_file):
    """Carga un archivo CSV en una lista de diccionarios"""
    df = pd.read_csv(csv_file)
    dict_list = df.to_dict('records')
    return dict_list

#dado un archivo csv con pandas compruebe que han cargado correctamente en una lista de diccionarios.
class TestCarga(unittest.TestCase):

    def test_load_csv_to_dict_list(self):
        dict_list = load_csv_to_dict_list('vgsales.csv')
        self.assertEqual(len(dict_list), 16598)
        self.assertEqual(dict_list[0]['Rank'], 1)
        self.assertEqual(dict_list[0]['Name'], 'Wii Sports')
        self.assertEqual(dict_list[0]['Platform'], 'Wii')
        self.assertEqual(dict_list[0]['Year'], 2006)
        self.assertEqual(dict_list[0]['Genre'], 'Sports')
        self.assertEqual(dict_list[0]['Publisher'], 'Nintendo')
        self.assertEqual(dict_list[0]['NA_Sales'], 41.49)
        self.assertEqual(dict_list[0]['EU_Sales'], 29.02)
        self.assertEqual(dict_list[0]['JP_Sales'], 3.77)
        self.assertEqual(dict_list[0]['Other_Sales'], 8.46)
        self.assertEqual(dict_list[0]['Global_Sales'], 82.74)
        

 
if __name__ == '__main__':
    unittest.main()