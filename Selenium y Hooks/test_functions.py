import unittest
from functions import (
    total, addit, mult, divide, length, reverse, remove_letter,
    max, even_numbers, odd_numbers, is_even
)

class TestFunciones(unittest.TestCase):

    def test_total(self):
        self.assertEqual(total([1, 2, 3, 4]), 10)
        self.assertEqual(total([]), 0)
        self.assertEqual(total([-1, -2, -3, -4]), -10)

    def test_addit(self):
        self.assertEqual(addit(3), 8)
        self.assertEqual(addit(0), 5)
        self.assertEqual(addit(-5), 0)

    def test_mult(self):
        self.assertEqual(mult(3), 24)
        self.assertEqual(mult(0), 0)
        self.assertEqual(mult(-2), -14)

    def test_divide(self):
        self.assertEqual(divide(8, 2), 4)
        with self.assertRaises(ZeroDivisionError):
            divide(8, 0)

    def test_length(self):
        self.assertEqual(length([1, 2, 3, 4]), "Less than 5")
        self.assertEqual(length("Hola"), "Less than 5")
        self.assertEqual(length("Prueba"), "Longer than 5")

    def test_reverse(self):
        self.assertEqual(reverse("casa"), "asac")
        self.assertEqual(reverse("12345"), "54321")
        self.assertEqual(reverse(""), "")

    def test_remove_letter(self):
        self.assertEqual(remove_letter("a", "Hola esto es una prueba"), "Hol esto es un prueb")
        self.assertEqual(remove_letter("x", "Hola"), "Hola")

    def test_max(self):
        self.assertEqual(max([1, 8, 3, 0, 12]), 12)
        self.assertEqual(max([-1, -8, -3, -12]), -1)

    def test_even_numbers(self):
        self.assertEqual(even_numbers([1, 8, 3, 6, 12, 5]), [8, 6, 12])
        self.assertEqual(even_numbers([1, 3, 5]), [])

    def test_odd_numbers(self):
        self.assertEqual(odd_numbers([1, 8, 3, 6, 12, 5]), [1, 3, 5])
        self.assertEqual(odd_numbers([2, 4, 6]), [])

    def test_is_even(self):
        self.assertTrue(is_even(2))
        self.assertFalse(is_even(3))
        self.assertTrue(is_even(0))

if __name__ == "__main__":
    unittest.main()
