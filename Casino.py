#Casino
from Deck import Deck
from Keno import Keno

money = 500

def playCards():

    deck = Deck()
    deck.shuffle()
    deck.printDeck()

def playKeno():
    game = Keno()
    game.printBoard()
    game.chooseCard()
    game.markBoard()
    game.match()
    
    

while money > 0:
    print("You have ", money, " dollars.")
    print("Which game do yo want to play? Pleae type response exactly")
    choice = input("| Cards | Slots | Keno | Exit |")
    if choice == "Cards":
        print("You have selected cards")
        playCards()
    elif choice == "Exit":
        print("Goodbye")
        break
    elif choice == "Slots":
        print("You have chosen the slot machine")
    elif choice == "Keno":
        print("You have chosen to play keno")
        playKeno()
    else:
        print("Sorry, but your choice wasn't accepted. Try again.")
        
if money <= 0:
    print("You have no money")
    print("You can't play anymore")
else:
    print("You have ", money, " dollars.")
