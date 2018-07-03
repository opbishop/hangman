from flask import Flask
import hangman

app = Flask(__name__)
game = None

@app.route('/')
def new_game():
    global game
    game = hangman.HangmanGame()
    return "{}".format(game.display)


@app.route('/guess_character/<string:guess>')
def show_guess(guess):
    global game
    if game is None:
        game = hangman.HangmanGame()
    return "{}".format(game.guess_character(guess))
