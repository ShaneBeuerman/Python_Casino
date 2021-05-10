#BlackJack
from Deck import Deck

class Blackjack:
    deck = Deck()
    deck.shuffle()
    hand = []
    dealer = []
    handValue = 0
    dealerValue = 0

    def play(self, wager):
        self.handValue = hit(hand)
        self.dealerValue = hit(dealer)
        self.displayHand(hand)
        self.displayHand(dealer)
        if self.handValue == 21:
            print("You win")
            return wager * 2
        elif self.dealerValue == 21:
            print("You lose")
            return 0
        hitOrStand()
        if busted(self.handValue):
            print("You lose")
            return 0
        dealerPlay()
        compare()

    def hitOrStand(self):
        choice = input("Would you like to hit or stand? Type 'hit' to hit and 'stand' to stand")
        while(choice != 'hit' or choice != 'stand'):
            print("Please type in either 'hit' or 'stand'")
            choice = input("Would you like to hit or stand?")
        if choice == 'hit':
            print("You decided to hit")
            hit(self.hand)
            displayHand(self.hand)
            if busted(self.hand):
                print("You lose")
                return
            hitOrStand()
        elif choice == 'stand':
            print("You have decided to stand")

    def displayHand(self, curHand):
        value = 0
        for card in curHand:
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
            value += card.value
        print(value)

    def hit(self, curHand):
        if not curHand:
            curHand.append(deck.pop(0))
            curHand.append(deck.pop(0))
        else:
            curHand.append(deck.pop(0))

    def busted(self, val):
        if val > 21:
            return True
        else:
            return False

    def dealerPlay(self):
        if dealerValue > 16:
            print("Dealer stands")
            return
        if dealerValue > handValue:
            print("Dealer has no need to hit.")
            return
        hit(dealer)
        if dealerValue > 21:
            print("Dealer busts")
            return
        dealerPlay()

    def compare(self):
        if self.handValue <= 21 and self.dealerValue <= 21:
            if self.handValue > self.dealerValue:
                print("You win")
                return "win"
            elif self.dealerValue > self.handValue:
                print("You lose")
                return "lose"
            else:
                print("Tie")
                return "tie"
        elif busted(self.handValue):
            print("You lose")
            return "lose"
        elif busted(self.dealerValue):
            print("You win")
            return "win"