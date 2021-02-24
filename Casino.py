#Casino
from Deck import Deck

money = 500

def Cards():

    deck = Deck()
    deck.shuffle()

while money > 0:
    print("You have ", money, " dollars.")
    print("Which game do yo want to play? Pleae type response exactly")
    choice = input("| Cards | Slots | Keno | Exit |")
    if choice == "Cards":
        print("You have selected cards")
        Cards()
    elif choice == "Exit":
        print("Goodbye")
        break
    elif choice == "Slots":
        print("You have chosen the slot machine")
    elif choice == "Keno":
        print("You have chosen to play keno")
    else:
        print("Sorry, but your choice wasn't accepted. Try again.")
        
if money <= 0:
    print("You have no money")
    print("You can't play anymore")
else:
    print("You have ", money, " dollars.")
