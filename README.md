
# Calculatrice Web – Équipe 1

## Objectif

Ce projet vise à documenter et à corriger une application web de calculatrice simple utilisant **Python** et **Flask**.

L’application permet d’effectuer des opérations arithmétiques de base (addition, soustraction, multiplication, division) via une interface utilisateur intuitive.

La base de code initiale a été restructurée, documentée et corrigée afin d’appliquer les bonnes pratiques de génie logiciel.

---

## Prérequis

* Un compte GitHub
* VS Code
* Git installé localement
* Python (version 3.7 ou supérieure)
* pip (gestionnaire de paquets Python)

---

## Instructions d’installation

### 1. Cloner le dépôt

```bash
git clone https://github.com/lucabedel/LOG3000-TP3-Team-01.git
cd LOG3000-TP3-Team-01
```

### 2. Installer les dépendances

```bash
python -m pip install flask
```

### 3. Lancer l’application

```bash
python backend/app.py
```

### 4. Accéder à l’application

Ouvrez votre navigateur et rendez-vous à l’adresse suivante :

```
http://localhost:5000
```

---

## Instructions d’utilisation

### Effectuer un calcul

1. Cliquez sur les boutons numériques pour entrer le premier nombre
2. Cliquez sur un opérateur (`+`, `-`, `*`, `/`)
3. Entrez le deuxième nombre
4. Cliquez sur le bouton **=** pour afficher le résultat

### Effacer l'affichage

* Cliquez sur le bouton **C** pour tout effacer

### Exemples

| Expression | Résultat |
| ---------- | -------- |
| 15 + 3     | 18       |
| 10 - 4     | 6        |
| 6 * 7      | 42       |
| 15 / 3     | 5        |
| -2 + 5     | 3        |

---

## Tests

Pour exécuter les tests unitaires :

```bash
python -m unittest discover -s tests -v
```

---

## Flux de contribution

### Signaler un problème

1. Ouvrez une **Issue** dans l’onglet **Issues** sur GitHub
2. Décrivez clairement le problème et les étapes pour le reproduire

### Proposer une modification

#### 1. Créer une branche dédiée

```bash
git checkout -b type/nom-de-la-branche
```

Exemples :

* `fix/soustraction`
* `docs/readme`
* `feat/fonctionnalite`

#### 2. Effectuer les modifications et tester

#### 3. Committer les changements

```bash
git add .
git commit -m "type: description des changements"
```

#### 4. Pousser la branche

```bash
git push -u origin nom-de-la-branche
```

#### 5. Ouvrir une Pull Request

Créer une **Pull Request (PR)** vers la branche `main`.

---

## Règles de contribution

* Une branche = une seule fonctionnalité ou correction
* Tester avant de soumettre une PR
* Ne jamais pousser directement sur `main`

---

## Structure du projet

```
backend/              # Logique serveur et calculs
│
├── app.py            # Serveur Flask
├── operators.py      # Fonctions arithmétiques
├── README.md
static/               # Fichiers CSS
├── style.css         # Styles de l'application
├── README.md
templates/            # Fichiers HTML
├── index.html        # Interface utilisateur
├── README.md
tests/                # Tests unitaires
├── test_app.py       # Tests de la fonction calculate
├── test_operators.py # Tests des opérations
├── README.md
README.md             # Documentation principale
```
Luca Badel 2297114
Christopher Azrak 2251271
---
