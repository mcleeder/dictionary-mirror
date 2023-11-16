from flask import Flask, render_template
from markupsafe import Markup
from dictionary import dictionary
import json

app = Flask(__name__)

@app.route("/", methods=['GET'])
def hello_world(world: str = "world"):
    return Markup("<p>Hello, %s!</p>") % world.title()

@app.route("/<string:topic>", methods=['GET'])
def topics(topic: str = None):
    data = dictionary.lookup(topic)
    return render_template("index.html", word=data)