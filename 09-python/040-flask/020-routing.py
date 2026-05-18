from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Home Page"

@app.route("/hello")
def hello():
    return "Hello World!"

@app.route("/hello/<name>")
def parameter(name):
    return f"Hello {name} (from route path)"

@app.route("/parameter-int/<int:times>")
def parameterInt(times):
    text = "Hello! " * times
    return f"{text}<br>{type(times).__name__}"

@app.route("/parameter-float/<float:val>")
def parameterFloat(val):
    text = f"{val} tbsp sugar"
    return f"{text}<br>{type(val).__name__}"

@app.route("/parameter-path/<path:val>")
def parameterPath(val):
    text = f"Path: <pre>{val}</pre>"
    return f"{text}<br>{type(val).__name__}"

@app.route("/canonical/")
def canonical():
    return "Canonical URL"
