from funciones import saludar
import unittest

class TestSaludar(unittest.TestCase):
    
    def test_1(self):
        resultado = saludar("Gabriel")
        self.assertEqual(resultado, "Hola, Marcelo")

    def test_2(self):
        resultado = saludar("Ghost")
        self.assertEqual(resultado, "Hola, Juan")

if __name__ == '__main__':
    unittest.main()
