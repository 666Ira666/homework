from flask import Flask, render_template, request, session, flash
from random import choice
import os

app = Flask(__name__)

for root, dirs, files in os.walk('./static/images/gifs/'):
    files = files
rand = list(filter(lambda file: file.endswith('.gif'), files))

gif = './static/images/gifs/' + choice(rand)

@app.route('/')
def home(g=gif):
    if not session.get('logged_in'):
        return render_template('login.html', g=g)
    else:
        return render_template('home_page.html', g=g)


@app.route('/login', methods=['POST'])
def do_admin_login():
    db = {'Timofey': 'tim123', 'admin': 'password'}
    if request.form['username'] in db:
        if request.form['password'] == db[request.form['username']]:
            session['logged_in'] = True
        else:
            return home()
    else:
        return home()
    return home()


@app.route("/logout")
def logout():
    session['logged_in'] = False
    return home()


@app.route("/search", methods=['GET', 'POST'])
def search():
    q2 = False
    if request.method == "POST":
        sentences = []
        query1 = request.form['query1']
        query2 = request.form['query2']
        print(type(request.form['case']), request.form['case'])
        if query2 is '':
            corpus = open('./texts/corpus.txt', 'r', encoding='utf-8')
            if not request.form['case'] == 'Case sensitive search':
                corpus_read = corpus.read().lower().split()
                number = corpus_read.count(query1)
                corpus.close()
                corpus = open('./texts/corpus.txt', 'r', encoding='utf-8')
                num = 0
                for line in corpus:
                    if query1.lower() in line.lower().split():
                        num += 1
                        sentences.append([num, line])
            else:
                corpus_read = corpus.read().split()
                number = corpus_read.count(query1)
                corpus.close()
                corpus = open('./texts/corpus.txt', 'r', encoding='utf-8')
                num = 0
                for line in corpus:
                    if query1 in line.split():
                        num += 1
                        sentences.append([num, line])
            return search_results(query1, number, sentences, q2)
        else:
            q2 = True
            number = 0
            corpus = open('./texts/corpus.txt', 'r', encoding='utf-8')
            num = 0
            for line in corpus:
                if not request.form['case'] == 'Case sensitive search':
                    line_n = line.lower().split()
                else:
                    line_n = line.lower()
                for w in range(len(line_n)):
                    if query1 == line_n[w] and query2 == line_n[w+1]:
                        num += 1
                        sentences.append([num, line])
                        number += 1
            corpus.close()
            print(sentences)
            return search_results(query1 + ' ' + query2, number, sentences, q2)

    return render_template('search_page.html')


@app.route("/search/results/<q>", methods=['GET', 'POST'])
def search_results(q, n, sentences, q2):
    return render_template('search_query_page.html', q=q, n=n, s=sentences, q2=q2)

if __name__ == "__main__":
    app.secret_key = os.urandom(12)
    app.run(debug=True)