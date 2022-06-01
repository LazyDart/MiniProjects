import random

class Player():
    def __init__(self, letter):
        self.letter = letter

    def get_move(self, game):
        pass

class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)
    
    def get_move(self, game):
        valid_square = False
        val = None
        while not valid_square:
            square = input(f"{self.letter}, które pole wybierasz?(0-8): ")
            try:
                val = int(square)
                if val not in game.availablemoves():
                    raise ValueError
                valid_square = True
            except ValueError:
                print("Niewłaściwe pole, spróbuj jeszcze raz!")
        return val

class RandomComputer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        square = random.choice(game.availablemoves())
        return square
