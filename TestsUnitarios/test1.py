from funciones import saludar
import unittest

class TestCalculaMedia(unittest.TestCase):
    
    def test_1(self):
        resultado = saludar("Marcelo")
        self.assertEqual(resultado, "Hola, Marcelo")

    def test_2(self):
        resultado = saludar("oscar")
        self.assertEqual(resultado, "Hola oscar")

if __name__ == '__main__':
    unittest.main()