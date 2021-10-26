
"""ch01_ex02

A text-based game to acquire a hut by defeating the enemy (functional)

This is a supporting example code for example 2 of Chapter 1. It is a
command line program that illustrates use of Python functions.
The player inputs a hut number. If the occupant is an enemy, the player is
given an option to 'attack'. Player wins if he defeats the enemy.
In the aforementioned book this is also referred to as
"Attack of the Orcs v0.0.5". More details can be found in the relevant
chapter of the book..

RUNNING THE PROGRAM:
--------------------
- Python 3.5.x must be installed on your system.
- It is assumed that you have Python 3.5 available in your environment
  variable PATH. It will be typically available as 'python' or 'python3'.
- Here is the command to execute this code from command prompt

        $ python ch01_ex02.py     ( OR $ python3 ch01_ex02.py)

- See the README file for more information. Or visit python.org for OS
  specific instructions on executing Python from a command prompt.

.. todo::

1. The code comments and function descriptions in this file are
   intentionally kept to a minimum! See a later chapter of the book to
   learn about the code documentation and best practices!
   Feel free to add documentation after reading that chapter.
   Description of the code can be found in the book.


:license: The MIT License (MIT) . See LICENSE file for further details.
"""

import random
import textwrap
import sys


def show_theme_message(width):
    """Print the game theme in the terminal window"""
    print_dotted_line()
    print_bold("Attack of The Orcs v0.0.5:")
    msg = (
        "The war between humans and their arch enemies, Orcs, was in the "
        "offing. Sir Foo, one of the brave knights guarding the southern "
        "plains began a long journey towards the east through an unknown "
        "dense forest. On his way, he spotted a small isolated settlement."
        " Tired and hoping to replenish his food stock, he decided to take"
        " a detour. As he approached the village, he saw five huts. There "
        "was no one to be seen around. Hesitantly, he  decided to enter..")

    print(textwrap.fill(msg, width=width))


def show_game_mission():
    """Print the game mission in the terminal window"""
    print_bold("Mission:")
    print("\tChoose a hut where Sir Foo can rest...")
    print_bold("TIP:")
    print("Be careful as there are enemies lurking around!")
    print_dotted_line()


def reveal_occupants(idx, huts):
    """Print the occupants of the hut"""
    msg = ""
    print("Revealing the occupants...")
    for i in range(len(huts)):
        occupant_info = "<%d:%s>" % (i+1, huts[i])
        if i + 1 == idx:
            occupant_info = "\033[1m" + occupant_info + "\033[0m"
        msg += occupant_info + " "

    print("\t" + msg)
    print_dotted_line()


def occupy_huts():
    """Randomly populate the `huts` list with occupants"""
    huts = []
    occupants = ['enemy', 'friend', 'unoccupied']
    while len(huts) < 5:
        computer_choice = random.choice(occupants)
        huts.append(computer_choice)
    return huts


def process_user_choice():
    """Accepts the hut number from the user"""
    msg = "\033[1m" + "Choose a hut number to enter (1-5): " + "\033[0m"
    user_choice = input("\n" + msg)
    idx = int(user_choice)
    return idx


def show_health(health_meter, bold=False):
    """Show the remaining hit points of the player and the enemy"""
    msg = "Health: Sir Foo: %d, Enemy: %d" \
          % (health_meter['player'], health_meter['enemy'])
    if bold:
        print_bold(msg)
    else:
        print(msg)


def reset_health_meter(health_meter):
    """Reset the values of health_meter dict to the original ones"""
    health_meter['player'] = 40
    health_meter['enemy'] = 30


def print_bold(msg, end='\n'):
    """Print a string in 'bold' font"""
    print("\033[1m" + msg + "\033[0m", end=end)


def print_dotted_line(width=72):
    """Print a dotted (rather 'dashed') line"""
    print('-'*width)


def attack(health_meter):
    """The main logic to determine injured unit and amount of injury"""
    """Get random target of hit in 60% - enemy, 40% - player"""
    hit_list = 4 * ['player'] + 6 * ['enemy']
    injured_unit = random.choice(hit_list)
    hit_points = health_meter[injured_unit]
    """Get random damage from 10 to 15 and decrease health for chosen target, but nor lower than 0"""
    injury = random.randint(10, 15)
    health_meter[injured_unit] = max(hit_points - injury, 0)
    print("ATTACK! ", end='')
    show_health(health_meter)


def check_hut(huts, idx, health_meter):
    """Check hut for occupied"""
    if huts[idx - 1] != 'enemy':
        print_bold("Congratulations! YOU WIN!!!")
        return False
    else:
        print_bold('ENEMY SIGHTED! ', end='')
        show_health(health_meter, bold=True)
        return True


def check_defeat(health_meter):
    """Check who lose in fight"""
    if health_meter['enemy'] <= 0:
        print_bold("GOOD JOB! Enemy defeated! YOU WIN!!!")
        return True
    if health_meter['player'] <= 0:
        print_bold("YOU LOSE  :(  Better luck next time")
        return True


def play_game(health_meter):
    """The main control function for playing the game"""
    huts = occupy_huts()
    idx = process_user_choice()
    reveal_occupants(idx, huts)
    """Check who in chosen hut"""
    continue_attack = check_hut(huts, idx, health_meter)
    # Loop that actually runs the combat if user wants to attack
    while continue_attack:
        continue_attack = input(".......continue attack? (y/n): ")
        if continue_attack == 'n':
            print_bold("RUNNING AWAY with following health status...")
            show_health(health_meter, bold=True)
            print_bold("GAME OVER!")
            break
        attack(health_meter)
        if check_defeat(health_meter):
            break


def run_application():
    """Top level control function for running the application."""
    keep_playing = 'y'
    health_meter = {}
    reset_health_meter(health_meter)
    show_game_mission()

    while keep_playing == 'y':
        reset_health_meter(health_meter)
        play_game(health_meter)
        keep_playing = input("\nPlay again? Yes(y)/No(n): ")


if __name__ == '__main__':
    run_application()
