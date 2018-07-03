import random


class HangmanGame:

    def __init__(self):
        self.WORDS = ["monitor", "book"]
        self.HANGMANART = {1: '''
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
        self.guesses = 7
        self.word_to_guess = random.choice(self.WORDS)

    def new_game(self):
        display = ["_"] * len(self.word_to_guess)

        while self.guesses > 0:
            print(display)
            valid_input = False

            while valid_input is not True:
                print("Guess a char")
                input_guess = input()
                try:
                    valid_input = self.validate_input(input_guess)
                except (ValueError, TypeError):
                    print("Invalid selection - please choose a single letter a-zA-Z")

            if input_guess in self.word_to_guess:
                display = self.guess(display, input_guess)
                if self.is_over(display):
                    break
            else:
                self.guesses -= 1
                self.display_art(self.guesses)

        if self.guesses == 0:
            print("You lose")
        else:
            print("You win")



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
            print(self.HANGMANART[7 - guesses])

    def guess(self, display, g):
        for x in [pos for pos, char in enumerate(self.word_to_guess) if char == g]:
            display[x] = g
        return display

    @staticmethod
    def is_over(display):
        return "_" not in display
