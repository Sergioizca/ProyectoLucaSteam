import unittest
import pandas as pd
from unittest.mock import patch
from listar_juegos_genero import *
from media_ventas_globales import *

#Si buscamos por un género que no existe, devuelve una lista vacía
#Compruebo que la lista tiene longitud 0
class PruebaGenero(unittest.TestCase):
    
    def test_genero_juegos(self):
        archivo = "vgsales.csv"
        juegos_por_genero = listar_juegos_genero("f{archivo} género que no existe")
        self.assertEqual(len(juegos_por_genero) == 0)
#No imprime nada por lo que el test funciona bien

class PruebaTopVentas(unittest.TestCase):
    
    def media_menor_que(self):
        df = pd.read_csv("vgsales.csv")
        media = df['Global_Sales'].mean()
        top_ventas = df['Global_Sales'].max()
        self.assertTrue(top_ventas > media)
        ## aqui aseguramos que el numero top ventas global es mayor que la media de ventas globales
        
