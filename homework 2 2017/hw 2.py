__author__ = 'IrinaPavlova'

from flask import Flask, render_template, url_for
app = Flask(__name__)

with app.test_request_context():
    print(url_for('static', filename='style.css'))
