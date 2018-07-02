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
        g = input()

        if g in word_to_guess:
            display = guess(display, word_to_guess, g)
            if check_win(display):
                break
        else:
            guesses -= 1
            print(HANGMANART[7 - guesses])

    if guesses == 0:
        print("You lose")
    else:
        print("You win")


def guess(display, word_to_guess, g):
    for x in [pos for pos, char in enumerate(word_to_guess) if char == g]:
        display[x] = g
    return display


def check_win(display):
    return "_" not in display


if __name__ == "__main__":
    set_up_game()
