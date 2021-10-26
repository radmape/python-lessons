import random
import io


def print_bold(msg, end='\n'):
    print("\033[1m" + msg + "\033[0m", end=end)


class GameExceptions(Exception):
    def __init__(self, message=''):
        super().__init__(message)
        self.padding = '~'*50 + '\n'
        self.error_message = "Undefined ERROR"


class InputValueException(GameExceptions):
    def __init__(self, message=''):
        super().__init__(message)
        self.error_message = (self.padding + "ERROR: Вы ввели больше 1 символа"
        + '\n' + self.padding)


class PoleChydes:
    def __init__(self):
        self.wordsFile = io.open('polechydes-5simv.txt', encoding='utf-8')
        self.lines = self.wordsFile.readlines()
        self.randomWord = random.choice(self.lines)
        self.resultGame = False
        self.resultPlayerWord = '_____'
        self.rightAnswer = 'Ура - ты угадал число'
        self.wrongAnswer = 'Не угадал, попробуй еще раз.'

    def show_game_rules(self):
        """Print the game rules QuessNumber in the console"""
        print_bold("Правила игры:")
        print("Я загадываю случайное русское слово из 5 букв, а ты можешь его угадать по буквам!.")
        print("---------------------------------------------------------\n")

    def choose_one_char(self):
        "print(str(self.resultPlayerWord) == str(self.randomWord), self.resultPlayerWord, self.randomWord, type(self.randomWord), type(self.resultPlayerWord))"
        "str(self.resultPlayerWord) == str(self.randomWord) - при сравнении они не равны почему-то"
        if not '_' in str(self.resultPlayerWord):
            self.resultGame = True
            return
        suggestChar = input("Выбери любую букву, которая может содержаться в слове")
        if len(suggestChar) > 1:
            raise InputValueException("Вы ввели больше 1 символа")
        "self.validate_input(suggestUserNumber)"
        ind = 0
        newresult = ''
        if suggestChar in self.randomWord:
            while not ind == 5:
                if suggestChar == self.randomWord[ind]:
                    newresult = newresult + suggestChar
                elif not self.resultPlayerWord[ind] == '_':
                    newresult = newresult + self.resultPlayerWord[ind]
                else:
                    newresult = newresult + '_'
                ind = ind + 1
            self.resultPlayerWord = newresult
            print(self.rightAnswer)
            print(self.resultPlayerWord)
        else:
            print(self.wrongAnswer)

    def continue_play(self):
        answer = input('Хотите сыграть еще раз? (y/n)')
        if answer == 'y':
            self.randomWord = random.choice(self.lines)
            self.resultGame = False
            self.resultPlayerWord = '_____'
            self.play()
        else:
            print('Спасибо за игру и до новых встреч на поле ЧУДЕС!')

    def play(self):
        self.show_game_rules()
        """print(self.randomWord)""" "FOR DEBUG"
        while not self.resultGame:
            self.choose_one_char()
        self.continue_play()


if __name__ == '__main__':
    game = PoleChydes()
    game.play()
