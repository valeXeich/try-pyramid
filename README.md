todo
====

Getting Started
---------------

- Create a Python virtual environment, if not already created.

    python3 -m venv env

- Upgrade packaging tools, if necessary.

    try-pyramid/pip install --upgrade pip setuptools

- Сreate try-pyramid/.env file.

    ```env
    DB_URL=postgresql+psycopg2://postgres:postgres@localhost/postgres

    POSTGRES_USER=postgres
    POSTGRES_PASSWORD=postgres
    POSTGRES_DB=postgres
    
    PGADMIN_DEFAULT_EMAIL=admin@admin.com
    PGADMIN_DEFAULT_PASSWORD=admin
    ```

- Upgrade the database using Alembic.

    - Upgrade to that revision.

        try-pyramid/alembic -c development.ini upgrade head

- Run your project from.

    try-pyramid/pserve development.ini
