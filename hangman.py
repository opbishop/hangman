import random

WORDS = ["monitor", "book"]
HANGMANART = {1: '''
      +---+
      |   |
          |
          |
          |
          |
    =========''', 2: '''
      +---+
      |   |
      O   |
          |
          |
          |
    =========''', 3: '''
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========''', 4: '''
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========''', 5: '''
      +---+
      |   |
      O   |
     /|\  |
          |
          |
    =========''', 6: '''
      +---+
      |   |
      O   |
     /|\  |
     /    |
          |
    =========''', 7: '''
      +---+
      |   |
      O   |
     /|\  |
     / \  |
          |
    ========='''}


def set_up_game():
    word_to_guess = random.choice(WORDS)

    new_game(word_to_guess)


def new_game(word_to_guess):
    display = ["_"] * len(word_to_guess)
    guesses = 7

    while guesses > 0:
        print(display)
        print("Guess a char")
        try:
            g = read_input()
        except ValueError:
            print("Invalid selection - please choose a letter a-zA-Z")

        if g in word_to_guess:
            display = guess(display, word_to_guess, g)
            if check_win(display):
                break
        else:
            guesses -= 1
            display_art(guesses)

    if guesses == 0:
        print("You lose")
    else:
        print("You win")


def read_input():
    input_guess = input()
    if len(input_guess) == 1 & input_guess.isalpha():
        return input_guess
    else:
        raise ValueError


def display_art(guesses):
    print(HANGMANART[7 - guesses])

def guess(display, word_to_guess, g):
    for x in [pos for pos, char in enumerate(word_to_guess) if char == g]:
        display[x] = g
    return display


def check_win(display):
    return "_" not in display


if __name__ == "__main__":
    set_up_game()
