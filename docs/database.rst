===========================
Base de données et modèles
===========================

Vue d'ensemble
---------------

Le projet utilise l'ORM de Django.

Les principales applications métier sont:

* ``lettings``
* ``profiles``

Modèle Address
---------------

Le modèle ``Address`` représente une adresse postale associée à une location.

.. list-table::
   :header-rows: 1

   * - Champ
     - Type
     - Description
   * - number
     - PositiveIntegerField
     - Numéro de rue
   * - street
     - CharField
     - Nom de rue
   * - city
     - CharField
     - Ville
   * - state
     - CharField
     - Code d'état
   * - zip_code
     - PositiveIntegerField
     - Code postal
   * - country_iso_code
     - CharField
     - Code ISO du pays

Modèle Letting
---------------

Le modèle ``Letting`` représente une annonce de location.

.. list-table::
   :header-rows: 1

   * - Champ
     - Type
     - Description
   * - title
     - CharField
     - Titre de l'annonce
   * - address
     - OneToOneField
     - Adresse associé à la location

Modèle Profile
---------------

Le modèle ``Profile`` étend le modèle utilisateur natif de Django.

.. list-table::
   :header-rows: 1

   * - Champ
     - Type
     - Description
   * - user
     - OneToOneField
     - Utilisateur Django associé
   * - favorite_city
     - CharField
     - Ville favorite
