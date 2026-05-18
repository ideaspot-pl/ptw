from flask import Flask, request
from AnalyzedText import AnalyzedText

app = Flask(__name__)

@app.route('/wc', methods=['POST'])
def word_count():
    # get data from request (as text)
    # instantiate AnalyzedText
    # return dictionary with text, word count and letters count as keys
    # flask will make it JSON on its own
    return {}
