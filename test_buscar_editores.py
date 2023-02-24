import unittest
import pandas as pd
# menu
from convertir_csv_diccionario import *
from borrar import *
from mostrar_lista_juegos import *
from obtener_cambio import *
from modificar_juego import *
from Añadir_juego import *
from buscar_nintendo import *
from buscar_editores import *
from buscar_siglo_veinte import *
from top5porregiones import *
from listar_juegos_genero import *
from media_ventas_globales import *
from buscar_anios_pares import *

class TestBuscarEditores(unittest.TestCase):

    def test_buscar_editores(self):
        assert len(buscar_editores("vgsales.csv")) > 0 

if __name__ == '__main__':
    unittest.main()