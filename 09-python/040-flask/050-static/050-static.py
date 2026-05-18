from flask import Flask, url_for


app = Flask(__name__)


@app.route("/")
def index():
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>Hello World!</title>
    <link
        rel="stylesheet"
        type="text/css"
        href="{url_for('static', filename='style.css')}"
    >
</head>
<body>
    <h1>Hello World!</h1>
</body>
</html>"""

    return html
