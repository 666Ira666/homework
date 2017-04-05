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

if __name__ == "__main__":
    app.secret_key = os.urandom(12)
    app.run(debug=True)