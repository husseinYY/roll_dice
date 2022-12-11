from classes import game, player
from config import style, game_rules
import os

# CODE EXPLANATION:-

# CLASS 'GAME' has all the game rules-related methods
# CLASS 'RESULTS' has all the game results and scores
# CLASS 'PLAYERS' has all the details about the players;
# CLASS 'PLAYER' inherits has all the details about the players;


def init():
    # Initialization:
    # - This is where you make an instance of a class.
    # - You call the class by calling it's name
    # - The object takes params the same number that was declared in the __init__ method in the class
    # After you make an instance, you can invoke the methods inside of it
    # Making an instance of a class is not required though, because you can use the abstraction property of the OOP by just calling the class name without invoking it with () and then calling the method needed. But you have to put the decorator @staticmethod over the method.
    # @staticmethod doesn't give `self` because it doesn't have `self` in the first place
    # @classmethod is another decorator that can be added, but, it has a cls param that gives away the whole class...
    # Static Method
    game.Game.print_game_name()
    dice_game = game.Game()

    # A method that starts the game.
    # The method is inside Game class and we need to make instance before we call it.
    dice_game.start()


if __name__ == '__main__':
    init()
