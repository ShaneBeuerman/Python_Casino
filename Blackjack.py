#BlackJack
from Deck import Deck

class Blackjack:
    deck = Deck()
    deck.shuffle()
    hand = []
    dealer = []
    handValue = 0
    dealerValue = 0

    def hitOrStay(self):
        handValue = hit(hand)
        dealerValue = hit(dealer)
        choice = input("Would you like to hit or stay?")
        if choice == 'hit':
            print("You decided to hit")
        elif choice == 'stay':
            print("You have decided to stay")
        else:
            print("Sorry, but you have not given a satisfactory response.")
            print("Please type in either 'hit' or 'stay'")
            hitOrStay()

    def displayHand(self):
        value = 0
        for card in hand:
            if card.value == 1:
                print("Ace", card.suit)
            elif card.value == 11:
                print("Jack", card.suit)
            elif card.value == 12:
                print("Queen", card.suit)
            elif card.value == 13:
                print("King", card.suit)
            else:
                print(card.value, card.suit)

    def hit(self, curHand):
        if not curHand:
            #hand draws twice
            displayHand()
        else:
            #hand draws once
            displayHand()
            #check if busted
            #if busted:
                #Game ends
            #else:
                #Hit or stay?
        print("To be continued")

    def busted(self, val):
        if val > 21:
            return True
        else:
            return False

    def dealerPlay(self):
        print("Not yet ready")

    def compare(self):
        if handValue <= 21 and dealerValue <= 21:
            if handValue > dealerValue:
                print("You win")
                #payout
            elif dealerValue > handValue:
                print("You lose")
                #no payout
            else:
                print("Tie")
                #pay back your wager
        elif handValue > 21:
            print("You lose")
        elif dealerValue > 21:
            print("You lose")
