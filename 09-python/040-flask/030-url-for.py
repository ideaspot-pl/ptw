from flask import Flask, url_for

app = Flask(__name__)

@app.route("/")
def index():
    url = url_for("post_index")
    return f"Index Page. Go to <a href='{url}'>{url}</a>"

@app.route("/post/")
def post_index():
    url = url_for('post_edit', id=3)
    return f'Post Index. Go to <a href="{url}">{url}</a>'

@app.route("/post/<int:id>/")
def post_edit(id):
    url = url_for('post_index')
    return f"Post {id} Edit. Go back to post index <a href='{url}'>{url}</a>"
