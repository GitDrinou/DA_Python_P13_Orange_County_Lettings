Interface de programmation
==========================

Vue d'ensemble
---------------

L'application expose principalement des routes web Django.

Routes principales
-------------------

.. list-table::
   :header-rows: 1

   * - Route
     - Vue
     - Description
   * - /
     - index
     - Page d'accueil
   * - /lettings/
     - lettings:index
     - Liste des locations
   * - /lettings/<id>/
     - lettings:letting
     - Détail d'une location
   * - /profiles/
     - profiles:index
     - Liste des profils
   * - /profiles/<username>/
     - profiles:profile
     - Détail d'un profil
   * - /admin/
     - Django Admin
     - Interface d'administration
