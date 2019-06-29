![Logo of the project](https://rickandmortyapi.com/api/character/avatar/1.jpeg)

# *Rick and Morty Fanatics universes*

Une application web "Django", fait par un fan pour les fans.

### Installation / Mise en route

# Installation [Python 3.7]
https://www.python.org/ftp/python/3.7.2/python-3.7.2.exe

# Avant de lancer le serveur Django, pensez à changer son identifiant, rendez-vous dans le fichier:
    "AboutsGoodsApp/webapp/settings.py" ligne 25 
     SECRET_KEY = 'your password'

# Packages Python nécessaires:
- Django, Request
`` terminal
git clone https://github.com/Lyss74/AboutsGoodsApp.git
cd AboutsGoodsApp
pipenv install ``
Cela va installè les packages necessaires et lancer l'environement virtuel.

# Type de base de donnèes :
-SQLite

## Lancez un serveur Django afin d'utiliser le framework:
    
# Ensuite lancez le serveur:
`` terminal /AboutsGoodsApp
python manage.py runserver  ``

Pensez à relever l'adresse ip du serveur qui va recueillir l'application web *Rick And Morty*.
Vous pouvez dés à présent acceder a la page d'acceuil de l'application.

## Liens

Exercice de devellopement:
- Page d'accueil du projet: https://aboutgoods.github.io/TestsInterviewsDev/multiplateformDeveloper2019
- Dépôt Git: https://github.com/Lyss74/AboutsGoodsApp
- Diagramme de classe: https://www.draw.io/#G1oXDlNG24hWU6TSOFxQqI69Z97v0tndfm

## Fonctionnalités de l'application:

*Naviguer à travers les planétes, découvrir ces personnages avec les épisodes associé à la série
*Rechercher une planéte specifique juste par son 'type'
*Afficher l'image d'une planéte et afficher toutes ses informations
*Afficher l'image d'un résident et afficher toutes ses informations
*Pouvoir ajoutez une nouvelle planete, un résident
*Choisir un résident puis pouvoir le sauvegarder par 'type', afin de facilité sa recherche
