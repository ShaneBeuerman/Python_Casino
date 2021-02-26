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

    def match(self):
        for i in Keno.card:
            if(i in Keno.values):
                Keno.count = Keno.count + 1
        print(Keno.count)
