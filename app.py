from flask import Flask, request, render_template
from syllabicator import syllabicator_i
import re
import string

# set the project root directory as the static folder, you can set others.
app = Flask(__name__, static_url_path='/static')

@app.route('/')
def root():
    return app.send_static_file('index.html')


@app.route('/syllabify', methods = ['POST'])
def syllabify():
    text = request.form['text']
    text = syllabicator_i.pre_process_word(text)
    words = []
    syllables = []
    for word in text.strip().lower().split():
        words.append(word)
        try:
            syllables.append(syllabicator_i.syllabicate(word))
        except ValueError:
            syllables.append(' ')
    
    return render_template('syllables.html', **locals())


if __name__ == '__main__':
    app.run(debug=True)

