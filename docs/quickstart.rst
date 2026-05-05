Guide de démarrage rapide
==========================

Démarrage local
----------------

.. code-block:: bash

    python manage.py runserver

L'application est disponible à l'adresse:

.. code-block:: bash

    http://127.0.0.1:8000/

Lancer les tests
-----------------

.. code-block:: bash

    pytest

Construire l'image Docker
-------------------------

.. code-block:: bash

    docker build -t oc-lettings-site .

Lancer l'application avec Docker
--------------------------------

.. code-block:: bash

    docker run -p 8000:8000 --env-fil .env oc-lettings-site