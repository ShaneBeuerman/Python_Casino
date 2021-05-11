#BlackJack
from Deck import Deck

class Blackjack:
    deck = Deck()
    deck.shuffle()
    hand = []
    dealer = []
    handValue = 0
    dealerValue = 0

    def __init__(self):
        deck = Deck()
        deck.shuffle()
        hand = []
        dealer = []
        handValue = 0
        dealerValue = 0

    def reshuffle(self):
        while self.hand:
            self.deck.push(self.hand.pop())
        while self.dealer:
            self.deck.push(self.dealer.pop())
        self.deck.shuffle()

    def play(self, wager):
        self.handValue = self.hit(self.hand)
        self.dealerValue = self.hit(self.dealer)
        print("Your hand")
        self.handValue = self.displayHand(self.hand)
        print("Dealer's hand")
        self.dealerValue = self.displayHand(self.dealer)
        if self.handValue == 21:
            print("You win")
            self.reshuffle()
            return wager * 2
        elif self.dealerValue == 21:
            print("You lose")
            self.reshuffle()
            return 0
        self.hitOrStand()
        if self.handValue > 21:
            print("You lose")
            self.reshuffle()
            return 0
        self.dealerPlay()
        result = self.compare()
        if result == 'win':
            self.reshuffle()
            return wager * 2
        elif result == 'lose':
            self.reshuffle()
            return 0
        else:
            self.reshuffle()
            return wager

    def hitOrStand(self):
        choice = input("Would you like to hit or stand? Type 'hit' to hit and 'stand' to stand")
        while choice != 'hit' and choice != 'stand':
            print("Please type in either 'hit' or 'stand'")
            choice = input("Would you like to hit or stand?")
        if choice == 'hit':
            print("You decided to hit")
            self.hit(self.hand)
            self.handValue = self.displayHand(self.hand)
            if self.handValue > 21:
                print("You busted")
                return
            self.hitOrStand()
        elif choice == 'stand':
            print("You have decided to stand")

    def displayHand(self, curHand):
        value = 0
        aces = 0
        print("------")
        for card in curHand:
            if card.value == 1:
                print("Ace", card.suit)
                aces += 1
            elif card.value == 11:
                print("Jack", card.suit)
            elif card.value == 12:
                print("Queen", card.suit)
            elif card.value == 13:
                print("King", card.suit)
            else:
                print(card.value, card.suit)
            if card.value >= 10:
                value += 10
            elif card.value == 1:
                value += 11
            else:
                value += card.value
        while aces >= 1 and value > 21:
            value -= 10
            aces -= 1
        print("------")
        print(value)
        return value

    def hit(self, curHand):
        if not curHand:
            curHand.append(self.deck.pop())
            curHand.append(self.deck.pop())
        else:
            curHand.append(self.deck.pop())

    def dealerPlay(self):
        if self.dealerValue > 16:
            print("Dealer stands")
            return
        if self.dealerValue > self.handValue:
            print("Dealer has no need to hit.")
            return
        self.hit(self.dealer)
        self.dealerValue = self.displayHand(self.dealer)
        if self.dealerValue > 21:
            print("Dealer busts")
            return
        self.dealerPlay()

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
        elif self.handValue > 21:
            print("You lose")
            return "lose"
        elif self.dealerValue > 21:
            print("You win")
            return "win"