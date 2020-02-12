
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
@app.route("/hello")
def index():
    return "Hello World!"

@app.route("/hello.json")
def hello():
    return jsonify({"message": "Hello World", "things": [1,2,3]})
