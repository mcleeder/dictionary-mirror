from flask import Flask
from markupsafe import Markup
from dictionary import dictionary
import json

app = Flask(__name__)

@app.route("/", methods=['GET'])
def hello_world(world: str = "world"):
    return Markup("<p>Hello, %s!</p>") % world.title()

@app.route("/<string:topic>", methods=['GET'])
def topics(topic: str = None):
    return json.dumps(dictionary.lookup(topic))