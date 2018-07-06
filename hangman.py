import random
import string


class HangmanGame:

    def __init__(self):
        self.WORDS = ["monitor", "book"]
        self.CHARSET = list(string.ascii_lowercase)
        self.HANGMANART = {1: '''
          +---+
          |   |\n
              |\n
              |\n
              |\n
              |\n
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
        self.guesses = 7
        self.word_to_guess = random.choice(self.WORDS)
        self.display = ["_"] * len(self.word_to_guess)

    @staticmethod
    def validate_input(input_guess):
        if len(input_guess) != 1:
            raise ValueError
        elif not input_guess.isalpha():
            raise TypeError
        else:
            return True

    def display_art(self, guesses):
        if self.guesses > 7 or self.guesses < 0:
            raise ValueError
        else:
            return self.HANGMANART[7 - guesses]

    def guess_character(self, input_guess):
        if input_guess in self.word_to_guess:
            for x in [pos for pos, char in enumerate(self.word_to_guess) if char == input_guess]:
                self.display[x] = input_guess

        else:
            self.guesses -= 1



    def is_over(self):
        return "_" not in self.display
