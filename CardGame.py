import random

class Card:
    suits = ['Spades', 'Hearts', 'Diamonds', 'Clubs']
    suits_v = {'Spades' : '\u2664', 'Hearts' : '\u2661',
               'Clubs' : '\u2667', 'Diamonds' : '\u2662'}
    values = [None, None, '2', '3', '4', '5', '6', '7',
              '8', '9', '10', 'J', 'Q', 'K', 'A']

    def __init__(self, value, suit):
        """suit + value are ints"""
        self.value = value
        self.suit = suit

    def __gt__(self, another):
        if self.value > another.value :
            return True
        if self.value == another.value :
            if self.suit > another.suit :
                return True
            else :
                return False

    def __str__(self):
        v = self.suits_v[self.suits[self.suit]] + " " + self.values[self.value]
        return v

class Deck:
    def __init__(self):
        self.cards = []
        for i in range(2, 15):
            for j in range(4):
                self.cards.append(Card(i, j))
            random.shuffle(self.cards)

    def remove_card(self):
        if len(self.cards) == 0:
            return None
        return self.cards.pop()

class Player:
    def __init__(self, name):
        self.wins = 0
        self.card = None
        self.name = None

class Game:
    def __init__(self):
        self.deck = Deck()
        self.p1 = Player(input("Player1 name : "))
        self.p2 = Player(input("Player2 name : "))

    def wins(self, winner):
        print(f"{winner} wins.")

    def draw(self, p1n, p1c, p2n, p2c):
        print(f'{p1n}, {p1c}, {p2n}, {p2c}')

    def play_game(self):
