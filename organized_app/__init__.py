from flask import Flask
#from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from organized_app.routes import routes
from organized_app.models import db

#db = SQLAlchemy()
migrate = Migrate()

def create_app(config):
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///organized_lambdata.db"
    app.register_blueprint(routes)

    db.init_app(app)
    migrate.init_app(app, db)

    return app

if __name__ == "__main__":
    my_app = create_app()
    my_app.run(debug=True) # debug mode allows you to see printed content in development environment
