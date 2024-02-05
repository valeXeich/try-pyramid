from setuptools import setup, find_packages

requires = [
    'pyramid',
    'waitress',
    'alembic',
    'SQLAlchemy',
    'psycopg2',
    'pydantic',
    'pydantic-settings'
]

setup(
    name='todo',
    version='0.0',
    description='todo',
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Pyramid',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: WSGI :: Application',
    ],
    author='',
    author_email='',
    url='',
    keywords='web pyramid pylons',
    packages=find_packages(exclude=['tests']),
    include_package_data=True,
    zip_safe=False,
    install_requires=requires,
    entry_points={
        'paste.app_factory': [
            'main = todo:main',
        ]
    },
)
