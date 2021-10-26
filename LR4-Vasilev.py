

"""attackoftheorcs_v_1_1

A text-based game to acquire a hut by defeating the enemy(handle exceptions)

This module is compatible with Python 3.5.x. It contains
supporting code for the book, Learning Python Application Development,
Packt Publishing.

General game play:
The player inputs a hut number. If the occupant is an enemy, the player is
given an option to 'attack'. Player wins if he defeats the enemy.
Additionally,the player can 'run away' from the combat, get healed
in friendly hut and then resume the fight.

In the aforementioned book this is also referred to as
"Attack of the Orcs v1.1.0". More details can be found in the relevant
chapter of the book..

Demonstrates use of Abstract Base Class (ABC) in Python. This module
is based on code from file ch01_ex03_AbstractBaseClass.py of Chapter 1

What's new in this module then?
- Implements some try...except clauses to demonstrate exception handling.
  Examples:
  - It fixes the invalid input problem while choosing the hut number.
  - The heal method, under certain conditions now raises a custom exception
    called 'GameUnitError'. This is used by heal_exception_example.py

Usage: It is primarily meant to be used along with heal_exception_example.py
        But you can also run this standalone as noted below:

RUNNING THE PROGRAM:
--------------------
- Python 3.5.x must be installed on your system.
- It is assumed that you have Python 3.5 available in your environment
  variable PATH. It will be typically available as 'python'
- Here is the command to execute this code from command prompt

        $ python attackoftheorcs_v1_1.py

- See the README file for more information. Or visit python.org for OS
  specific instructions on executing Python from a command prompt.

.. todo::

1. The code comments and function descriptions in this file are
   intentionally kept to a minimum! See a later chapter of the book to
   learn about the code documentation and best practices!
   Feel free to add documentation after reading that chapter.
   Description of the code can be found in the book.
2. Split the code into smaller modules
3. See the other TODO comments..things you can try fixing as an exercise!

:copyright: 2016, Ninad Sathaye

:license: The MIT License (MIT) . See LICENSE file for further details.
"""
import random
import sys

if sys.version_info < (3, 0):
    print("This code requires Python 3.x and is tested with version 3.5.x ")
    print("Looks like you are trying to run this using "
          "Python version: %d.%d " % (sys.version_info[0],
                                      sys.version_info[1]))
    print("Exiting...")
    sys.exit(1)















