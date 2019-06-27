# Application web "Rick ANd Morty"

#### Application web *Rick And Morty*

## Type de base de donnèes:
-MySQL 8.0

## Environnement virtuel:
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

## Packages nécessaire
    - Django
    - records 
    - requests 
    - mysql-connector-python                

#### Installation:
Rendez-vous dans le répertoire du projet avec l'invité de commande

## Exemple de positionnement: 
    "C:Users\Admin\Desktop\AboutsGoodsApp"

## Installez pipenv: 
    pip install pipenv

une fois fait, après quelques secondes:

## Tapez: 
    pipenv install 
    -[Cette commande installera tous les packages, en suivant le fichier Pipfile]

### Lancez un serveur SQL afin dutiliser la base de donnèes.

## La connexion à la base se fera sous ces identifiants: 
    DATABASE = 'PurBeurre'
    USER = 'OPFF' 
    PASSWORD = 'OCP5' 

### Lancez un serveur Django afin dutiliser le framework.

Rendez-vous dans le répertoire du projet avec l'invité de commande

## Exemple de positionnement: 
    "C:Users\Admin\Desktop\AboutsGoodsApp"

## Puis tapez dans l'invité de commande
    -py manage.py runserver
# Pensez à relever l'ip du serveur qui va receuillir l'application web *Rick And Morty*.

### Lancement

## Tapez: 
    pipenv run python main.py 

## Pour directement alimenter la base de donnèes:
    pipenv run python main.py --database 


# Fonctionnalités de l'application:

# *The Rick and Morty universe*

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
