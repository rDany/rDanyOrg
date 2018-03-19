import json
import urllib
import random
from flask import Flask
from flask import request
from flask import render_template


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('ask.html', question="¿Hola?")


@app.route('/ask/<hash>/')
@app.route('/ask/<hash>')
@app.route('/ask')
def ask(hash=None):
    question = request.args.get('q', '')
    with open("answers.json") as data_file:
        answers = json.load(data_file)
    all_answers = []
    for answer in answers:
        all_answers.append(answer)
        if answer["q"] == question:
            current_answer = answer["a"]
    other_questions = []
    for n in range(5):
        other_questions.append(random.choice(all_answers)["q"])
    return render_template('ask.html', question=question, answer=current_answer, other_questions=other_questions, lang="es")


@app.route('/sitemap.txt')
def sitemap():
    with open("answers.json") as data_file:
        answers = json.load(data_file)
    sitemap_text = "https://rdany.org"
    for answer in answers:
        sitemap_text = "{}\nhttps://rdany.org/ask?q={}".format(sitemap_text, urllib.parse.quote_plus(answer["q"]))
    return sitemap_text

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
