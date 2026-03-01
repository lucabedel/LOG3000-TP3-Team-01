"""
Fichier principal de l'application Flask pour la calculatrice web.
Ce module initialise le serveur, définit les routes et gère la logique de calcul.
"""

from flask import Flask, request, render_template
from operators import add, subtract, multiply, divide

# Initialisation de l'application Flask
app = Flask(__name__)

# Dictionnaire faisant le lien entre les symboles d'opérateurs et leurs fonctions correspondantes
# Centraliser ici facilite l'ajout de nouveaux opérateurs si nécessaire
OPS = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide,
}

def calculate(expr: str):
    """
    Évalue une expression mathématique simple (un seul opérateur) et retourne le résultat.
    Gère les nombres négatifs (ex: "-2+3" est interprété comme (-2) + 3).
    
    Args:
        expr (str): L'expression mathématique sous forme de chaîne (ex: "3+5" ou "-2+3")
    
    Returns:
        float: Le résultat du calcul
    
    Raises:
        ValueError: Si l'expression est vide, mal formatée, ou contient des opérandes non numériques
    """
    # Vérification que l'expression n'est pas vide (évite les erreurs silencieuses)
    if not expr or not isinstance(expr, str):
        raise ValueError("empty expression")

    # Supprime les espaces pour que par exemple "3+5" et "3 + 5" soient traités de la même façon
    s = expr.replace(" ", "")

    op_pos = -1
    op_char = None

    # Parcourt chaque caractère pour trouver l'opérateur principal
    for i, ch in enumerate(s):
        if ch in OPS:
            # Gestion du signe moins pour les nombres négatifs
            # Si '-' est au début ou après un autre opérateur, c'est un signe négatif, pas un opérateur
            if ch == '-' and (i == 0 or s[i-1] in OPS):
                continue
            
            # Si on a déjà trouvé un opérateur, l'expression est invalide
            # (la calculatrice ne gère que les opérations simples pour l'instant)
            if op_pos != -1:
                raise ValueError("only one operator is allowed")
            op_pos = i
            op_char = ch

    # Vérifie que l'opérateur est valide et bien placé (pas au début ou à la fin)
    if op_pos <= 0 or op_pos >= len(s) - 1:
        raise ValueError("invalid expression format")

    # Sépare l'expression en opérande gauche et droite
    left = s[:op_pos]
    right = s[op_pos+1:]

    # Convertit les chaînes en nombres
    try:
        a = float(left)
        b = float(right)
    except ValueError:
        # L'utilisateur a peut-être entré des lettres ou des symboles non valides
        raise ValueError("operands must be numbers")

    # Appelle la fonction correspondant à l'opérateur trouvé
    return OPS[op_char](a, b)

@app.route('/', methods=['GET', 'POST'])
def index():
    """
    Route principale de l'application.
    Gère à la fois l'affichage de la page (GET) et le traitement du formulaire (POST).
    
    Returns:
        str: Page HTML rendue avec le résultat du calcul (ou vide au premier chargement)
    """
    result = ""
    
    if request.method == 'POST':
        # Récupère l'expression saisie par l'utilisateur dans le champ 'display'
        expression = request.form.get('display', '')
        
        try:
            # Tente de calculer le résultat
            result = calculate(expression)
        except Exception as e:
            # Affiche une erreur explicite à l'utilisateur plutôt que d'interrompre l'application
            result = f"Error: {e}"
    
    # Renvoie la page HTML avec le résultat (vide si pas de calcul)
    return render_template('index.html', result=result)

if __name__ == '__main__':
    # Lance le serveur en mode debug uniquement si le fichier est exécuté directement
    # Le mode debug permet de voir les erreurs détaillées pendant le développement
    app.run(debug=True)