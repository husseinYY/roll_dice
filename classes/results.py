# Encapsulation

class Results():
    def __init__(self):
        self.global_score1 = 0
        self.global_score2 = 0
        self.current_score1 = 0
        self.current_score2 = 0

    def get_global_score(self, player_number):
        if player_number == 1:
            return self.global_score1
        else:
            return self.global_score2

    def add_global_score(self, player_number, value):
        if player_number == 1:
            self.global_score1 += value
        else:
            self.global_score2 += value

    def get_current_score(self, player_number):
        if player_number == 1:
            return self.current_score1
        else:
            return self.current_score2

    def add_current_score(self, player_number, value):
        if player_number == 1:
            self.current_score1 += value
        else:
            self.current_score2 += value

    def check_if_won(self, player_number, final_score):
        if self.get_global_score(player_number) >= final_score:
            return True
        return False

    def reset_current_score(self):
        self.current_score1 = 0
        self.current_score2 = 0
