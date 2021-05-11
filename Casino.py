#Casino
from Deck import Deck
from Keno import Keno
from Blackjack import Blackjack
from Slot_Machine import slotmachine

money = 500

def playCards():
    global money
    game = Blackjack()
    print("You have", money, "dollars")
    payment = input("Would you like to play blackjack? Type y for yes, anything else for no.")
    if payment == 'y':
        wager = input("Would you like to pay ten dollars to play blackjack? y/n")
        if wager == 'y':
            print("Let's play")
            wager = 10
            money = money - wager
            print("Wager is 10 dollars")
            winnings = game.play(wager)
            print("Winnings are", winnings)
            money += winnings
        elif wager == 'n':
            print("Okay, we'll return you to the beginnning.")
            return
        else:
            print("Sorry, not accepatble input.")
            playCards()

def playKeno():
    global money
    game = Keno()
    print("You have", money, "dollars")
    payment =input("Would you like to see the payouts? Type y for yes, anything else for no.")
    if payment == "y":
        game.payout()
    while True:
        wager = input("Would you like to pay ten dollars to play keno? y/n")
        if wager == "y":
            print("Let's play")
            wager = 10
            money = money - wager
            break
        elif wager == "n":
            print("Okay, we'll return to the beginning.")
            return
        else:
            print("Sorry, not acceptable input.")
            print("Try y for yes and n for no.")
    print("Wager is", wager)
    game.printBoard()
    game.chooseCard()
    game.markBoard()
    winnings = game.match(wager)
    print("Winnings are", winnings)
    money += winnings
    
def playSlots():
    global money
    slots = slotmachine()
    print("You have", money, "dollars")
    payouts = input("Would you like to see the payouts? Type y for yes, anything else for no.")
    if payouts == "y":
        slots.payout()
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
