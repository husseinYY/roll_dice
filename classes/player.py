import shutil


class Player():
    def __init__(self):
        self.player_number = 1

    def change_player(self):
        if self.player_number == 1:
            self.player_number = 2
        else:
            self.player_number = 1

    def get_player_number(self):
        return self.player_number


# Inheritance
class Player1(Player):
    def __init__(self, player_name, player_color):
        super().__init__()
        self.player_name = player_name
        self.player_color = player_color

    def get_player_name(self):
        return self.player_name

    def get_player_color(self):
        return self.player_color


class Player2(Player):
    def __init__(self, player_name, player_color):
        super().__init__()
        self.player_name = player_name
        self.player_color = player_color

    def get_player_name(self):
        return self.player_name

    def get_player_color(self):
        return self.player_color
