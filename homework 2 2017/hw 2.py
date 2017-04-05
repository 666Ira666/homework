__author__ = 'IrinaPavlova'

from flask import Flask, render_template, url_for
app = Flask(__name__)

url_for('static', filename='style.css')
