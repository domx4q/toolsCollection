Server
======

The Server was the initial plan for the project. It is a `FastAPI <https://fastapi.tiangolo.com/>`_ server which makes the :doc:`tools` available via a REST API. It also provides access to its own SQLite database system.


Endpoints
---------
.. list-table::
   :widths: 25 50
   :header-rows: 1

   * - Endpoint
     - Function

   * - ``/``
     - root
   * - ``/crypto/decrypt``
     - decrypt
   * - ``/crypto/encrypt``
     - encrypt
   * - ``/crypto/generateKey``
     - generate_key
   * - ``/crypto/hash``
     - hash_string
   * - ``/db/add``
     - add_user
   * - ``/db/connect``
     - connect
   * - ``/db/create``
     - create_table
   * - ``/db/delete``
     - delete_user
   * - ``/db/deleteall``
     - delete_all_users
   * - ``/db/get``
     - get_user
   * - ``/db/getall``
     - get_all_users
   * - ``/db/list``
     - listTables
   * - ``/db/update``
     - update_user
   * - ``/docs``
     - swagger_ui_html
   * - ``/docs/oauth2-redirect``
     - swagger_ui_redirect
   * - ``/openapi.json``
     - openapi
   * - ``/ping``
     - ping
   * - ``/redoc``
     - redoc_html


.. _swagger_ui_html:

Swagger UI
----------
For a better visualization of the API, the `Swagger UI <https://swagger.io/tools/swagger-ui/>`_ is available at ``/docs``.

.. openapi:: _static/openapi.yaml