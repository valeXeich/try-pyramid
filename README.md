todo
====

Getting Started
---------------

- Create a Python virtual environment, if not already created.


    ```bash
    python -m venv env
    ```

- Upgrade packaging tools, if necessary.


    ```bash
    pip install --upgrade pip setuptools
    ```

- Сreate .env file.

  Example:

    ```env
    DB_URL=postgresql+psycopg2://postgres:postgres@localhost/postgres

    POSTGRES_USER=postgres
    POSTGRES_PASSWORD=postgres
    POSTGRES_DB=postgres
    
    PGADMIN_DEFAULT_EMAIL=admin@admin.com
    PGADMIN_DEFAULT_PASSWORD=admin
    ```

- Upgrade the database using Alembic.

    ```bash
    alembic -c development.ini upgrade head
    ```

- Run your project from.

    ```bash
    pserve development.ini
    ```
