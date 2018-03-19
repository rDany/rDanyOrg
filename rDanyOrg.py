import json
import urllib
import random
from flask import Flask
from flask import request
from flask import render_template


app = Flask(__name__)


@app.route('/<lang>')
def index_lang(lang):

    with open("answers.json") as data_file:
        answers = json.load(data_file)
    all_answers = {}
    for answer in answers:
        if answer["lang"] not in all_answers:
            all_answers[answer["lang"]] = []
        all_answers[answer["lang"]].append(answer["q"])
    if lang not in all_answers:
        lang = "en"
    data = {
        "question": "",
        "all_questions": all_answers[lang],
        "lang": lang
    }
    return render_template('index_lang.html', **data)


@app.route('/')
def index():
    data = {
        "question": "",
        "lang": "mul"
    }
    return render_template('index.html', **data)


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
            current_lang = answer["lang"]
    other_questions = []
    for n in range(30):
        select_random = random.choice(all_answers)
        if select_random["lang"] == current_lang:
            other_questions.append(select_random["q"])
    data = {
        "question": question,
        "answer": current_answer,
        "other_questions": other_questions,
        "lang": current_lang
    }
    return render_template('ask.html', **data)


@app.route('/sitemap.txt')
def sitemap():
    with open("answers.json") as data_file:
        answers = json.load(data_file)
    sitemap_text = "https://rdany.org"
    for answer in answers:
        sitemap_text = "{}\nhttps://rdany.org/ask?q={}".format(sitemap_text, urllib.parse.quote_plus(answer["q"]))
    return sitemap_text


@app.route('/robots.txt')
def robots():
    return "User-agent: *\nDisallow:"


@app.route('/amp')
def amp():
    return render_template('amp.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
