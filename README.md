# Openclassrooms - Développez une application Web en utilisant Django

MVP (Minimal Viable Product) du projet LITReview.

Son objectif est de developper une application Web permettant à une communauté d'utilisateurs de consulter ou de solliciter une critique de livres à la demande.

L'application developpée via le framework Django doit notamment comprendre les fonctionnalités suivantes :

Inscription sur le site afin de disposer d'un compte utilisateur et d'un mot de passe\
Accès aux fonctionnalités du site uniquement aux utilisateurs connectés\
Abonnements à d'autres utilisateurs afin de visualiser leurs contenus (tickets et critiques)\
Création d'un ticket ("demande de critique") avec ajout possible d'image\
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

## fonctionnalités :

* Creation de compte utilisateur :\
Classe User héritant de la classe django.contrib.auth.models.User\
Néçessite uniquement le choix d'un nom d'utilisateur et d'un mot de passe

* Connexion à l'application:\
Via un compte utilisateur valide précedemment crée\
L'accès aux fonctionnalités suivantes néçessite la connexion sous peine d'etre redirigé vers la page de connexion.

* Flux (page d'acceuil) :\
Affichage, du plus récent au plus ancien, des tickets (demande de critique) et reviews (critiques) de tous les utilisateurs suivis (voir abonnements) ainsi que ceux de l'utilisateur connecté.\
Les reviews, néçessairement associées à un ticket, s'affichent de telle sorte que le ticket apparait dans la review.\
Cas particulier : Si une review a été créée en réponse à un ticket de l'utilisateur connecté, par un autre utilisateur qui n'est pas suivi (voir abonnements) par ce premier, alors la review apparait tout de même dans le flux de l'utilisateur connecté.

* Posts :\
Affichage, du plus récent au plus ancien, des tickets (demande de critique) et reviews (critiques) de l'utilisateur connecté.\
Si l'utilisateur connecté à crée un ticket et sa review associée, les deux elements sont listés séparemment.

* Abonnements:\
Ajout d'utilisateurs suivis via champ de texte : La correspondance parfaite avec le nom d'utilisateur doit etre saisie afin de voir l'utilisateur apparaitre dans la liste des utilisateurs suivis. Les posts de ce derniers apparaitraitrons dans la section flux.\
Un bouton à côté de l'utilisateur suivi dans la liste permet de se désabonner de celui-ci.\
Une liste des utilisateurs abonnés à l'utilisateur connecté apparait également sur cette page.\

* Gestion de l'utilisateur:\
Fonction d'ajout de photo de profil pour l'utilisateur connecté.\
Fonctionn de changement de mot passe pour l'utilisateur connecté.\

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
