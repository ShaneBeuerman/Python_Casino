from Card import Card
import random

class Deck:
    deck = []
    
    def __init__(self):
        suits = ["Hearts", "Diamonds", "Spades", "Clubs"]
        for i in range(13):
            for j in suits:
                Deck.deck.append(Card(i, j))

    def shuffle(self):
        print("Shuffling")
        n = len(Deck.deck)
        for i in range(0,n):
            rand = random.randint(0, n-1)
            Deck.deck[i], Deck.deck[rand] = Deck.deck[rand], Deck.deck[i]

    def printDeck(self):
        for i in Deck.deck:
            print(i.suit, i.value)
