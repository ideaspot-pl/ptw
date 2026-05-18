from flask import Flask, request
from AnalyzedText import AnalyzedText

app = Flask(__name__)

@app.route('/wc', methods=['POST'])
def word_count():
    payload = request.get_data(as_text=True)
    analyzed_text  = AnalyzedText(payload)
    return {
        'text': payload,
        'word_count': analyzed_text.words_count,
        'letters_count': analyzed_text.letters_count
    }
