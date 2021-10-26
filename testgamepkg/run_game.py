"""sys.path.append("C:/Users/Я/PycharmProjects/LearnSoftDevPc/wargame")"""
# optionally print the sys.path for debugging)
# print("in __init__.py sys.path:\n ",sys.path)
from testgamepkg.wargame import AttackOfTheOrcs

game = AttackOfTheOrcs()
game.play()
