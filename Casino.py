#Casino
from Deck import Deck
from Keno import Keno
from Slot_Machine import slotmachine

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
    
def playSlots():
    global money
    print("You have", money, "dollars")
    while True:
        wager = input("Would you like to pay 5, 10, 50, or 100 dollars to play the slotmachine?")
        try:
            wager = int(wager)
        except ValueError:
            print("Sorry, not an acceptable input")
            continue
        if wager > money:
            print("Sorry, you don't have enough money")
        elif wager != 5 and wager != 10 and wager != 50 and wager != 100:
            print("Sorry, you can't bet that much money.")
        else:
            print("Thank you for your payment")
            money = money - wager
            break
        
    slots = slotmachine()
    winnings = slots.play(wager)
    print("Winnings are", winnings)
    money += winnings



while money > 0:
    print("You have", money, "dollars.")
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
        playSlots()
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
