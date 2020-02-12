

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

class Tweet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.String)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))

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

@app.route("/tweets")
@app.route("/tweets.json")
def get_tweets():
    print("GET TWEETS")
    tweets = Tweet.query.all()
    print(len(tweets))
    response = []
    for t in tweets:
        print(t)
        d = t.__dict__
        del d["_sa_instance_state"]
        response.append(d)
    return jsonify(response)

# http://localhost:5000/tweets/new/?user_id=1&status=Hello%20World
@app.route("/tweets/new/")
def create_tweet():
    print("CREATE TWEET")
    print("ARGS:", request.args)
    if "user_id" in request.args and "status" in request.args:
        user_id = request.args["user_id"] # todo: validate?
        status = request.args["status"]
        db.session.add(Tweet(user_id=user_id, status=status))
        db.session.commit()
        return jsonify({"message": "CREATED OK", "user_id": user_id, "status": status})
    else:
        return jsonify({"message": "OOPS PLEASE SPECIFY A USER_ID AND STATUS!"})
