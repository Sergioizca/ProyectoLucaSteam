import unittest
import pandas as pd
from buscar_nintendo import *
from convertir_csv_diccionario import *


#comprueba que el archivo es válido para cargarlo.
class TestBuscarNintendo(unittest.TestCase):
    
    def test_buscar_nintendo(self):
        # Llamar a la función con un archivo válido
        archivo = "vgsales.csv"
        buscar_nintendo(archivo)

#comparar si la primera fila coincide con la primera fila cargada

import unittest
import pandas as pd


class TestCSV(unittest.TestCase):

    def test_primera_y_ultima_fila(self):
        # Cargar el archivo CSV utilizando pandas
        df = pd.read_csv('vgsales.csv')
        # Obtener la primera y última fila del archivo cargado
        primera_fila_cargada = df.iloc[0].tolist()
        ultima_fila_cargada = df.iloc[-1].tolist()
        # Leer el archivo CSV como un archivo de texto
        f=convertir_csv_diccionarios('vgsales.csv')
        # Obtener la primera y última línea del archivo
        lineas_archivo = f.readlines()
        primera_linea_archivo = lineas_archivo[0].strip()
        ultima_linea_archivo = lineas_archivo[-1].strip()
        # Convertir la primera y última línea del archivo en listas de valores
        primera_fila_archivo = primera_linea_archivo.split(',')
        ultima_fila_archivo = ultima_linea_archivo.split(',')
        # Comparar las dos listas
        self.assertListEqual(primera_fila_cargada, primera_fila_archivo)
        self.assertListEqual(ultima_fila_cargada, ultima_fila_archivo)


if __name__ == '__main__':
    unittest.main()


