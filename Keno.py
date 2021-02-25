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
        while(len(card) < 8):
            value = input("Add a value")
            try:
                value = int(value)
                if(value > 80 or value < 0 or value in card):
                    print("Try again")
                else:
                    card.append(value)
            except ValueError:
                print("Sorry, not an integer.")
        print(card)

    def markBoard(self):
        for i in range(20):
            value = random.choice(board)
            board.remove(value)
            values.append(value)
        print(values)

    def match(self):
        for i in card:
            if(i in values):
                count = count + 1
        print(count)
