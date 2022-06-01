import time
import math
from kolokrzyzgracze import HumanPlayer, RandomComputer

class TicTacToe():
    def __init__(self):
        self.board = self.makeboard()
        self.winner = None
    @staticmethod
    def makeboard():
        return [" " for x in range(9)]
    
    def printboard(self):
        for row in [self.board[i*3: (i+1)*3] for i in range(3)]:
            print("| " + " | ".join(row) + " |")
    @staticmethod
    def printboardnums():
        for row in [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]:
            print("| " + " | ".join(row) + " |")
    def makemove(self, square, letter):
        if self.board[square] == " ":
            self.board[square] = letter
            if self.iswinner(square, letter):
                self.winner = letter
            return True
        return False
    def iswinner(self, square, letter):
        rowind = math.floor(square/3)
        if all([l == letter for l in self.board[rowind*3: (rowind +1)*3]]):
            return True
        colind = square % 3
        if all([l == letter for l in [self.board[colind + i*3] for i in range(3)]]):
            return True
        if square % 2 == 0:
            if all([l == letter for l in [self.board[i] for i in [0, 4, 8]]]):
                return True
            if all([l == letter for l in [self.board[i] for i in [2, 4, 6]]]):
                return True
        return False
    def empty(self):
        return " " in self.board
    def emptycount(self):
        return self.board.count(" ")
    def availablemoves(self):
        return [i for i, x in enumerate(self.board) if x == " "]

def play(game, xplayer, oplayer, printgame=True):
    if printgame:
        game.printboardnums()
    letter = "X"
    while game.empty():
        if letter == "O":
            square = oplayer.get_move(game)
        else:
            square = xplayer.get_move(game)
        if game.makemove(square, letter):
            if printgame:
                print(letter + " wybiera pole: {}".format(square))
                game.printboard()
                print(" ")
            if game.winner:
                if printgame:
                    print(letter+" wygrywa!")
                return letter
            letter = "O" if letter == "X" else "X"
        time.sleep(.8)
    if printgame:
        print("Remis!")

if __name__ == '__main__':
    xplayer = RandomComputer("X")
    oplayer = HumanPlayer("O")
    t = TicTacToe()
    play(t, xplayer, oplayer, printgame=True)