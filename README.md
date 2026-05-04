# Site web d'Orange County Lettings

## Développement local

### Prérequis

- Compte GitHub avec accès en lecture à ce repository
- Git CLI
- SQLite3 CLI
- Interpréteur Python, version 3.6 ou supérieure

Dans le reste de la documentation sur le développement local, il est supposé que la commande `python` de votre OS shell exécute l'interpréteur Python ci-dessus (à moins qu'un environnement virtuel ne soit activé).

### macOS / Linux

#### Cloner le repository

- `cd /path/to/put/project/in`
- `git clone https://github.com/OpenClassrooms-Student-Center/Python-OC-Lettings-FR.git`

#### Créer l'environnement virtuel

- `cd /path/to/Python-OC-Lettings-FR`
- `python -m venv venv`
- `apt-get install python3-venv` (Si l'étape précédente comporte des erreurs avec un paquet non trouvé sur Ubuntu)
- Activer l'environnement `source venv/bin/activate`
- Confirmer que la commande `python` exécute l'interpréteur Python dans l'environnement virtuel
`which python`
- Confirmer que la version de l'interpréteur Python est la version 3.6 ou supérieure `python --version`
- Confirmer que la commande `pip` exécute l'exécutable pip dans l'environnement virtuel, `which pip`
- Pour désactiver l'environnement, `deactivate`

#### Exécuter le site

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pip install --requirement requirements.txt`
- `python manage.py runserver`
- Aller sur `http://localhost:8000` dans un navigateur.
- Confirmer que le site fonctionne et qu'il est possible de naviguer (vous devriez voir plusieurs profils et locations).

#### Linting

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `flake8`

#### Tests unitaires

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pytest`

#### Base de données

- `cd /path/to/Python-OC-Lettings-FR`
- Ouvrir une session shell `sqlite3`
- Se connecter à la base de données `.open oc-lettings-site.sqlite3`
- Afficher les tables dans la base de données `.tables`
- Afficher les colonnes dans le tableau des profils, `pragma table_info(Python-OC-Lettings-FR_profile);`
- Lancer une requête sur la table des profils, `select user_id, favorite_city from
  Python-OC-Lettings-FR_profile where favorite_city like 'B%';`
- `.quit` pour quitter

#### Panel d'administration

- Aller sur `http://localhost:8000/admin`
- Connectez-vous avec l'utilisateur `admin`, mot de passe `Abc1234!`

### Windows

Utilisation de PowerShell, comme ci-dessus sauf :

- Pour activer l'environnement virtuel, `.\venv\Scripts\Activate.ps1` 
- Remplacer `which <my-command>` par `(Get-Command <my-command>).Path`

## Détection, journalisation et analyse des erreurs
Le projet intègre Sentry pour la détection, journalisation et analyse des 
erreurs applicatives.
Les développements futurs s'appuieront sur la journalisation standard Python 
(`logging`) et sur Sentry pour garantir une observabilité de l'application.

### Mise en place d'un nouvel environnement
1. Créer un compte sur Sentry puis créer un nouveau projet de type Django
2. Récupérer le DSN fourni dans les paramètres du projet
3. Ajouter cette valeur dans le fichier `.env`à la racine du projet: 
   `SENTRY_DSN=https://<public_key>@o0.ingest.sentry.io/<project_id>`
4. Vérifier également dans le fichier `.env` la configuration générale: 
   `DEBUG=False` et `LOG_LEVEL=INFO`
5. Redémarrer l'application

### Configuration actuelle
Le projet utilise les paramètres suivants:
- activation conditionnée: Sentry est initialisé uniquement si la valeur 
  `SENTRY_DSN`est défini
- environnement automatique:
  - **développement** si `DEBUG=True`
  - **production** si `DEBUG=False`
- Protection des données personnelles: `send_default_pii=False`
- Monitoring de performance: `traces_sample_rate` configurable dans 
  `settings.py`(par défaut: `1.0`)

### Désactivation
Pour désactiver Sentry sur un environnement donné, il faut simplement 
supprimer la valeur de la variable d'environnement `SENTRY_DSN`.

### Recommandation de sécurité
- Ne jamais versionner le fichier `.env`
- Ne jamais publier le DSN dans un dépôt public
- Utiliser des variables d'environnements pour chaque environnement (local, 
  production)
- Vérifier régulièrement les alertes et les remontées dans Sentry

## Déploiement
Le projet utilise une pipeline CI/CD basée sur GitHub Actions.
À chaque `push` sur la branche principale (`master`):
1. analyse du code avec Flake8
2. exécution des tests avec pytest
3. vérification de la couverture de test (supérieure à 80% par application)
4. construction d'une image Docker
5. publication de l'image sur Docker Hub avec un tag basé sur le latest hash 
   du commit

L'image Docker est ensuite utilisée pour:
- exécution locale via Docker
- déploiement sur AWS Elastic Beanstalk

### Pré-requis
#### Environnement local
- Docker
- Git
#### Déploiement AWS
- Compte AWS
- Accès à la console web AWS

### Déploiement local avec Docker
- vérifier dans DockerHub que l'image Docker est bien publique
- lancer l'application avec la commande suivante:
    ```
    docker run --rm -p 8000:8000 --env-file .env <DOCKERHUB_USERNAME>/oc-lettings-site:latest
    ```
- accès à l'application en allant sur l'url `http://localhost:8000`

Si l'image locale n'est pas à jour, exécuter les commandes suivantes:
```
docker rmi <DOCKERHUB_USERNAME>/oc-lettings-site:latest
docker pull <DOCKERHUB_USERNAME/oc-lettings-site:latest
```

### Déploiement sur AWS Elastic Beanstalk (interface web)
#### Étape 1: création de l'application
1. se connecter à la console AWS
2. aller sur `Elastic Beanstalk`
3. cliquer sur `Créer une application
4. nommer l'application: `oc-lettings-site`

#### Étape 2: permissions IAM (Identity Access Management)
1. aller sur `IAM`
2. créer une nouvelle politique avec les autorisations suivantes: 
   - `EC2`
   - `Elastic Beanstalk`
   - `S3`
   - `CloudFormation`

#### Étape 3: création de l'environnement
1. cliquer sur `Créer un environnement`
2. choisir:
   - `Niveau d'environnement`: `Environnement serveur web`
   - `Plateforme`: `Docker`
3. cliquer sur `Suivant`

#### Étape 4: configuration des variables d'environnement
1. cliquer sur l'environnement créé dans l'étape 2
2. cliquer sur le menu `Configuration`
3. dans la section `Mise à jour, surveillance et journalisation`, ajouter 
   les propriétés d'environnement suivants:
   - Source: `Text brut`, Clé: `ALLOWED_HOSTS`, Valeur: `<URLS-AUTORISES>`
   - Source: `Text brut`, Clé: `DEBUG`, Valeur: `False`
   - Source: `Text brut`, Clé: `SECRET_KEY`, Valeur: 
     `<CLE-SECRETE-APPLICATION-DJANGO>`


#### Étape 5: lancement
1. lancer un commit vide pour lancer la pipeline CI/CD complète:
    ```
    git commit --allow-empty -m "Déploiement"
    git push origin master
    ```
2. accéder à la console AWS > Elastic Beanstalk > Environnement
3. cliquer sur l'environnement de l'application (`oc-lettings-site-env`)
4. cliquer sur le lien du domaine
