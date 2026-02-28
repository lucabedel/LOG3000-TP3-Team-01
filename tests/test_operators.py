import unittest
from operators import add, subtract, multiply, divide

class TestOperators(unittest.TestCase):
    """Tests unitaires pour les fonctions du module operators."""

    def test_add(self):
        """Test de la fonction add."""
        self.assertEqual(add(2, 1), 3)
        self.assertEqual(add(-2, 1), -1)
        self.assertEqual(add(2, 0), 2)
        self.assertEqual(add(0.5, 2), 2.5)

    def test_subtract(self):
        """Test de la fonction subtract."""
        self.assertEqual(subtract(2, 1), 1)
        self.assertEqual(subtract(-2, 1), -3)
        self.assertEqual(subtract(2, 0), 2)
        self.assertEqual(subtract(0.5, 2), -1.5)

    def test_multiply(self):
        """Test de la fonction multiply."""
        self.assertEqual(multiply(2, 2), 4)  
        self.assertEqual(multiply(2, -2), -4) 
        self.assertEqual(multiply(2, 0), 0)
        self.assertEqual(multiply(0.5, 2), 1)

    def test_divide(self):
        """Test de la fonction divide."""
        self.assertEqual(divide(2, 2), 1)    
        self.assertEqual(divide(4, 2), 2)
        self.assertEqual(divide(2, -2), -1)
        self.assertEqual(divide(1, 3), 0.3333333333333333)
        self.assertEqual(divide(0.5, 2), 0.25)
        with self.assertRaises(ZeroDivisionError):
            divide(5, 0)  # Test de division par zéro

if __name__ == "__main__":
    unittest.main()