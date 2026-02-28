import unittest
from backend.app import calculate

class TestCalculate(unittest.TestCase):
    """Tests unitaires pour la fonction calculate du module app."""

    def test_addition(self):
        """Test de l'addition."""
        self.assertEqual(calculate("2+1"), 3)
        self.assertEqual(calculate("0.5+2"), 2.5)
        self.assertEqual(calculate("-2+1"), -1)
        self.assertEqual(calculate("1+-2"), -1)
        self.assertEqual(calculate("2+0"), 2)

    def test_subtraction(self):
        """Test de la soustraction."""
        self.assertEqual(calculate("5-2"), 3)
        self.assertEqual(calculate("0-2"), -2)
        self.assertEqual(calculate("2-0"), 2)
        self.assertEqual(calculate("-2-1"), -3)
        self.assertEqual(calculate("0.5-2"), -1.5)

    def test_multiplication(self):
        """Test de la multiplication."""
        self.assertEqual(calculate("2*3"), 6) 
        self.assertEqual(calculate("0.5*2"), 1)
        self.assertEqual(calculate("2*0"), 0)
        self.assertEqual(calculate("-2*1"), -2)
        self.assertEqual(calculate("1*-2"), -2)
        
    def test_division(self):
        """Test de la division."""
        self.assertEqual(calculate("5/2"), 2.5)  
        self.assertEqual(calculate("1/3"), 0.3333333333333333)
        self.assertEqual(calculate("0.5/2"), 0.25)
        self.assertEqual(calculate("-2/2"), -1)
        self.assertEqual(calculate("2/-2"), -1)
        with self.assertRaises(ZeroDivisionError):
            calculate("5/0")
            
    def test_invalid_operator(self):
        """Test avec plusieurs opérateurs."""
        with self.assertRaises(ValueError):
            calculate("2++3")

    def test_operator_at_start(self):
        """Test avec opérateur au début."""
        with self.assertRaises(ValueError):
            calculate("+23")

    def test_operator_at_end(self):
        """Test avec opérateur à la fin."""
        with self.assertRaises(ValueError):
            calculate("23+")
    
    def test_operator_at_start_and_end(self):
        """Test avec opérateur au début et à la fin."""
        with self.assertRaises(ValueError):
            calculate("+23+")

    def test_empty_expression(self):
        """Test avec une expression vide."""
        with self.assertRaises(ValueError):
            calculate("")

if __name__ == "__main__":
    unittest.main()