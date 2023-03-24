import random

class Die:
    def __init__(self):
        self.face = random.randrange(1, 7)
    def roll(self):
        self.face = random.randrange(1, 7)

class Dice_Game():
    def __init__(self):
        self.dice = [Die() for n in range(2)]

    def play(self):
        for die in self.dice:
            die.roll()

    def win(self):
        sum = 0
        for die in self.dice:
            sum += die.face
            print(die.face, end = ' ')

        if sum > 6:
            print("==> Player Wins")
        else :
            print("==> Computer Wins")

if __name__ == "__main__":
    dicegame = Dice_Game()
    dicegame.play()
    dicegame.win()