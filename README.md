# Projet 2: Code Caesar
Le code Caesar est le plus simple algorithme de cryptage possible, il est basé sur un décalage des lettres par une valeur donnée. Exemple avec un décalage de 3
clair : ABCDEFGHIJKLMNOPQRSTUVWXYZ
chiffré : DEFGHIJKLMNOPQRSTUVWXYZABC

* Objectif : 
Implémenter un programme Python qui chiffre et déchiffre du texte en utilisant le chiffrement de César.

* Fonctionnalités :
Chiffrement d'un texte avec une clé donnée (décalage des lettres de l'alphabet).
Déchiffrement d'un texte chiffré avec la même clé.
Gestion des lettres majuscules et minuscules.
Gestion des caractères non alphabétiques (ponctuation, espaces, etc.).
Tests unitaires avec Pytest pour vérifier le bon fonctionnement du chiffrement et du déchiffrement.

* Amélioration:
prendre en compte les majuscules, les espaces et la ponctuation.

# Installation environnement virtuel

**Virtual environnement**
```powershell
python -m venv .venv
```
> .venv is the name of the virtual environnement 

**Connect to the venv** 

- mac/linux
`source .venv/bin/activate.fish`
- windows
`.venv/Scripts/activate` or `.venv/Scripts/activate.ps1` 

**create requirements.txt from pip**
`pip freeze > requirements.txt`

in a new environnement install the librairies
**install librairies**.
`pip install -r requirements.txt`

**quit venv**
`deactivate` 
