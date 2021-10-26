import random


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


class NumberHigher(GameExceptions):
    def __init__(self, message=''):
        super().__init__(message)
        self.error_message = (self.padding + "ERROR: Введенное число больше максимально допустимого!"
        + '\n' + self.padding)


class NumberLower(GameExceptions):
    def __init__(self, message=''):
        super().__init__(message)
        self.error_message = (self.padding + "ERROR: Введенное число меньше минамально допустимого!"
        + '\n' + self.padding)


class QuessNumber:
    def __init__(self):
        self.result = False
        self.topNumber = 100
        self.quessedNumber = random.randint(1, self.topNumber)
        self.hoorayText = 'Ура - ты угадал число'
        self.looserText = 'Не угадал, попробуй еще раз.'

    def show_game_rules(self):
        """Print the game rules QuessNumber in the console"""
        print_bold("Rules of Game:")
        print(" I generate a random number from 1 to 100, you need to quess what is it.")
        print("---------------------------------------------------------\n")

    def validate_input(self, input:any):
        if input > 100:
            raise NumberHigher("Inputted number more than max value")
        if input < 0:
            raise NumberLower("Inputted number lower than min value")

    def check_result(self):

        try:
            suggestUserNumber = int(input(".... What you suggest number?"))
            self.validate_input(suggestUserNumber)
            if suggestUserNumber == self.quessedNumber:
                self.result = True
                print(self.hoorayText)
            else:
                print(self.looserText)
        except ValueError:
            raise InputTypeException("Input is not a int type")


    def play(self):
        self.show_game_rules()
        print(self.quessedNumber)
        while not self.result:
            self.check_result()


if __name__ == '__main__':
    game = QuessNumber()
    game.play()




