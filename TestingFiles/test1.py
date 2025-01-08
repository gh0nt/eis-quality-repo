from funciones import saludar
import unittest

class TestSaludar(unittest.TestCase):
    
    def test_1(self):
        resultado = saludar("Marcelo")
        self.assertEqual(resultado, "Hola, Marcelo")

    def test_2(self):
        resultado = saludar("Juan")
        self.assertEqual(resultado, "Hola, Juan")

if __name__ == '__main__':
    unittest.main()
