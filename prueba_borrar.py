import unittest

def prueba_borrar():
    
class PruebaTestFixture(unittest.TestCase):

    def setUp(self):
        print("Preparando el contexto")
        self.juegos = [1, 2, 3, 4, 5]

    def test(self):
        print("Realizando una prueba")
        r = [doblar(n) for n in self.juegos]
        self.assertEqual(r, [2, 4, 6, 8, 10])

    def tearDown(self):
        print("Destruyendo el contexto")
        del(self.juegos)


if __name__ == '__main__':
    unittest.main() 