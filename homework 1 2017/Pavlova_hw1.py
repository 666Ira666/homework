__author__ = 'IrinaPavlova'

from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'

count_db = {}


@app.route('/user/<username>')
def show_user_profile(username):
    if str(username) in count_db:
        count_db[str(username)] += 1
    else:
        count_db[str(username)] = 1
    if count_db[str(username)] == 1:
        return 'Hello, %s' % username + '<br/>Your page was viewed %s time' % count_db[str(username)]
    else:
        return 'Hello, %s' % username + '<br/>Your page was viewed %s times' % count_db[str(username)]

if __name__ == "__main__":
    app.run()