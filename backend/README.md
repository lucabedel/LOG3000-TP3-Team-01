# Module backend - Logique serveur et calculs

## Raison d'être du module
Ce module contient toute la logique serveur de l'application Flask et les fonctions mathématiques de la calculatrice.

## Fichiers

### `app.py`
- **Rôle** : Serveur Flask principal
- **Responsabilités** :
  - Initialise l'application Flask
  - Définit les routes (GET et POST)
  - Gère les requêtes utilisateur
  - Appelle les fonctions de calcul

### `operators.py`
- **Rôle** : Opérations mathématiques de base
- **Responsabilités** :
  - `add(a, b)` : Additionne deux nombres
  - `subtract(a, b)` : Soustrait b de a
  - `multiply(a, b)` : Multiplie a par b
  - `divide(a, b)` : Divise a par b (avec gestion d'erreur)

## Dépendances
- Flask (framework web)
- Python 3.8 ou supérieur