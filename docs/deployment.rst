Déploiement et gestion de l'application
========================================

Vue d'ensemble
---------------

Le déploiement repose sur:

* GitHub Actions
* Docker
* Docker Hub
* AWS Elastic Beanstalk
* Sentry

Pipeline CI/CD
---------------

La pipeline GitHub Actions exécute:

1. récupération du code source
2. installation des dépendances
3. exécution du linting
4. exécution des tests
5. construction de l'image Docker
6. publication sur Docker Hub
7. déploiement sur AWS Elastic Beanstalk

Variables GitHub Actions
-------------------------

.. list-table::
   :header-rows: 1

   * - Secret
     - Description
   * - SECRET_KEY
     - Clé secrète Django
   * - ALLOWED_HOSTS
     - Liste de hôtes autorisés
   * - SENTRY_DSN
     - DSN Sentry
   * - DOCKERHUB_USERNAME
     - Nom d'utilisateur Docker Hub
   * - DOCKERHUB_TOKEN
     - Token Docker Hub
   * - AWS_ACCESS_KEY_ID
     - Identification AWS
   * - AWS_SECRET_ACCESS_KEY
     - Clé secrète AWS
   * - AWS_REGION
     - Identifiant de la région AWS
   * - EB_APPLICATION_NAME
     - Nom de l'application Elastic Beanstalk
   * - EB_ENVIRONMENT_NAME
     - Nom de l'environnement de l'application EB
   * - EB_S3_BUCKET
     - Identifiant du bucket S3


Déploiement Docker
------------------

.. code-block:: bash

    docker build -t oc-lettings-site .
    docker run -p 8000:8000 --env-fil .env  oc-lettings-site


Déploiement AWS Elastic Beanstalk
-----------------------------------

Le déploiement est automatisé par GitHub Actions lors d'un push sur ``master``.

Surveillance avec Sentry
------------------------

Sentry permet de suivre les erreurs applicatives et les exceptions Django.