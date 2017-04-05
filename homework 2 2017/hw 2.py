__author__ = 'IrinaPavlova'

from flask import Flask, render_template, url_for
app = Flask(__name__)

@app.route('/')
def home_page():
    return render_template('home_page.html')

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

if __name__ == "__main__":
    app.run(debug=True)