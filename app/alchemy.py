

from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///lambdata1.db"

db = SQLAlchemy(app)

migrate = Migrate(app, db)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))

@app.route("/")
@app.route("/users")
@app.route("/users.json")
def users():
    print("GET USERS")
    users = User.query.all() # returns a list of <class 'alchemy.User'>
    print(len(users))

    # h/t: https://stackoverflow.com/questions/1958219/convert-sqlalchemy-row-object-to-python-dict
    #users_response = [u.__dict__ for u in users]
    #users_response = [del myu["_sa_instance_state"] for u in users_response]
    users_response = []
    for u in users:
        print(u)
        d = u.__dict__
        del d["_sa_instance_state"]
        users_response.append(d)

    return jsonify(users_response)

@app.route("/users/new/")
def create_user():
    print("CREATE USER")
    print("ARGS:", request.args)
    #> ImmutableMultiDict([])
    #> ImmutableMultiDict([('name', 'MyUser')])
    if "name" in request.args:
        name = request.args["name"]
        print(name)
        db.session.add(User(name=name))
        db.session.commit()
        return jsonify({"message": "CREATED OK", "name": name})
    else:
        return jsonify({"message": "OOPS PLEASE SPECIFY A NAME!"})









#if __name__ == "__main__":
#    pass
