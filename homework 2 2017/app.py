from flask import Flask, flash, redirect, render_template, request, session, abort
import os

app = Flask(__name__)


@app.route('/')
def home():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return render_template('home_page.html')


@app.route('/login', methods=['POST'])
def do_admin_login():
    db = {'Timofey': 'tim123', 'admin': 'password'}
    if request.form['username'] in db:
        if request.form['password'] == db[request.form['username']]:
            session['logged_in'] = True
        else:
            return render_template('home_page.html')
    else:
        return render_template('home_page.html')
    return home()


@app.route("/logout")
def logout():
    session['logged_in'] = False
    return home()


@app.route("/search", methods=['GET', 'POST'])
def search():
    if request.method == "POST":
        sentences = []
        query = request.form['query']
        corpus = open('corpus.txt', 'r', encoding='utf-8')
        corpus_read = corpus.read().lower().split()
        number = corpus_read.count(query)
        corpus.close()
        corpus = open('corpus.txt', 'r', encoding='utf-8')
        num = 0
        for line in corpus:
            if query.lower() in line.lower().split():
                num += 1
                sentences.append([num, line])
        return search_results(query, number, sentences)
    return render_template('search_page.html')


@app.route("/search/results/<q>", methods=['GET', 'POST'])
def search_results(q, n, sentences):
    return render_template('search_query_page.html', q=q, n=n, s=sentences)

if __name__ == "__main__":
    app.secret_key = os.urandom(12)
    app.run(debug=True)