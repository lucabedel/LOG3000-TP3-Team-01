# Module de tests du projet Calculatrice

Ce dossier contient les tests unitaires pour le projet de calculatrice.

## Structure

- `test_app.py` : Tests de la fonction `calculate` du fichier `app.py`.
- `test_operators.py` : Tests des fonctions arithmétiques du fichier `operators.py`.

## Comment exécuter les tests

Ouvrez un terminal à la racine du projet et lancez :

```
python -m unittest discover tests
```

Tous les tests seront exécutés automatiquement.

## Ce que couvrent les tests

- **Fonction `calculate`** :
  - Opérations de base (+, -, \*, /)
  - Gestion des erreurs (opérateurs multiples, opérandes non numériques, expression vide, opérateur mal placé)

- **Fonctions arithmétiques** :
  - Addition, soustraction, multiplication, division
  - Gestion des cas limites (zéro, négatif, division par zéro)
