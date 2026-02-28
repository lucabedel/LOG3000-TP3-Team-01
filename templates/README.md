# Module Templates - Interface utilisateur

## Raison d'être du module
Ce module contient tous les fichiers HTML qui définissent la structure et l'interface visible de l'application. Il sépare la présentation (ce que l'utilisateur voit) de la logique métier (calculs côté serveur), conformément au patron de conception MVC (Modèle-Vue-Contrôleur) utilisé par Flask.

## Fichiers

### `index.html` (fichier unique)
- **Rôle** : Point d'entrée unique de l'interface utilisateur
- **Responsabilités** :
  - Affiche l'interface complète de la calculatrice (écran et boutons)
  - Capture les saisies de l'utilisateur (chiffres, opérateurs)
  - Envoie les expressions au serveur via formulaire POST
  - Contient le script JavaScript minimal pour la mise à jour de l'affichage
  - Affiche le résultat retourné par le serveur Flask

- **Ce que le fichier contient** :
  - Structure HTML5 sémantique
  - Formulaire avec méthode POST pour sécuriser l'envoi des données
  - Champ d'affichage en lecture seule (empêche les modifications directes)
  - Grille de boutons organisée en 4 colonnes (chiffres et opérateurs)
  - Script JavaScript pour :
    - `appendToDisplay(value)` : Ajoute un caractère à l'expression
    - `clearDisplay()` : Réinitialise l'affichage

## Dépendances et hypothèses

### Dépendances techniques
- **Flask** : Le fichier utilise la syntaxe Jinja2 (`{{ result }}`) pour afficher les données dynamiques du serveur
- **CSS** : Dépend du fichier `style.css` dans le dossier `static` pour la présentation visuelle
- **JavaScript** : Le script intégré est autonome (pas de bibliothèque externe)

### Hypothèses de fonctionnement
- Le serveur Flask renvoie une variable `result` contenant le résultat du calcul ou l'expression en cours
- Le formulaire POST est traité par une route Flask qui effectue les calculs
- Les classes CSS (`.calculator`, `.btn`, `.operator`) existent dans le fichier `style.css`
- L'élément avec l'id `display` est présent pour que JavaScript puisse le manipuler

### Hypothèses d'utilisation
- L'utilisateur interagit uniquement avec les boutons (pas de saisie directe au clavier)
- Le bouton "=" déclenche un envoi au serveur pour sécuriser les calculs
- Le bouton "C" efface tout d'un coup pour une correction rapide


## Notes pour les nouveaux développeurs
- L'interface est volontairement simple : un seul fichier HTML pour faciliter la maintenance
- Le JavaScript est minimal et intégré dans le HTML car l'application est petite
- Si l'application grandit, il faudrait déplacer le JavaScript dans un fichier séparé dans `static/`
- Les bogues visuels (boutons sans symbole) sont identifiés dans les commentaires du fichier