
from flask import Blueprint, jsonify, request, current_app

from organized_app.models import User, Tweet #,db

routes = Blueprint("routes", __name__)

@routes.route("/")
def home():
    print("HOME")
    return jsonify({"message":"WELCOME HOME"})

@routes.route("/users")
@routes.route("/users.json")
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

@routes.route("/users/new/")
def create_user():
    db = current_app["db"]
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

@routes.route("/tweets")
@routes.route("/tweets.json")
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
@routes.route("/tweets/new/")
def create_tweet():
    db = current_app["db"]
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
