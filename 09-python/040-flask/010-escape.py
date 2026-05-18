from flask import Flask, request
from markupsafe import escape

app = Flask(__name__)

@app.route("/hello-raw")
def raw():
    name = request.args.get("name", "World")
    return f"Hello, {name}!"

@app.route("/hello-escaped")
def escaped():
    name = request.args.get("name", "World")
    return f"Hello, {escape(name)}!"
