from flask import Flask, render_template

app = Flask(__name__)

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    fruits = ['apple', 'banana', 'orange']
    return render_template(
        'hello.html',
        name=name,
        fruits=fruits
    )
