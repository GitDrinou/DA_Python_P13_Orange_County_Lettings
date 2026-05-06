=======================
Installation du projet
=======================

Prérequis
---------

Avant d'installer le projet, vérifier que les outils suivants sont disponibles :

* Python 3.8 ou supérieur
* Git
* pip
* virtualenv
* Docker

Cloner le projet
-----------------

.. code-block:: bash

    git clone https://github.com/GitDrinou/DA_Python_P13_Orange_County_Lettings.git

Créer  et activer un environnement virtuel
-------------------------------

.. code-block:: bash

    python -m venv venv
    source venv/bin/activate

Sous Windows:

.. code-block:: bash

    venv\Scripts\activate

Installer les dépendances
--------------------------

.. code-block:: bash

    pip install -r requirements.txt

Configurer les variables d'environnement
-----------------------------------------

Créer un fichier ``.env`` à partir du fichier d'exemple:

.. code-block:: bash

    cp .env.example .env

Variables principales:

.. code-block:: bash

    SECRET_KEY=clé-secrète-django
    DEBUG=False
    ALLOWED_HOSTS=localhost, 127.0.0.1
    SENTRY_DSN=<dsn-sentry>
    LOG_LEVEL=INFO

Initialiser la base de données
------------------------------

.. code-block:: bash

    python manage.py migrate

Lancer le serveur
-----------------

.. code-block:: bash

    python manage.py runserver
