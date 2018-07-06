from flask import Flask, render_template
import hangman

app = Flask(__name__)
game = None


@app.route('/')
def new_game():
    global game
    game = hangman.HangmanGame()
    return render_template('hangman.html', game=game)


@app.route('/guess_character/<string:guess>')
def show_guess(guess):
    global game
    if game is None:
        game = hangman.HangmanGame()
    game.guess_character(guess)
    if game.is_over():
        return "You win"
    else:
        return render_template('hangman.html', game=game)
