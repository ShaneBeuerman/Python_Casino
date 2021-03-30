from Card import Card
import random

class Deck:
    deck = []
    
    def __init__(self):
        suits = ["♥", "◆", "♠", "♣"]
        for i in range(13):
            for j in suits:
                self.deck.append(Card(i, j))

    def shuffle(self):
        print("Shuffling")
        random.shuffle(self.deck)

    def printDeck(self):
        for i in self.deck:
            print(i.suit, i.value)
