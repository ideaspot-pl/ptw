from flask import Flask, render_template, flash

app = Flask(__name__)
app.secret_key = 'veryharddontguess' # for flash to work

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/flash')
def flash_index():
    return render_template('flash.html')

@app.route('/flash/green')
def flash_green():
    flash('Green button was clicked!', 'success')
    return render_template('flash.html')

@app.route('/flash/red')
def flash_red():
    flash('Red button was clicked!', 'danger')
    return render_template('flash.html')
