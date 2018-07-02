from flask import Flask
import hangman

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'hello world'

@app.route('/guess/<string:guess>', methods=["POST"])
def show_guess(guess):
    return guess
