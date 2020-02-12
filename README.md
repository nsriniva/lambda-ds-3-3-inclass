
# Lambda Unit 3 - Sprint 3

[Productization and Cloud](https://learn.lambdaschool.com/ds/sprint/recvbdRfBNCqSB4hd)


Setup:

```sh
conda create -n lambda-flask-env python=3.7
conda activate lambda-flask-env
pip install -r requirements.txt
cd app/
```

Basic routing:

```sh
FLASK_APP=hello.py flask run
```

Database-backed:


```sh
FLASK_APP=alchemy.py flask db init #> generates app/migrations dir

# run both when changing the schema:
FLASK_APP=alchemy.py flask db migrate #> creates the db (with "alembic_version" table)
FLASK_APP=alchemy.py flask db upgrade #> creates the "users" table

FLASK_APP=alchemy.py flask run
```


Organized:


```sh

FLASK_APP=organized_app flask db init #> generates app/migrations dir

# run both when changing the schema:
FLASK_APP=organized_app flask db migrate #> creates the db (with "alembic_version" table)
FLASK_APP=organized_app flask db upgrade #> creates the "users" table

FLASK_APP=organized_app flask run
```


## Class 1

Topics:

  1. Client-server architecture and HTTP
  2. Flask routing and views
  3. Adding a database (Flask SQL Alchemy)

Lambda Materials:

  + https://learn.lambdaschool.com/ds/module/recKGvwkPaEsfnwDL/
  + https://github.com/LambdaSchool/DS-Unit-3-Sprint-3-Productization-and-Cloud/tree/master/module1-web-application-development-with-flask

Flask:

  + https://github.com/pallets/flask
  + https://palletsprojects.com/p/flask/
  + https://flask.palletsprojects.com/en/1.1.x/quickstart/

Alchemy:

  + https://github.com/pallets/flask-sqlalchemy/
  + https://flask-sqlalchemy.palletsprojects.com/en/2.x/
  + https://flask-sqlalchemy.palletsprojects.com/en/2.x/api/#models
  + https://docs.sqlalchemy.org/en/13/core/type_basics.html
  + https://docs.sqlalchemy.org/en/13/orm/join_conditions.html?highlight=foreign%20key

Migrate:

  + https://flask-migrate.readthedocs.io/en/latest/
  + https://github.com/miguelgrinberg/Flask-Migrate

Bonus Examples:

  + https://github.com/prof-rossetti/web-app-starter-flask
  + https://github.com/prof-rossetti/web-app-starter-flask-sheets
  + https://github.com/prof-rossetti/salad-system-alchemy (MySQL version)

## Class 2

  + https://learn.lambdaschool.com/ds/module/recVFIbE3mpjpVGrj/

## Class 3

  + https://learn.lambdaschool.com/ds/module/recZOXl2H7Bbd1LMK/

## Class 4

  + https://learn.lambdaschool.com/ds/module/recpPYQdaOmZdBSYq/
