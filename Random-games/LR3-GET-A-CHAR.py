import random
import string

def print_bold(msg, end='\n'):
    print("\033[1m" + msg + "\033[0m", end=end)


class GameExceptions(Exception):
    def __init__(self, message=''):
        super().__init__(message)
        self.padding = '~'*50 + '\n'
        self.error_message = "Undefined ERROR"


class InputTypeException(GameExceptions):
    def __init__(self, message=''):
        super().__init__(message)
        self.error_message = (self.padding + "ERROR: Вы ввели не число!"
        + '\n' + self.padding)


class QuessAChar:
    def __init__(self):
        self.result = False
        self.compChar = random.choice(string.ascii_lowercase)
        self.rightAnswer = 'Ура - ты угадал число'
        self.wrongAnswer = 'Не угадал, попробуй еще раз.'

    def show_game_rules(self):
        """Print the game rules QuessNumber in the console"""
        print_bold("Правила игры:")
        print("Я загадываю случайную букву английского алфавита - а ты должен ее угадать.")
        print("---------------------------------------------------------\n")

    def check_result(self):
            suggestChar = input("Какую букву я загдал?")
            "self.validate_input(suggestUserNumber)"
            print(self.compChar)
            if suggestChar == self.compChar:
                self.result = True
                print(self.rightAnswer)
            else:
                print(self.wrongAnswer)

    def play(self):
        self.show_game_rules()
        while not self.result:
            self.check_result()


if __name__ == '__main__':
    game = QuessAChar()
    game.play()

