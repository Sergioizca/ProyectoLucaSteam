import unittest

def esta_juego_presente(juegos, nombre)
    nombre_a_borrar = juegos[0]["nombre"] # pillamos el primer juego
    borrar_juego(juegos, nombre_a_borrar)
    assert(not esta_juego_presente(juegos, nombre_a_borrar)