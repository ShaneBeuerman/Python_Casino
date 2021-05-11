from Card import Card
import random

class Deck:
    deck = []
    
    def __init__(self):
        suits = ["♥", "◆", "♠", "♣"]
        for i in range(1, 13):
            for j in suits:
                self.deck.append(Card(j, i))

    def shuffle(self):
        print("Shuffling")
        random.shuffle(self.deck)

    def printDeck(self):
        for i in self.deck:
            print(i.suit, i.value)
    
    def pop(self):
        return self.deck.pop()

    def push(self, card):
        self.deck.append(card)
