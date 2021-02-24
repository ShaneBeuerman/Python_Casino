from Card import Card

class Deck:
    test = "text"
    deck = []
    
    def __init__(self):
        suits = ["Hearts", "Diamonds", "Spades", "Clubs"]
        for i in range(13):
            for j in suits:
                Deck.deck.append(Card(i, j))

    def test(self):
        print("test")

    def shuffle(self):
        print("Shuffling")

    def printDeck(self):
        for i in Deck.deck:
            print(i.suit, i.value)

d = Deck()
d.test()
d.shuffle()
d.printDeck()
