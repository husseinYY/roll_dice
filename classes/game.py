from config import *
from random import randint
import shutil

from classes import player, results

# Abstraction

# Encapsulation


class Game():
    # Constructor
    def __init__(self):
        self.final_score = 0
        self.is_playing = True

    @staticmethod
    def print_game_name():
        print(game_name)

    def get_final_score(self):
        keep_looping = True
        while keep_looping:
            try:
                self.final_score = int(
                    input("Enter the final score where the game should end at:- "))
                keep_looping = False
            except:
                print("Only numbers are allowed")

    def get_player_data(self):
        print("Enter the name of the players and their favorite colors")
        player1 = input("Name of the player 1:- ")
        player2 = input("Name of the player 2:- ")
        print("List of colors to choose from(Enter it's first letter):- ")
        print(f"{style['p']}Pink:- {style['END']}")
        print(f"{style['b']}Blue:- {style['END']}")
        print(f"{style['c']}CYAN:- {style['END']}")
        print(f"{style['g']}GREEN:- {style['END']}")
        print(f"{style['y']}YELLOW:- {style['END']}")
        print(f"{style['r']}RED:- {style['END']}")
        color1 = input("Letter of the color for the player 1:- ").lower()[0]
        color2 = input("Letter of the color for the player 2:- ").lower()[0]
        if color1 not in ['p', 'b', 'c', 'g', 'y', 'r']:
            if color2 != 'b':
                print("You chose a color that doesn't exit, so we chose blue for you")
                color1 = 'b'
            else:
                print("You chose a color that doesn't exit, so we chose red for you")
                color1 = 'r'
        if color2 not in ['p', 'b', 'c', 'g', 'y', 'r']:
            if color1 != 'b':
                print("You chose a color that doesn't exit, so we chose blue for you")
                color2 = 'b'
            else:
                print("You chose a color that doesn't exit, so we chose red for you")
                color2 = 'r'

        return {'player1': player1, 'player2': player2, 'color1': color1, 'color2': color2}

    def print_game_details(self):
        self.get_final_score()
        span = shutil.get_terminal_size().columns
        print(
            f"{style['BOLD']}{print_separators(span)} {game_name} {print_separators(span)}{style['END']}".center(span))
        print(
            f"{style['UNDERLINE']}The game is of:- {self.final_score} {style['END']}".center(span))

    def roll_dice(self, player_color):
        span = shutil.get_terminal_size().columns - 50
        dice = randint(0, 6)
        for i in range(5):
            print(
                f"{style[player_color]}{dice_information[dice][i]}".center(span))
        return dice

    def show_details(self, results, player1, player2, player_number):
        span = shutil.get_terminal_size().columns - 50
        print(
            f"{style[player1.get_player_color()]}{player1.get_player_name()}{style['END']}\t\t\t\t\t\t\t{style[player2.get_player_color()]}\t{player2.get_player_name()}{style['END']}\t\t\t\t\t\t".center(span))
        print(
            f"{style[player1.get_player_color()]}GLOBAL SCORE:- {results.get_global_score(1)}/{self.final_score}{style['END']}\t\t\t\t\t\t\t{style[player2.get_player_color()]}GLOBAL SCORE:- {results.get_global_score(2)}/{self.final_score}{style['END']}\t\t\t\t\t\t".center(span))
        print(
            f"{style[player1.get_player_color()]}CURRENT SCORE:- {results.get_current_score(1)}{style['END']}\t\t\t\t\t\t\t{style[player2.get_player_color()]}CURRENT SCORE:- {results.get_current_score(2)}{style['END']}\t\t\t\t\t\t".center(span))
        # Message passing!
        player_name = player1.get_player_name(
        ) if player_number == 1 else player2.get_player_name()
        player_color = player1.get_player_color(
        ) if player_number == 1 else player2.get_player_color()
        print(
            f"{style['BOLD']}{style[player_color]}It's {player_name}'s turn. Press R to roll the dice and H to hold it, to count your current score(X: exit, N: New game):- {style['END']}{style['END']}".center(span))

    def help_menu(self):
        print(help_menu)

    def rules(self):
        print(game_rules)

    def start(self):
        keep_looping = True
        while keep_looping:
            self.help_menu()
            action = input().lower()
            if action == 's':
                # Start the game
                keep_looping = False
                self.play()
            elif action == 'help':
                self.help_menu()
            elif action == 'rules':
                # Print game rules;
                self.rules()
            elif action in ['r', 'x', 'h', 'n']:
                print("This works in the game only")
            else:
                print("Wrong choice")

    def play(self):
        self.print_game_details()
        data = self.get_player_data()

        player1_controller = player.Player1(data['player1'], data['color1'])
        player2_controller = player.Player2(data['player2'], data['color2'])
        # Polymorphism;
        player_controller = player.Player()
        results_controller = results.Results()
        won = False
        while self.is_playing:
            while True and won == False:
                self.show_details(results_controller, player1_controller,
                                  player2_controller, player_controller.get_player_number())
                action = input().upper()
                player_number = 1 if player_controller.get_player_number() == 1 else 2
                color = player1_controller.get_player_color(
                ) if player_controller.get_player_number() == 1 else player2_controller.get_player_color()
                if action == "R":
                    dice = self.roll_dice(color)
                    results_controller.add_current_score(
                        player_controller.get_player_number(), dice)
                    if dice == 0:
                        results_controller.reset_current_score()
                        player_controller.change_player()
                        break
                elif action == "H":
                    if results_controller.check_if_won(player_number, self.final_score):

                        # The player won the game
                        # Inheritance
                        self.show_the_winner(player_number)
                        self.is_playing = False
                        won = True
                        break

                    else:
                        current_score = results_controller.get_current_score(
                            player_controller.get_player_number())
                        results_controller.add_global_score(
                            player_controller.get_player_number(), current_score)
                        results_controller.reset_current_score()
                        player_controller.change_player()
                elif action == "X":
                    self.is_playing = False
                    self.exit_the_game()
                    break

                elif action == "N":
                    print("NEW GAME STARTED")
                    self.play()
                else:
                    print("YOU ENTERED SOMETHING WRONG")

    def show_the_winner(self, winner_number):
        span = shutil.get_terminal_size().columns
        print(
            f"{style['BOLD']}{style['r']} Player {winner_number} WON THE GAME! {style['END']}".center(span))

    def exit_the_game(self):
        span = shutil.get_terminal_size().columns
        print(
            f"{style['BOLD']}{style['r']}{print_separators(span)} GAME EXITED! {print_separators(span)}{style['END']}".center(span))
