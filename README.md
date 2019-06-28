**Rick and Morty Fanatics universes**


#### Application web *Rick And Morty*

## Type de base de donnèes :
-MySQL 8.0

## Environnent virtuel:
-PipEnv

## Exercice de développement multiplateforme:
https://aboutgoods.github.io/TestsInterviewsDev/multiplateformDeveloper2019

## Api *Rick And Morty*:
http://rickandmortyapi.com 

## Diagramme de classe: 
https://www.draw.io/#G1oXDlNG24hWU6TSOFxQqI69Z97v0tndfm

## Langue d'écriture, variables, commentaires, fonctions: 
-Anglais

## Installation [Python 3.7]
https://www.python.org/ftp/python/3.7.2/python-3.7.2.exe

##### Téléchargement:

## Télécharger le fichier: 
https://github.com/Lyss74/AboutsGoodsApp/archive/master.zip

## Ou cloner le repository:
https://github.com/Lyss74/AboutsGoodsApp.git

## Packages nécessaires:
    - Django
               
### Lancez un serveur Django afin d'utiliser le framework.
# Avant de lancer le serveur pensez à changer son identifiant, rendez-vous dans le fichier:
    "webapp/settings.py" ligne 26 
     SECRET_KEY = 'your password'
     
# Ensuite lancez le serveur:
Rendez-vous dans le répertoire du projet avec l'invité de commande

## Exemple de positionnement: 
    "C:Users\Admin\Desktop\AboutsGoodsApp"

## Puis tapez dans l'invité de commande
    -py manage.py runserver
# Pensez à relever l'adresse ip du serveur qui va recueillir l'application web *Rick And Morty*.

# Fonctionnalités de l'application:

# *Rick and Morty Fanatics universes*

### We need to create a front interface for the Rick & Morty universe, to allow fans to navigate through elements and character of the TV Show.
    [FR]-Nous devons créer une interface frontale pour l'univers Rick & Morty, afin de permettre aux fans de naviguer à travers les éléments et le personnage de l'émission.

### Nous avons particulièrement besoin de :

## Browse all the locations of all differents universes in a list:
    [FR]-Parcourir tous les emplacements de tous les différents univers dans une liste 
        -universe = ['locations'] / total page = 4

## Search for a specific location by it’s type:
    [FR]-Rechercher un lieu spécifique par son type 
        = ['locations'] -> ['types']

## When clicking on a location, showing details and image of the planet and a list of all the residents:
    [FR]-En cliquant sur un lieu, montrant les détails et l'image de la planète et une liste de tous les résidents
        = ['locations'] -> ['residents']

## We want to show details (including picture) of a resident by clicking on it:
    [FR]-Nous voulons montrer les détails (y compris la photo) d'un résident en cliquant dessus
        = ['locations'] -> ['residents'] -> ['url'] {img}

## We also want to create a new location or resident locally:
    [FR]-Nous voulons également créer un nouvel emplacement ou un résident local

## We want a favorite system to save our favorite resident and location with a way to filter them by their type:
    [FR]-Nous voulons un système favori pour enregistrer notre résident préféré et son emplacement avec un moyen de les filtrer par type.
        favoris = [ ['resident'] -> ['location'] -> ['type'] ]