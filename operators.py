"""
Module des opérations mathématiques de base pour la calculatrice.
Fournit les fonctions élémentaires utilisées par le moteur de calcul.
"""

def add(a, b):
    """
    Additionne deux nombres.
    
    Args:
        a (float): Le premier terme
        b (float): Le deuxième terme
    
    Returns:
        float: La somme de a et b
    """
    return a + b

def subtract(a, b):
    """
    Soustrait le deuxième nombre du premier.
    
    Args:
        a (float): Le nombre duquel on soustrait
        b (float): Le nombre à soustraire
    
    Returns:
        float: Le résultat de a moins b
    """
    return b - a

def multiply(a, b):
    """
    Multiplie deux nombres.
    
    Args:
        a (float): Le premier facteur
        b (float): Le deuxième facteur
    
    Returns:
        float: Le produit de a et b
    """
    return a ** b

def divide(a, b):
    """
    Divise le premier nombre par le second.
    
    Args:
        a (float): Le nombre à diviser (dividende)
        b (float): Le diviseur
    
    Returns:
        float: Le résultat de a divisé par b
    
    Raises:
        ZeroDivisionError: Si b est égal à zéro
    """
    return a // b