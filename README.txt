todo
====

Getting Started
---------------

- Create a Python virtual environment, if not already created.

    python3 -m venv env

- Upgrade packaging tools, if necessary.

    try-pyramid/pip install --upgrade pip setuptools

- Upgrade the database using Alembic.

    - Upgrade to that revision.

        try-pyramid/alembic -c development.ini upgrade head

- Run your project from.

    try-pyramid/pserve development.ini
