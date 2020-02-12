
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

(BONUS) HTTP Slides:
  + https://docs.google.com/presentation/d/1K83U0VjYob6dgdRodbidWBtFxK4Q_9h8zojzmto2wJY/edit#slide=id.g5846519fbe_0_1904

Flask:

  + https://github.com/pallets/flask
  + https://palletsprojects.com/p/flask/
  + https://flask.palletsprojects.com/en/1.1.x/quickstart/
  + https://flask.palletsprojects.com/en/1.1.x/patterns/appfactories/

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

STRETCH GOALS / FURTHER EXPLORATION...

Twitter Bootstrap:
  + https://getbootstrap.com/docs/4.4/getting-started/introduction/

Using Twitter Bootstrap to improve the look and feel of your HTML view templates, and inheriting HTML contents from a common base layout, and other template examples:
  + https://github.com/prof-rossetti/web-app-starter-flask-sheets/blob/master/web_app/templates/layout.html
  + https://github.com/prof-rossetti/web-app-starter-flask-sheets/blob/master/web_app/templates/index.html
  + https://github.com/prof-rossetti/web-app-starter-flask-sheets/blob/master/web_app/templates/products/index.html

Example of flash and redirect:
  + https://github.com/prof-rossetti/web-app-starter-flask-sheets/blob/master/web_app/routes/products_api.py#L31-L32

## Class 2

Lambda Materials:

  + https://learn.lambdaschool.com/ds/module/recVFIbE3mpjpVGrj/
  + https://github.com/LambdaSchool/DS-Unit-3-Sprint-3-Productization-and-Cloud/tree/master/module2-consuming-data-from-an-api

The requests package:

  + _________

The AlphaVantage API:

  + _________

The Twitter API and Tweepy Package:

  + _________

The Basilica API:

  + https://www.basilica.ai/quickstart/python/
  + https://www.basilica.ai/api-keys/
  + https://basilica-client.readthedocs.io/en/latest/basilica.html

## Class 3

  + https://learn.lambdaschool.com/ds/module/recZOXl2H7Bbd1LMK/

## Class 4

  + https://learn.lambdaschool.com/ds/module/recpPYQdaOmZdBSYq/
