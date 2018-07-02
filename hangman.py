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
        valid_input = False

        while valid_input is not True:
            print("Guess a char")
            input_guess = input()
            try:
                valid_input = validate_input(input_guess)
            except (ValueError, TypeError):
                print("Invalid selection - please choose a single letter a-zA-Z")


        if input_guess in word_to_guess:
            display = guess(display, word_to_guess, input_guess)
            if check_win(display):
                break
        else:
            guesses -= 1
            display_art(guesses)

    if guesses == 0:
        print("You lose")
    else:
        print("You win")


def validate_input(input_guess):
    if len(input_guess) != 1:
        raise ValueError
    elif not input_guess.isalpha():
        raise TypeError
    else:
        return True


def display_art(guesses):
    if guesses > 7 or guesses < 0:
        raise ValueError
    else:
        print(HANGMANART[7 - guesses])


def guess(display, word_to_guess, g):
    for x in [pos for pos, char in enumerate(word_to_guess) if char == g]:
        display[x] = g
    return display


def check_win(display):
    return "_" not in display


if __name__ == "__main__":
    set_up_game()
