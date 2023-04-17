# Openclassrooms - Développez une application Web en utilisant Django

MVP (Minimal Viable Product) du projet LITReview.

Son objectif est de developper une application Web permettant à une communauté d'utilisateurs de consulter ou de solliciter une critique de livres à la demande.

L'application developpée via le framework Django doit notamment comprendre les fonctionnalités suivantes :

Inscription sur le site afin de disposer d'un compte utilisateur et d'un mot de passe
Accès aux fonctionnalités du site uniquement aux utilisateurs connectés
Abonnements à d'autres utilisateurs afin de visualiser leurs contenus (tickets et critiques)
Création d'un ticket ("demande de critique") avec ajout possible d'image
Création d'une critique en réponse à un ticket ou avec création de ticket



## Installation

* Installer Python 3.11 :
 https://www.python.org/
  _Compatibilité avec d'autres versions probable mais non testée_

* Télécharger et extraire le repository suivant depuis github :\
https://github.com/Tod92/Projet9

* Se positionner dans le répértoire où le repository a été extrait :\
  `..\Projet9-main\`

* Créer l'environnement virtuel :\
_Installation de venv requise : pip install venv_
  `python -m venv env`

* Activer l'environnement virtuel :\
  `..\Projet9-main\env\Scripts\activate`

* Installer les packages Python néçessaire à l'execution du script :\
  `(env)..\Projet9-main\pip install -r requirements.txt`

* Installation terminée. Désactivation de l'environnement virtuel :\
  `deactivate`

## Execution du Serveur web en local :

* L'environnement virtuel doit etre activé :\
  `..\Projet9-main\env\Scripts\activate`

* Executer le script python :\
  `..\Projet9-main\litereview\python manage.py runserver`

* Depuis votre navigateur web :\
  `http://127.0.0.1:8000`

* Penser à désactiver l'environnement virtuel :\
  `deactivate`

## Tests de l'application :

La base de donnée a été peuplée avec les comptes et mots de passe de test suivants :

user : bart\
password : LisaEstNulle

user : lisa\
password : BartEstNul

user : marge\
password : ILoveOmer



## Historique

* 17/04/2023 : Finalisation et tests avec popoulation de la base de données
* 14/04/2023 : Avancement mise en forme CSS via bootstrap
* 10/04/2023 : Finalisation des fonctionnalités de création/modification/suppression
* 08/04/2023 : Integration abonnements à d'autres utilistaurs
* 06/04/2023 : Ajout gestion des photos (users + posts)
* 04/04/2023 : Creation tickets et reviews
* 30/03/2023 : Gestion Users (inscription + connexion)
* 28/03/2023 : Démarrage du projet

## Credits
Projet réalisé par Thomas DERUERE\
Assisté par Idriss BEN GELOUNE (Mentor Openclassrooms)
