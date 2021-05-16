from flask import Flask
from flask import url_for

app = Flask(__name__)

@app.route("/")
def index():
    return "index"

@app.route("/login")
def login():
    return "login"


@app.route("/profile/<username>")
def profile(username):
    return f'{username}\'s profile'

with app.test_request_context():
    print(url_for('index'))
    print(url_for('login'))
    print(url_for('login', unknownquery='flow'))
    print(url_for('profile', username='John Doe'))
