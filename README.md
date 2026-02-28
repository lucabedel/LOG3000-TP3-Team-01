# LOG3000-TP3-Team-01

## Numéro d'équipe
**Équipe 01**

---

## Objectif du projet

Application web de calculatrice simple développée avec **Flask (Python)**.

Elle permet d'effectuer des opérations arithmétiques de base :

- Addition
- Soustraction
- Multiplication
- Division

Ce projet met en pratique les bonnes pratiques de génie logiciel :

- Gestion de versions collaborative
- Documentation complète
- Tests automatisés

---

## Prérequis

Avant de commencer, assurez-vous d’avoir :

- Git
- Python 3.8 ou supérieur
- pip (gestionnaire de paquets Python)
- Un navigateur web (Chrome, Firefox, Safari ou Edge)

---

## Installation

### 1. Cloner le dépôt

```bash
git clone https://github.com/lucabedel/LOG3000-TP3-Team-01.git
cd LOG3000-TP3-Team-01
```

### 2. Créer et activer un environnement virtuel

#### Sous Windows

```bash
python -m venv venv
venv\Scripts\activate
```

#### Sous macOS / Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Installer les dépendances

```bash
pip install flask
```

### 4. Lancer l'application

```bash
python app.py
```

### 5. Accéder à l’application

Ouvrez votre navigateur et rendez-vous à l’adresse :

```
http://127.0.0.1:5000
```

---

## Instructions d'utilisation

### Effectuer un calcul

1. Cliquez sur les boutons numériques pour entrer le premier nombre  
2. Cliquez sur un opérateur (+, -, *, /)  
3. Entrez le deuxième nombre  
4. Cliquez sur `=` pour afficher le résultat  

### Effacer l’affichage

Cliquez sur le bouton `C` pour tout effacer.

---

## Exemple concret

Pour calculer **15 + 3** :

1. Cliquez sur `1` puis `5`  
2. Cliquez sur `+`  
3. Cliquez sur `3`  
4. Cliquez sur `=`  

Le résultat **18** s’affiche.

---

## Structure du projet

```
LOG3000-TP3-Team-01/
│
├── app.py                 # Serveur Flask et logique de calcul
├── operators.py           # Fonctions mathématiques de base
│
├── templates/
│   └── index.html         # Interface utilisateur
│
├── static/
│   └── style.css          # Styles CSS
│
└── README.md              # Documentation principale
```

---

## Tests

### Exécuter les tests

```bash
# À venir - Les tests seront ajoutés dans le dossier tests/
```

### Couverture prévue

- Tests unitaires des fonctions dans `operators.py`
- Tests d’intégration des routes Flask
- Cas particuliers :
  - Division par zéro
  - Nombres négatifs
  - Entrées invalides

---

## Flux de contribution

### Signaler un problème

1. Ouvrez une **Issue** dans l’onglet *Issues* sur GitHub  
2. Décrivez clairement le problème  
3. Indiquez les étapes pour le reproduire  
4. Ajoutez des captures d’écran si nécessaire  

### Proposer une correction

#### 1. Créer une branche dédiée

```bash
git checkout -b correction-description-du-bogue
```

#### 2. Effectuer les modifications et tester

#### 3. Committer les modifications

```bash
git add .
git commit -m "Corrige [description précise du problème]"
```

#### 4. Pousser la branche

```bash
git push origin correction-description-du-bogue
```

#### 5. Ouvrir une Pull Request

- Créez une PR vers la branche `main`
- Liez la PR à l’issue correspondante (ex: `Fixes #12`)

---

## Règles de contribution

- Une branche = une seule fonctionnalité ou correction
- Messages de commit explicites
- Tester avant de soumettre une PR
- Attendre la revue de code avant de fusionner

---

## Auteurs

Équipe 01 — LOG3000

---

## Licence

Projet réalisé dans le cadre du cours **LOG3000 — Génie logiciel**.