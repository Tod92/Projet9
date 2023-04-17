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

## Vues

Le site presente un film en vedette, meilleur film par note imdb, première réponse de la requete api GET : "?sort_by=-imdb_score&imdb_score_min=9"

Le site presente ensuite 3 bandeaux de films, chacun contenant 4 pages de 7 films pouvant defiler via des boutons flèches gauches et droites.
Les bandeaux de films presentent les résultats aux requetes API suivantes :
* "Meilleurs scores ImDb" : "?sort_by=-imdb_score&imdb_score_min=9"
 (en evitant le premier résultat qui a été isolé pour la vignette meilleur film)
* "Meilleurs films d'animation": "?sort_by=-imdb_score&genre_contains=Animation"
* "Meilleurs films de Tarantino" : "?sort_by=imdb_score&writer_contains=tarantino&director_contains=tarantino"



## Historique

* 24/02/2023 : Finalisation v1 projet et documentation
* 23/02/2023 : Ajout fenetre modale
* 20/02/2023 : Ajout flèches et fonctions clic
* 18/02/2023 : Vues rows de films avec css
* 17/02/2023 : Lien Js <> Api fonctionnel
* 10/02/2023 : Démarrage du projet

## Credits
Projet réalisé par Thomas DERUERE\
Assisté par Idriss BEN GELOUNE (Mentor Openclassrooms)
