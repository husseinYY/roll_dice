game_name = "Roll Dice"

# GAME RULES:
game_rules = """
- The game has 2 players, playing in rounds
- In each turn, a player rolls a dice as many times as he whishes. Each result get added to his ROUND score
- BUT, if the player rolls a 0, all his ROUND score gets lost. After that, it's the next player's turn
- The player can choose to 'Hold', which means that his ROUND score gets added to his GLOBAL score. After that, it's the next player's turn
- The first player to reach 100 points on GLOBAL score wins the game

"""

help_menu = """
- s:- start the game(works only here)
- rules:- game rules(works only here)
- help:- this menu(works only here)
- r:- roll the dice(works only in the game)
- h: hold the dice(works only in the game)
- x: exit the game(works in the game only)
- n: new game(works in the game only)

"""


def print_separators(stop):
    separator = ""
    for i in range(int(stop / 2 - len(game_name))):
        separator = separator + "-"
    return separator

# Bash colors


style = {
    "p": '\033[95m',
    "b": '\033[94m',
    "c": '\033[96m',
    "g": '\033[92m',
    "y": '\033[93m',
    "r": '\033[91m',
    "BOLD": '\033[1m',
    "UNDERLINE": '\033[4m',
    "END": '\033[0m'
}

dice_information = {
    0: (
        "┌─────────┐",
        "│         │",
        "│         │",
        "│         │",
        "└─────────┘",
    ),
    1: (
        "┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘",
    ),
    2: (
        "┌─────────┐",
        "│  ●      │",
        "│         │",
        "│      ●  │",
        "└─────────┘",
    ),
    3: (
        "┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│      ●  │",
        "└─────────┘",
    ),
    4: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘",
    ),
    5: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘",
    ),
    6: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘",
    ),
}
