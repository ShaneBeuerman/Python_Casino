import random

class Keno:
    board = []
    values = []
    card = []
    count = 0

    def __init__(self):
        for i in range(1,81):
            Keno.board.append(i)

    def printBoard(self):
        print(Keno.board)

    def chooseCard(self):
        while(len(Keno.card) < 8):
            value = input("Add a value")
            try:
                value = int(value)
                if(value > 80 or value < 0 or value in Keno.card):
                    print("Try again")
                else:
                    Keno.card.append(value)
            except ValueError:
                print("Sorry, not an integer.")
        print(Keno.card)

    def markBoard(self):
        for i in range(20):
            Keno.value = random.choice(Keno.board)
            Keno.board.remove(Keno.value)
            Keno.values.append(Keno.value)
        print(Keno.values)

    def payout(self):
        print("Here are the payouts:")
        print("Match 1 or 2: 0.5 * wager")
        print("Match 3: 1 * Wager")
        print("Match 4: 3 * Wager")
        print("Match 5: 6 * Wager")
        print("Match 6: 19 * Wager")
        print("Match 7: 90 * Wager")
        print("Match 8: 720 * Wager")
        print("This game of keno only allows you to choose eight numbers. No more, no less")

    def match(self, wager):
        count = 0
        for i in Keno.card:
            if(i in Keno.values):
                count = count + 1
        print(count, "Match")
        Keno.card.clear()
        if count == 1:
            print("You win half your wager back")
            return wager / 2
        elif count == 2:
            print("You win half your wager back")
            return wager / 2
        elif count == 3:
            print("You win your wager back")
            return wager
        elif count == 4:
            print("You win three times your wager back")
            return wager * 3
        elif count == 5:
            print("You win six times your wager back")
            return wager * 6
        elif count == 6:
            print("You win ninteen times your wager back")
            return wager * 19
        elif count == 7:
            print("You win ninety times your wager back")
            return wager * 90
        elif count == 8:
            print("You win seven hundred twenty times your wager back")
            return wager * 720
        else:
            print("I'm sorry, you lose.")
            return 0            
